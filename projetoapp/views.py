from django.shortcuts import render
from .models import Cliente
from projetoapp.forms import ClienteForm

# Create your views here.
def hello_home(request):
    return render(request, 'index.html')


def form_modelform(request):
    if request.method == "GET":
        form = ClienteForm()
        context = {
            'form': form
        }
        return render(request, "formulario_modelform.html", context=context)
    
    else:
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            form = ClienteForm()

        
        context = {
            'form': form
        }

        return render(request, "formulario_modelform.html", context=context)

