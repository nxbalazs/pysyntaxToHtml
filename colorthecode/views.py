from django.shortcuts import render
from .pysyntax import pysyntax

# Create your views here.
def colorthecode_view(request):
    colored_text = ""
    if request.method == "POST":
        text = request.POST.get('text')
        c = pysyntax.Coloring(text)
        c.color_bg("#333333")
        c.color_tc("#ffffff")
        colored_text = c.colored()
    return render(request, 'index.html', {'colored': colored_text})