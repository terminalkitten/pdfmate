[![PyPI](https://img.shields.io/pypi/v/pdfmate)](https://pypi.python.org/pypi/pdfmate)
[![PyPI version](https://img.shields.io/pypi/pyversions/pdfmate)](https://pypi.python.org/pypi/pdfmate)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# PDFMate

Async / sync wrapper for Pyppeteer

### Install

    pip install pdfmate

# Usage

For simple async tasks:

```python
import pdfgen

async def f():
    await pdfgen.from_url('http://google.com', 'out.pdf')
    await pdfgen.from_file('test.html', 'out.pdf')
    await pdfgen.from_string('Hello!', 'out.pdf')
```

Sync API is also provided at `pdfgen.sync` for all the above-mentioned functions:

```python
import pdfgen

pdfgen.sync.from_url('http://google.com', 'out.pdf')
pdfgen.sync.from_file('test.html', 'out.pdf')
pdfgen.sync.from_string('Hello!', 'out.pdf')
```

You can pass a list with multiple URLs or files:

```python
pdfgen.sync.from_url(['google.com', 'yandex.ru', 'engadget.com'], 'out.pdf')
pdfgen.sync.from_file(['file1.html', 'file2.html'], 'out.pdf')
```

Also you can pass an opened file:

```python
with open('file.html') as f:
    pdfgen.sync.pdfgen(f, 'out.pdf')
```

If you wish to further process generated PDF, you can read it to a
variable:

```python
# Ignore output_path parameter to save pdf to a variable
pdf = pdfgen.sync.from_url('http://google.com')
```

You can specify all [Pyppeteer
options](https://pyppeteer.github.io/pyppeteer/reference.html#pyppeteer.page.Page.pdf) used for saving PDF as shown below:

```python
options = {
    'scale': 2.0,
    'format': 'Letter',
    'margin': {
        'top': '0.75in',
        'right': '0.75in',
        'bottom': '0.75in',
        'left': '0.75in',
    },
    'pageRanges': '1-5,8',
}

pdfgen.sync.from_url('http://google.com', 'out.pdf', options=options)
```

You can also pass any options through meta tags in your HTML:

```python
body = """
    <html>
      <head>
        <meta name="pdfgen-format" content="Legal"/>
        <meta name="pdfgen-landscape" content="False"/>
      </head>
      Hello World!
      </html>
    """

pdfgen.sync.from_string(body, 'out.pdf')
```

## Configuration

Each API call takes an optional options parameter to configure print PDF behavior. However, to reduce redundancy, one can certainly set default configuration to be used for all API calls. It takes the
configuration options as initial paramaters. The available options are:

- `options` - the dict used by default for pyppeteer `page.pdf(options)` call. `options` passed as argument to API call will take precedence over the default options.
- `meta_tag_prefix` - the prefix for `pdfgen` specific meta tags - by
  default this is `pdfgen-`.
- `environ` - the dict used to provide env variables to pyppeteer headless browser.

```python
import pdfgen

pdfgen.configuration(options={'format': 'A4'})

async def f():
    # The resultant PDF at 'output_file' will be in A4 size and 2.0 scale.
    await pdfgen.from_string(html_string, output_file, options={'scale': 2.0})
```

### Setup for development

    poetry install -v --no-root

### Run tests

    poetry run pytest tests/

### Enable git-hooks with lint-staged

    npx mrm lint-staged
    npx husky install

#### Credits

This is adapted version of PDFGen-Python and python-PDFKit library, so big thanks to them!

- [PDFGen-Python](https://pypi.org/project/pdfgen/)
- [python-pdfkit](https://github.com/JazzCore/python-pdfkit/)
- [Pyppeteer](https://pypi.org/project/pyppeteer/)

### Other projects

- [django-pdf-reactor](https://github.com/terminalkitten/django-pdf-reactor/)

### Is it any good?

[Yes.](http://news.ycombinator.com/item?id=3067434)
