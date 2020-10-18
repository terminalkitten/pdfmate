# -*- coding: utf-8 -*-
"""
Pyppeteer-based async python wrapper to convert html to pdf
"""

__forked_from__ = 'Shivansh Saini'
__author__ = 'terminalkitten'
__version__ = '0.0.1'
__license__ = 'MIT'

import pdfmate.api_sync as sync

from .api_async import from_file, from_sources, from_string, from_url
from .configuration import configuration
from .pdfmate import PDFMate
from .source import Source
