# -*- coding: utf-8 -*-
import re
import os
import locale

class Lang(object):
    def __init__(self, en='', ja=''):
        self.jp = ja
        self.en = en
    def output(self):
        lang = 'en'
        env = re.sub('_.+', '', os.environ.get('MAYA_UI_LANGUAGE', ''))
        loc = re.sub('_.+', '', locale.getdefaultlocale()[0])
        if loc != '':
            lang = loc
        if env != '':
            lang = env
        if lang == 'ja':
            return self.jp
        if lang == 'en':
            return self.en