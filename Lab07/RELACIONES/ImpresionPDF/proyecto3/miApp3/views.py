from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

def generar_pdf(request):
    # Obtener la plantilla HTML
    template = get_template('base.html')
    context = {'data': 'Datos de ejemplo'}  # Puedes pasar datos a la plantilla si es necesario

    # Renderizar la plantilla con los datos
    rendered_template = template.render(context)

    # Generar el PDF utilizando xhtml2pdf
    pdf = pisa.CreatePDF(rendered_template)

    # Verificar si se generó correctamente el PDF
    if not pdf.err:
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="archivo.pdf"'
        response.write(pdf.dest.getvalue())
        pdf.dest.close()
        return response

    return HttpResponse('Error al generar el PDF', status=500)
