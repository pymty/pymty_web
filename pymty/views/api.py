import cherrypy as cp


class API:
    exposed = True

    def GET(self):
        cp.log.error("Example")
        return {'rsp': "Hola desde el API!"}
