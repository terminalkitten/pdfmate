# -*- coding: utf-8 -*-

from .pdfmate import PDFMate
from .source import Source
from .utils import is_iterable


async def from_url(url, output_path=None, options=None):
    """
    Convert file of files from URLs to PDF document

    :param url: URL or list of URLs to be saved
    :param output_path: (optional) path to output PDF file. If not provided,
        PDF will be returned as string
    :param options: (optional) dict to configure pyppeteer page.pdf action

    Returns: output_path if provided else PDF Binary
    """
    sources = (
        [Source(urli, 'url') for urli in url]
        if is_iterable(url)
        else Source(url, 'url')
    )
    r = PDFMate(sources, options=options)
    return await r.to_pdf(output_path)


async def from_file(input, output_path=None, options=None):
    """
    Convert HTML file or files to PDF document

    :param input: path to HTML file or list with paths or file-like object
    :param output_path: (optional) path to output PDF file. If not provided,
        PDF will be returned as string
    :param options: (optional) dict to configure pyppeteer page.pdf action

    Returns: output_path if provided else PDF Binary
    """
    sources = (
        [Source(file, 'file') for file in input]
        if is_iterable(input)
        else Source(input, 'file')
    )
    r = PDFMate(sources, options=options)
    return await r.to_pdf(output_path)


async def from_string(input, output_path=None, options=None):
    """
    Convert given string or strings to PDF document

    :param input: string with a desired text. Could be a raw text or a html file
    :param output_path: (optional) path to output PDF file. If not provided,
        PDF will be returned as string
    :param options: (optional) dict to configure pyppeteer page.pdf action

    Returns: output_path if provided else PDF Binary
    """

    sources = Source(input, 'string')
    r = PDFMate(sources, options=options)
    return await r.to_pdf(output_path)


async def from_sources(sources, output_path=None, options=None):
    """
    Convert given sources to PDF document

    :param sources: list of source objects
    :param output_path: (optional) path to output PDF file. If not provided,
        PDF will be returned as string
    :param options: (optional) dict to configure pyppeteer page.pdf action

    Returns: output_path if provided else PDF Binary
    """
    r = PDFMate(sources, options=options)
    return await r.to_pdf(output_path)
