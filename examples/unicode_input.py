import pystache

class UnicodeInput(pystache.View):
    template_path = 'examples'
    template_encoding = 'utf8'

    def age(self, text):
        return 156
