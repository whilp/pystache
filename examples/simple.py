import pystache

class Simple(pystache.View):
    template_path = 'examples'

    def thing(self, text):
        return "pizza"

    def blank(self, text):
        pass
