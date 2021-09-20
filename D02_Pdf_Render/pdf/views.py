from django.shortcuts import render

# pdf 
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas 
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter


import os 
from django.conf import settings

# Create your views here.

def get_pdf_name(request):
    pdf_dir = os.listdir(os.path.join(settings.MEDIA_ROOT, 'sample_pdf'))
    pdf_dir_path = list(map( lambda x : '/{}/{}/{}'.format('media', 'sample_pdf', x), pdf_dir))
    res = []
    for ind, item in enumerate(pdf_dir):
        res.append("<a href='{}' target='_blank' >{}</a>".format(pdf_dir_path[ind], item))

        
    content = {'list' : res}
    return render(request, 'index.html', content)


def get_pdf(request):
    # ccreaate Bytestream Buffer 
    buf = io.BytesIO()
    # create a canvas
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    # Create a text Object 
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)

    # add Some lines of text
    lines = [
        "This is line one",
        "This is line two",
        "This is line three",
    ]

    for line in lines:
        textob.textLine(line)
    
    #Finsh up
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)
    response = FileResponse(buf, as_attachment=True, filename='file.pdf')
    response.headers['Content-Type'] = 'application/pdf'
    return response
 
    contnet = {}
    return render(request, 'index.html', content)