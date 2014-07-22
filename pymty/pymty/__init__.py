import os

import cherrypy as cp

from pymty.views.main import Main
from pymty.views.api import API


local_dir = os.path.join(os.getcwd(), os.path.dirname(__file__))

def _set_environ_for_app_engine():
    config = {
        'environment': 'embedded',
        'tools.mako.directories': os.path.join(local_dir, 'templates')
    }
    cp.config.update(config)
    cp.log.access_log.propagate = False


def get_app():
    _set_environ_for_app_engine()
    main = cp.Application(Main())
    api = cp.Application(API(), '/api')
    api_config = {'/': {
        'tools.json_out.on': True,
        'tools.json_in.on': True,
        'request.dispatch': cp.dispatch.MethodDispatcher()
        }
    }
    cp.tree.mount(main, '')
    cp.tree.mount(api, config=api_config)
    return cp.tree

app = get_app()
