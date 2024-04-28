## js2pdf

Really simple Python script for injecting JS into a PDF.

```
usage: script.py path/to/pdf.pdf path/to/javascript.js
options:
  -o    to specify a different output file (example: -o path/to/output.pdf)
  -O    to overwrite the input PDF (by default, the new PDF is named using the old filename prefixed with "new_")
```

Requires PyPDF2:
``pip install pypdf2``