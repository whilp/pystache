import pystache

class DoubleSection(pystache.View):
    template_path = 'examples'

    def t(self, text):
        return text

    def two(self, text):
        return "second"
