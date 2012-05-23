#!/usr/bin/env python
#!-*- encoding:utf-8 -*-
import os
import sys
import pystache

def _gen ( path,context ):
    cache_flag = ""#len ( context['path'] ) == 0 and ' manifest="cache.manifest"' or ""
    
    return pystache.render ( u"""<!DOCTYPE html>
<html%s>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="{{media_abs_path}}media/bootstrap/css/bootstrap.css" rel="stylesheet">
        <link href="{{media_abs_path}}media/bootstrap/css/bootstrap-responsive.css" rel="stylesheet">
        <link rel="stylesheet" href="{{media_abs_path}}media/default.css">
        <title>{{title}}</title>
        <!-- Le HTML5 shim, for IE6-8 support of HTML5 elements -->
        <!--[if lt IE 9]>
              <script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>
        <![endif]-->
        <link rel="shortcut icon" href="../{{media_abs_path}}/media/bootstrap/ico/favicon.ico">
    </head>
    <body>
        <div class="navbar navbar-fixed-top">
            <div class="navbar-inner">
                <div class="container">
                    <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                     </a>
                     <a class="brand" href="#">Example</a>
                     <div class="nav-collapse">
                         <ul class="nav">
                            <li class="active"><a href="#">Code</a></li>
                          </ul>
                      </div><!--/.nav-collapse -->
                  </div>
            </div>
        </div>
        <div class="container">
            <table class="table table-bordered">
                <tbody>
                    {{#dirs}}
                    <tr><td><a href="{{.}}/index.html">{{.}}</a></td></tr>
                    {{/dirs}}
                    {{#files}}
                    <tr><td><a href="{{.}}.html">{{.}}</a></td></tr>
                    {{/files}}
                </tbody>
            </table>
        </div>
        <script src="{{media_abs_path}}media/bootstrap/js/jquery.js"></script>
        <script src="{{media_abs_path}}media/bootstrap/js/google-code-prettify/prettify.js"></script>
        <script src="{{media_abs_path}}media/bootstrap/js/bootstrap-transition.js"></script>
        <script src="{{media_abs_path}}media/bootstrap/js/bootstrap-alert.js"></script>
        <script src="{{media_abs_path}}media/bootstrap/js/bootstrap-modal.js"></script>
        <script src="{{media_abs_path}}media/bootstrap/js/bootstrap-dropdown.js"></script>
        <script src="{{media_abs_path}}media/bootstrap/js/bootstrap-scrollspy.js"></script>
        <script src="{{media_abs_path}}media/bootstrap/js/bootstrap-tab.js"></script>
        <script src="{{media_abs_path}}media/bootstrap/js/bootstrap-tooltip.js"></script>
        <script src="{{media_abs_path}}media/bootstrap/js/bootstrap-popover.js"></script>
        <script src="{{media_abs_path}}media/bootstrap/js/bootstrap-button.js"></script>
        <script src="{{media_abs_path}}media/bootstrap/js/bootstrap-collapse.js"></script>
        <script src="{{media_abs_path}}media/bootstrap/js/bootstrap-carousel.js"></script>
        <script src="{{media_abs_path}}media/bootstrap/js/bootstrap-typeahead.js"></script>
        <script src="{{media_abs_path}}media/bootstrap/js/application.js"></script>
    </body>
</html>
        """ % cache_flag,
        context)
        
def _gen_source ( path, context ):
    return pystache.render  ( u"""<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="{{media_abs_path}}media/bootstrap/css/bootstrap.css" rel="stylesheet">
        <link href="{{media_abs_path}}media/bootstrap/css/bootstrap-responsive.css" rel="stylesheet">
        <link rel="stylesheet" href="{{media_abs_path}}media/default.css">
        <script src="{{media_abs_path}}media/highlight/highlight.pack.js"></script>
        <script type="text/javascript">
        hljs.initHighlightingOnLoad();
        </script>
        <link rel="stylesheet" href="{{media_abs_path}}media/highlight/styles/default.css">
        <title>{{title}}</title>
        <!-- Le HTML5 shim, for IE6-8 support of HTML5 elements -->
        <!--[if lt IE 9]>
              <script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>
        <![endif]-->
        <link rel="shortcut icon" href="../{{media_abs_path}}/media/bootstrap/ico/favicon.ico">
    </head>
    <body data-spy="scroll" data-target=".subnav" data-offset="50">
        <div class="navbar navbar-fixed-top">
            <div class="navbar-inner">
                <div class="container">
                    <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                     </a>
                     <a class="brand" href="#">Example</a>
                     <div class="nav-collapse">
                         <ul class="nav">
                            <li class="active"><a href="#">Code</a></li>
                            <li class="active"><a href="#">Code</a></li>
                            <li class="active"><a href="#">Code</a></li>
                          </ul>
                      </div>
                  </div>
            </div>
        </div>
        <div class="container">
            <pre>
                <code>{{content}}</code>
            </pre>
        </div>
        <script src="{{media_abs_path}}media/bootstrap/js/jquery.js"></script>
        <script src="{{media_abs_path}}media/bootstrap/js/google-code-prettify/prettify.js"></script>
        <script src="{{media_abs_path}}media/bootstrap/js/bootstrap-transition.js"></script>
        <script src="{{media_abs_path}}media/bootstrap/js/bootstrap-alert.js"></script>
        <script src="{{media_abs_path}}media/bootstrap/js/bootstrap-modal.js"></script>
        <script src="{{media_abs_path}}media/bootstrap/js/bootstrap-dropdown.js"></script>
        <script src="{{media_abs_path}}media/bootstrap/js/bootstrap-scrollspy.js"></script>
        <script src="{{media_abs_path}}media/bootstrap/js/bootstrap-tab.js"></script>
        <script src="{{media_abs_path}}media/bootstrap/js/bootstrap-tooltip.js"></script>
        <script src="{{media_abs_path}}media/bootstrap/js/bootstrap-popover.js"></script>
        <script src="{{media_abs_path}}media/bootstrap/js/bootstrap-button.js"></script>
        <script src="{{media_abs_path}}media/bootstrap/js/bootstrap-collapse.js"></script>
        <script src="{{media_abs_path}}media/bootstrap/js/bootstrap-carousel.js"></script>
        <script src="{{media_abs_path}}media/bootstrap/js/bootstrap-typeahead.js"></script>
        <script src="{{media_abs_path}}media/bootstrap/js/application.js"></script>
    </body>
</html>
        """,
        context)
        
class Path:
    """
    >>> path = Path ()
    """
    def __init__ ( self ):
        pass
        
    def relative_path ( self, current, dest ):
        """
        >>> path = Path ()
        >>> path.relative_path ( "/tmp/gen/gen.py", "/tmp/gen.pid" )
        '../gen.pid'
        >>> path.relative_path ( "/tmp/gen/bin/gen.py", "/tmp/gen.pid" )
        '../../gen.pid'
        >>> path.relative_path ( "/tmp/1.pid", "/tmp/gen.pid" )
        'gen.pid'
        >>> path.relative_path ( "/", "/tmp/gen.pid" )
        'tmp/gen.pid'
        """
        current = os.path.dirname ( current ).split ( os.sep )[1:]
        dest = dest.split ( os.sep )[1:]
        
        if len ( current ) == 1 and current[0] == "":
            del current[0]

        found = 0
        for i in range ( len ( current ) ):
            try:
                if current[i] == dest[i]:
                    found += 1
            except IndexError:
                break
        _relative_path = "../" * ( len ( current ) - found )
                
        return _relative_path + "/".join ( dest[found:] )

class PathScan ( Path ):
    def __init__ ( self, path, out = 'gen' ):
        """
        >>> scan = PathScan ( os.path.abspath ( "./highlight" ) )
        """
        self._path = path
        self._out  = out
        
        if path[0] == ".":
            self._path = os.path.abspath ( path )
            
        for path, dirs, files in os.walk ( self._path ):
            self.generate_index (
                path.decode ( 'utf-8' ),
                [ d.decode ( 'utf-8' ) for d in dirs ],
                [ f.decode ( 'utf-8' ) for f in files ] )
                
    def _context ( self ):
        return {
            
        }
        
    def generate_index ( self, path, dirs, files ):
        relative_path = os.sep.join ( self.relative_path ( self._path, path ).split ( "/" )[1:] )
        context = {
            "abs_path" : path,
            "dirs" : dirs,
            "files" : files,
            "relative_path" : relative_path,
            "media_abs_path" : self.relative_path ( os.path.join ( self._out, relative_path, "fixme" ), os.path.join ( self._out ) )
        }
        
        g = _gen ( path, context )
        _gen_index_path = os.path.join ( self._out, relative_path, "index.html" )
        context['gen_index_path'] = _gen_index_path
        try:
            os.makedirs ( os.path.dirname ( _gen_index_path ) )
        except OSError:
            pass
        
        context['index'] = g
        fd = open ( _gen_index_path, "w" )
        fd.write ( g.encode ( "utf-8" ) )
        fd.close ( )
        
        try:
            self.process_index ( context )
        except AttributeError:
            pass
        # sys.exit ()
        
        for f in files:
            self.generate_source ( f, context.copy () )
    
    def generate_source ( self, path, context ):
        relative_path = os.sep.join ( self.relative_path ( self._path, context['abs_path'] ).split ( "/" )[1:] )
        source_path = os.path.join ( context['abs_path'], path )
        gen_path = os.path.join ( self._out, relative_path, "%s.html" % path )
        
        fd = open ( source_path, "rb" )
        content = fd.read ()
        content = content.decode("utf-8", "ignore")
        if "\0" in content:
            fd.close ()
            return
        fd.close ()
        context['content'] = content
        context['gen_source_path'] = gen_path

        source_content = _gen_source ( path, context )

        source_fd = open ( gen_path, "w+" )
        source_fd.write ( source_content.encode("utf-8") )
        source_fd.close ()
        
        try:
            self.process_source ( context )
        except AttributeError:
            pass
        
"""
if "__main__" == __name__:
    import doctest
    doctest.testmod ()
    sys.exit ()
    
def gen ( path, gen_path = u"gen" ):
    cache = "cache.manifest"
    cache_manifest = [ "CACHE MANIFEST", "", "CACHE:"]
    
    for _path, dirs, files in os.walk ( path ):
        _c_path = _path[len(path)+1:]
        _dirs = []
        _files = []
        
        _gen_path = _path.replace ( path, "" )[1:].decode("utf-8")
        
        _dirs += [ os.path.join ( _d ).decode("utf-8", "ignore") for _d in dirs ]
        _files += [ _f.decode("utf-8", "ignore") for _f in files ]
 
        cache_manifest += [ os.path.join ( _d, "index.html" ).decode("utf-8", "ignore") for _d in dirs ]
        cache_manifest += [ os.path.join ( _gen_path, _f ).decode("utf-8", "ignore") + ".html" for _f in files ]
        
        out = os.path.join ( gen_path, _gen_path )
        out_index = os.path.join ( out, "index.html" )

        root = _path.decode("utf-8").replace ( path, "" ).count(os.sep) * "../"
        index_file = _gen ( path,
            {
                "dirs" : _dirs,
                "files" : _files,
                "root" : root,
                "title" : _gen_path,
                "path" : _gen_path,
                "_c_path" : _c_path,
            }
        )
        
        try:
            os.makedirs ( os.path.dirname ( out_index ) )
        except OSError:
            pass
            
        out_fd = open ( out_index, "w+" )
        out_fd.write ( index_file.encode ( "utf-8") )
        out_fd.close ()
        
        for _f in _files:
            print os.path.join ( _c_path, _f )
            fd = open ( os.path.join ( path, _c_path, _f ), "rb" )
            content = fd.read ()
            content = content.decode("utf-8", "ignore")
            if "\0" in content:
                fd.close ()
                continue
            fd.close ()

            source_content = _gen_file ( path,
                {
                    "content" : content,
                    "root" : root,
                }
            )
            
            p = os.path.join ( os.path.dirname ( path ), gen_path, _c_path, _f + ".html" )
            # print p
            print p
            source_fd = open ( p, "w+" )
            source_fd.write ( source_content.encode("utf-8") )
            source_fd.close ()
            
    mf = open ( os.path.join ( gen_path, cache, ), "w" )
    mf.write ( "\n".join ( cache_manifest ) )
    mf.close ()

def main ():
    gen ( os.path.abspath ( "./flask" ) )
    
if __name__ == "__main__":
    main ()
"""