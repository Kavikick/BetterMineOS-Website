import cherrypy
import os, os.path

class BetterMineOSServer:
    @cherrypy.expose
    def index(self):
        return open('index.html')

if __name__ == '__main__':
    conf = {
        '/': {
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': '/home/wesley/Coding/BetterMineOS-Website/static'
        }
    }
    cherrypy.quickstart(BetterMineOSServer(), '/', conf)
