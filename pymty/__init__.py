import os

import cherrypy as cp

from pymty.views.main import Main
from pymty.views.api import API


local_dir = os.path.join(os.getcwd(), os.path.dirname(__file__))


def mount_app():
    main = cp.Application(Main(), config={
        '/': {
            'tools.mako.directories': os.path.join(local_dir, 'templates')
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': os.path.join(local_dir, 'static')
        }
    })
    api = cp.Application(API(), '/api', config={
        '/': {
            'tools.json_out.on': True,
            'tools.json_in.on': True,
            'request.dispatch': cp.dispatch.MethodDispatcher()
        }
    })
    cp.tree.mount(main)
    cp.tree.mount(api)


def run():
    mount_app()
    cp.engine.start()
    cp.engine.block()
