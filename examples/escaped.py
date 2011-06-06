import pystache

class Escaped(pystache.View):
    template_path = 'examples'

    def title(self, test):
        return "Bear > Shark"
