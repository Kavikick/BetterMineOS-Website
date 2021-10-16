import cherrypy
import os
import os.path


class Root(object):
    @cherrypy.expose
    def index(self):
        return open('index.html')


def error_page_default(status, message, traceback, version):
    return """<div style="text-align:center;">Bad Kitty</div>"""  # """<div style="text-align:center;" ><img src="/files/suspicious.jpeg"><div>"""


if __name__ == '__main__':
    folderRoot = os.path.abspath(os.getcwd())
    conf = {
        'global': {
            'server.socket_port': 25545,
            'server.socket_host': '192.168.32.5',
            'error_page.default': error_page_default,
            'log.access_file': './logs/normal.log',
        },
        '/': {
            'tools.staticdir.root': folderRoot
        },
        '/favicon.ico':
        {
            'tools.staticfile.on': True,
            'tools.staticfile.filename': folderRoot+'/favicon.ico'
        },
        '/files': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        },
        '/styling': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './styling'
        }
    }
    cherrypy.quickstart(Root(), '/', conf)
