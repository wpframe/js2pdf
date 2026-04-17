## js2pdf

Really simple Python script for injecting JavaScript into a PDF. The JavaScript should run in most viewers/browsers when the PDF is opened.

#### Requires PyPDF2: ``pip install pypdf2``

```
usage: js2pdf.py path/to/pdf.pdf path/to/javascript.js

optional arguments:
  -o OUTPUT, --output OUTPUT      specify an output PDF filename. by default, the new PDF is named using the old filename prefixed with "new_".
  -w, --overwrite      overwrite the input PDF. this option ignores the -o/--output option.
```

### Example

```
[will@will]$ python3 js2pdf.py document.pdf payload.js -o poisoned_document.pdf
Successfully injected payload.js into document.pdf. Output file: poisoned_document.pdf
```

If the content of your JavaScript file is ``app.alert("Hello World!");`` then an alert showing "Hello World!" will appear when viewing the PDF (in this example, in Chrome).

![example image](alert.png)
