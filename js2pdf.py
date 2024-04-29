import sys
from PyPDF2 import PdfWriter, PdfReader

if len(sys.argv) not in [3, 4, 5] or (len(sys.argv) == 4 and sys.argv[3] != "-O") or (len(sys.argv) == 5 and sys.argv[3] != "-o"):
	print("usage: script.py path/to/pdf.pdf path/to/javascript.js")
	print("options:")
	print("  -o	to specify a different output file (example: -o path/to/output.pdf)")
	print("  -O	to overwrite the input PDF (by default, the new PDF is named using the old filename prefixed with \"new_\")")
	exit()

reader = PdfReader(open(sys.argv[1], 'rb'))
script = open(sys.argv[2], 'r').read()
if len(sys.argv) == 3: filename = "new_" + sys.argv[1]	# Default filename is just the input filename with new_ prepended
elif len(sys.argv) == 4: filename = sys.argv[1] 		# If the -O flag has been used, our output filename is the input filename
elif len(sys.argv) == 5: filename = sys.argv[4] 		# If the -o flag has been used, our output filename is the provided filename

output = PdfWriter()
output.append_pages_from_reader(reader)
output.add_js(script)
output.write(open(filename, 'wb'))
print(f"Successfully injected {sys.argv[2]} into {sys.argv[1]}. Output file: {filename}")