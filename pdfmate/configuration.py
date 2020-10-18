# -*- coding: utf-8 -*-
import os
from collections import OrderedDict


class Configuration(object):
    def __init__(self, options={}, pyppeteer={}, meta_tag_prefix='pdfgen-', environ=''):
        self.update(options, pyppeteer, meta_tag_prefix, environ)

    def update(self, options=None, pyppeteer={}, meta_tag_prefix=None, environ=None):
        if meta_tag_prefix is not None:
            self.meta_tag_prefix = meta_tag_prefix

        if environ is not None:
            self.environ = environ
            if not self.environ:
                self.environ = os.environ
            for key in self.environ.keys():
                if not isinstance(self.environ[key], str):
                    self.environ[key] = str(self.environ[key])

        if options is not None:
            self.options = OrderedDict(options)

        # Always pass on empty dict
        self.pyppeteer = OrderedDict(pyppeteer)
        self.page_options = self.pyppeteer.get('pageOptions', None)
        self.browser_args = self.pyppeteer.get('browserArgs', [])

        return self


DEFAULT_CONFIG = Configuration()


def configuration(**kwargs):
    """
    Constructs and returns a :class:`Configuration` with given options

    :param options: Pyppeteer .pdf options
    :param meta_tag_prefix: the prefix for ``pdfgen`` specific meta tags
    """
    return DEFAULT_CONFIG.update(**kwargs)
