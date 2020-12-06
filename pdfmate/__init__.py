# -*- coding: utf-8 -*-
"""
Pyppeteer-based async python wrapper to convert html to pdf
"""

__forked_from__ = 'Shivansh Saini'
__author__ = 'terminalkitten'
__version__ = '0.4.9'
__license__ = 'MIT'

import pdfmate.api_sync as sync  # noqa

from .api_async import from_file, from_sources, from_string, from_url  # noqa
from .configuration import configuration  # noqa
from .pdfmate import PDFMate  # noqa
from .source import Source  # noqa
