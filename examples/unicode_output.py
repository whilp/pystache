# encoding: utf-8

import pystache

class UnicodeOutput(pystache.View):
    template_path = 'examples'

    def name(self, text):
        return u'Henri Poincaré'
