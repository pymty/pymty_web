import cherrypy as cp


class Main(object):
    def __init__(self):
        self.trabajos = JobBoard()

    @cp.expose
    @cp.tools.mako(fname="index.mako")
    def index(self):
        return {}

    @cp.expose
    @cp.tools.mako(fname="reuniones.mako")
    def reuniones(self):
        return {}

    @cp.expose
    @cp.tools.mako(fname="comunidades.mako")
    def comunidades(self):
        return {}


    @cp.expose
    @cp.tools.mako(fname="contribuir.mako")
    def contribuir(self):
        return {}

    @cp.expose
    @cp.tools.mako(fname="documentacion.mako")
    def documentacion(self):
        return {}


class JobBoard(object):

    @cp.expose
    @cp.tools.mako(fname="trabajos.mako")
    def index(self):
        return {}
