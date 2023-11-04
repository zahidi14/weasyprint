from weasyprint import HTML
from weasyprint.css import CSS
#HTML
html = HTML(string=open('invoice.html').read(), )



# CSS
css = CSS(string=open('invoice.css').read())
pdf_bytes = html.write_pdf(stylesheets=[css])

with open('invoice.pdf', 'wb') as f:
    f.write(pdf_bytes)