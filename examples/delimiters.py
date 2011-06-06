import pystache

class Delimiters(pystache.View):
    template_path = 'examples'

    def first(self, text):
        return "It worked the first time."

    def second(self, text):
        return "And it worked the second time."

    def third(self, text):
        return "Then, surprisingly, it worked the third time."
