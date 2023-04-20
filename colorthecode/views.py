from django.shortcuts import render
from .pysyntax import pysyntax

# Create your views here.
def colorthecode_view(request):
    colored = str("")
    if request.method == "POST":
        text = request.POST.get('text')
        colored = pysyntax.Coloring(text).colored
    return render(request, 'index.html', {'colored': colored})