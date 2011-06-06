import pystache

class ComplexView(pystache.View):
    template_path = 'examples'

    def header(self, text):
        return "Colors"

    def item(self, text):
        items = []
        items.append({ 'name': 'red', 'current': True, 'url': '#Red' })
        items.append({ 'name': 'green', 'link': True, 'url': '#Green' })
        items.append({ 'name': 'blue', 'link': True, 'url': '#Blue' })
        return items

    def list(self, text):
        return not self.empty('')

    def empty(self, text):
        return len(self.item('')) == 0
        
    def empty_list(self, text):
        return [];
