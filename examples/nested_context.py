import pystache

class NestedContext(pystache.View):
    template_path = 'examples'

    def outer_thing(self):
        return "two"

    def foo(self, text):
        return {'thing1': 'one', 'thing2': 'foo'}

    def derp(self, text):
        return [{'inner': 'car'}]
        
    def herp(self, text):
        return [{'outer': 'car'}]
        
    def nested_context_in_view(self, text):
        return 'it works!' if self.get('outer') == self.get('inner') else ''