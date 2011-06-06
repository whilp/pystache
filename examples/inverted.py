import pystache

class Inverted(pystache.View):
    template_path = 'examples'

    def t(self, text):
        return True

    def f(self, text):
        return False

    def two(self, text):
        return 'two'

    def empty_list(self, text):
        return []
        
    def populated_list(self, text):
        return ['some_value']