#!/usr/bin/env python
#!-*- encoding:utf-8 -*-

import gen
import storage
import os
import sys
import setting

try:
    source = sys.argv[1]
except IndexError:
    print u"Error special source directory."
    
if source[0] == ".":
    source= os.path.abspath ( source )
class SaePath ( gen.PathScan ):
    def process_index ( self, context ):
        storage.uploadfile2 ( context['gen_index_path'], context['gen_index_path'], setting.appinfo, "source" )
        
    def process_source ( self, context ):
        storage.uploadfile2 ( context['gen_source_path'], context['gen_source_path'], setting.appinfo, "source" )
SaePath ( source, "twitter/highlight")
