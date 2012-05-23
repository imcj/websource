#!/usr/bin/env python

import os
import sys
import yaml 
import json
import shutil
import filecmp
import subprocess
import argparse
import os.path
import base64
import hmac
import hashlib
import urllib
import urllib2

UPLOAD_SERVER = 'http://upload.sae.sina.com.cn'
DEPLOY_SERVER = 'http://deploy.sae.sina.com.cn'
SVN_SERVER = 'https://svn.sinaapp.com/'
LOCAL_CACHE_DIR = os.path.expanduser('~/.saecloud')

# from sae import storage

def setprogress(text, frac):
    # if sys.stdout.isatty():
        # sys.stdout.write(erase_to_start)
        # sys.stdout.write(unsave)

    sys.stdout.write("%s ... %d%%" % (text, int(100*frac)))
    if not sys.stdout.isatty():
        sys.stdout.write(os.linesep)

    sys.stdout.flush()
    
def uploadfile2(filename, remote_filename, appinfo, domain):
    offset = 0
    chunk_size = 1024 * 256
    token = '0'

    file_size = os.stat(filename).st_size

    appname, accesskey, secretkey = appinfo

    _domain = '%s-%s' % (appname, domain)
    fixed_headers = {
        'FileName': remote_filename,
        'FileSize': file_size,
        'Extra': 'storengine: stor; acl: reserve; domain: %s' % _domain,
        'User-Agent': 'SaeSdk',
        'AccessKey': accesskey,
    }

    def get_signature(key, msg):
        h = hmac.new(key, msg, hashlib.sha256)
        return base64.b64encode(h.digest())

    upload_file = open(filename)
    while True:
        upload_file.seek(offset)
        c = upload_file.read(chunk_size)
        checksum = hashlib.md5(c).hexdigest()

        end = min(offset + chunk_size, file_size)
        headers = {
            'FileRange': '%d-%d' % (offset, end),
            'FileRangeChecksum': checksum,
            'Signature': get_signature(secretkey, checksum),
            'Token': token,
            'Content-type': 'application/octet-stream',
            'Content-length': len(c),
        }
        headers.update(fixed_headers)

        url = UPLOAD_SERVER + '/uploader'
        req = urllib2.Request(url, c, headers)

        try:
            rep = urllib2.urlopen(req, None, 5).read()
        except urllib2.URLError, e:
            continue
        except:
            break
        # except:
        #            import pdb
        #            pdb.set_trace ()

        code, message = rep.split(':', 1)
        
        if code == '0':
            token = message
        elif code == '1':
            # upload finished finally
            break
        else:
            raise Exception("Server returned: %s" % rep)

        offset += chunk_size

        setprogress("Uploading %s\n" % filename.decode("utf-8", "ignore"), float(end)/file_size)

    setprogress("Uploading %s\n" % filename.decode("utf-8", "ignore"), 1.0)

# uploadfile2("storage.py", "222/1111", appinfo, "source" )
# client = storage.Client ( "mwo02xkw05", "kzxy1h324mhwxjm4ky5k0x14hmiyiwwxky4j02i2", "websource")

# uploadObject = storage.Object ( "hello" )
# client.put ( "source", "hello", uploadObject )