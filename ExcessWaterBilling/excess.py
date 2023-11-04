from weasyprint import HTML
from weasyprint.css import CSS
html = HTML(string=open('excess.html').read())
css = CSS(string=open('excess.css').read())
pdf_bytes = html.write_pdf(stylesheets=[css])

with open('output.pdf', 'wb') as f:
    f.write(pdf_bytes)