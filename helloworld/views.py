from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def hello(request):
    return render(request, 'hello.html', {"name":"Juan Manuel Antúnez"})
    #return HttpResponse("Hello World!")