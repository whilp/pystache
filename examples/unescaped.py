import pystache

class Unescaped(pystache.View):
    template_path = 'examples'

    def title(self, text):
        return "Bear > Shark"
