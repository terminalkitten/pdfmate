# -*- coding: utf-8 -*-
import os

import asynctest
import pytest

import pdfmate

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

    def setUp(self):
        pass

    def tearDown(self):
        if os.path.exists('out.pdf'):
            os.remove('out.pdf')

    @pytest.mark.asyncio
    async def test_pdf_page_emulate_media_setting(self):
        config = pdfmate.configuration(pyppeteer=PYPPETEER_EMULATE_MEDIA_SETTINGS)
        pdf = await pdfmate.from_url(
            'http://networkcheck.kde.org', 'out.pdf', options={'printBackground': True}
        )

        self.assertEqual(pdf, 'out.pdf')
        self.assertEqual(config.pyppeteer['emulateMedia'], 'screen')


if __name__ == "__main__":
    asynctest.main()
