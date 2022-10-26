from django.shortcuts import render

def clases(request):
    return render(request, 'ritmos/clases.html', context={})