import pystache

class TemplatePartial(pystache.View):
    template_path = 'examples'

    def title(self, text):
        return "Welcome"

    def title_bars(self, text):
        return '-' * len(self.title('derp'))

    def looping(self, text):
        return [{'item': 'one'}, {'item': 'two'}, {'item': 'three'}]
        
    def thing(self, text):
        return self['prop']