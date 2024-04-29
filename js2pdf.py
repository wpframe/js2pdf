import argparse
from PyPDF2 import PdfWriter, PdfReader

parser = argparse.ArgumentParser()
parser.add_argument('pdf', help='path to the input PDF file.')
parser.add_argument('javascript', help='path to the input JavaScript file.')
parser.add_argument('-o', '--output', help='specify an output PDF filename. by default, the new PDF is named using the old filename prefixed with "new_".')
parser.add_argument('-w', '--overwrite', action='store_true', help='overwrite the input PDF. This option ignores the -o/--output option.')
args = parser.parse_args()
if args.overwrite and args.output: parser.error("the -w/--overwrite option is incompatible with the -o/--output option.")

reader = PdfReader(open(args.pdf, 'rb'))
script = open(args.javascript, 'r').read()
if args.overwrite: filename = args.pdf
elif args.output: filename = args.output
else: filename = "new_" + args.pdf

output = PdfWriter()
output.append_pages_from_reader(reader)
output.add_js(script)
output.write(open(filename, 'wb'))
print(f"Successfully injected {args.javascript} into {args.pdf}. Output file: {filename}")