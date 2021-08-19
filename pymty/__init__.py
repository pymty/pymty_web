import os
import sys

import cherrypy as cp

from pymty.views.main import Main
from pymty.views.api import API


local_dir = os.path.join(os.getcwd(), os.path.dirname(__file__))


def _direct_static_file(fname):
    return {
        f'/{fname}': {
            'tools.staticfile.on': True,
            'tools.staticfile.filename': os.path.join(local_dir, 'static', fname)
        }
    }

def mount_app():
    main = cp.Application(Main(), config={
        '/': {
            'tools.mako.directories': os.path.join(local_dir, 'templates')
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': os.path.join(local_dir, 'static')
        },
        **_direct_static_file('favicon.ico'),
        **_direct_static_file('robots.txt'),
        **_direct_static_file('humans.txt')
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
    extra_config = sys.argv[1] if len(sys.argv) > 1 else None
    cp.config.update(cp.lib.reprconf.Config(extra_config))
    cp.engine.start()
    cp.engine.block()
