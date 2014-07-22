import cherrypy

from mako import exceptions
from mako.lookup import TemplateLookup

from pymty.utils import in_development

def setup():
    cherrypy.tools.mako = cherrypy.Tool('on_start_resource', MakoLoader())


class MakoHandler(cherrypy.dispatch.LateParamPageHandler):
    """Callable which sets response.body."""

    def __init__(self, template, next_handler):
        self.template = template
        self.next_handler = next_handler

    def __call__(self):
        env = self.next_handler()
        if in_development():
            output = self._debug_render(env)
        else:
            output = self.template.render(**env)
        return output

    def _debug_render(self, env):
        try:
            return self.template.render(**env)
        except Exception:
            return exceptions.html_error_template().render()


class MakoLoader(object):

    def __init__(self):
        self.lookups = {}

    def __call__(self, fname, directories, module_directory=None,
                 collection_size=-1):
        # Find the appropriate template lookup.
        key = (tuple(directories), module_directory)
        try:
            lookup = self.lookups[key]
        except KeyError:
            lookup = TemplateLookup(directories=directories,
                                    module_directory=module_directory,
                                    collection_size=collection_size,
                                    input_encoding='utf-8',
                                    output_encoding='utf-8')
            self.lookups[key] = lookup
        cherrypy.request.lookup = lookup
        # Replace the current handler.
        cherrypy.request.template = t = lookup.get_template(fname)
        cherrypy.request.handler = MakoHandler(t, cherrypy.request.handler)
