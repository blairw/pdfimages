# pdfimages

This is a Python script that can take a regular old PDF file (text is selectable) and convert it into a PDF file consisting of the pages of the original PDF file, converted to images. Basically, this prevents the text from being selectable.

It's basically a thin wrapper around [pdf2image](https://pypi.org/project/pdf2image/) and PIL (Python Imaging Library).

## How to get this working

1. Install Poppler for your operating system (see: https://pypi.org/project/pdf2image/)
2. Put your PDf files in the `01-input` folder
3. Install the Python dependencies listed at the top of `run.py`
4. Run `run.py`
5. Enjoy your new PDF files, which have been placed in the `02-output` folder :)
