import cherrypy as cp


class Main(object):
    def __init__(self):
        self.trabajos = JobBoard()
        self.reuniones = Meetings()

    @cp.expose
    @cp.tools.mako(fname="index.mako")
    def index(self):
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

class Meetings(object):

    @cp.expose
    @cp.tools.mako(fname="reuniones.mako")
    def index(self):
        return {}

    @cp.expose(['circulo-virtuoso',])
    @cp.tools.mako(fname="reuniones_cv.mako")
    def circulo_virtuoso(self):
        return {}


class JobBoard(object):

    @cp.expose
    @cp.tools.mako(fname="trabajos.mako")
    def index(self):
        return {}
