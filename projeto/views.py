from django.http import HttpResponse

def hello_teste(request):
    return HttpResponse("teste url ok!!!")