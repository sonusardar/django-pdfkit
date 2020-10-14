from django.shortcuts import render, HttpResponse



from django.template.loader import get_template

from . models import online_course
import pdfkit
from django.http import HttpResponse
from django.template import loader


def home(request):

   return render(request,'index.html')
   # return HttpResponse('index page bro')

def render_pdf_view(request):
   data_pdf =   online_course.objects.all()

   options = {
    'page-size': 'A4',
   #  'margin-top': '0.75in',
   #  'margin-right': '0.75in',
   #  'margin-bottom': '0.75in',
   #  'margin-left': '0.75in',
   }


   
   context = {'datass': data_pdf}    

   html = loader.render_to_string('index.html', context)
   output= pdfkit.from_string(html, output_path=False,options=options)
   response = HttpResponse(content_type="application/pdf")
   response.write(output)
   return response