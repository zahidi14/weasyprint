from weasyprint import HTML
from weasyprint.css import CSS
#HTML
html = HTML(string=open('account.html').read())



# CSS
css = CSS(string=open('account.css').read())
pdf_bytes = html.write_pdf(stylesheets=[css])

with open('output.pdf', 'wb') as f:
    f.write(pdf_bytes)