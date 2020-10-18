# -*- coding: utf-8 -*-
import codecs
import io
import os
import sys
import unittest

import pytest

import asynctest
import pdfmate

import pytest_asyncio.plugin
from pdfmate.errors import InvalidSourceError

TEST_PATH = os.path.dirname(os.path.realpath(__file__))

PYPPETEER_EXTRA_SETTINGS = {
    'browserArgs': [' --webkit-print-color-adjust'],
    'pageOptions': {'waitUntil': 'networkidle2'},
}

PYPPETEER_EMULATE_MEDIA_SETTINGS = {
    'emulateMedia': 'screen',
}


class TestPdfPyppeteerSettings(asynctest.TestCase):
    """Test pyppeteer settings"""

    @pytest.mark.asyncio
    async def test_pdf_page_emulate_media_setting(self):
        config = pdfmate.configuration(pyppeteer=PYPPETEER_EMULATE_MEDIA_SETTINGS)
        pdf = await pdfmate.from_url(
            'http://networkcheck.kde.org', 'out.pdf', options={'printBackground': True}
        )

        self.assertEqual(config.pyppeteer['emulateMedia'], 'screen')


if __name__ == "__main__":
    asynctest.main()
