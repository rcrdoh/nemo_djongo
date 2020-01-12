from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
#from handler.models import Nodos

from . import models
import json
# Create your views here.


def home_view(request,*args,**kwargs):
    return render(request, "home.html",{})

def display_data_view(request, *args, **kwargs):
    return render(request, "display-data.html",{})

# La funcion get_data_http detectara si el reques es un POST. Si lo es, 
# hara un decode del request(pq viene en bytes) para luego parsear todas las palabras que esten entre
# comillas. Asignara cada palabra segun su id o llave detectando quien va primero (y asumiendo que las llaves
# siempre van primero). Luego, asignara estas llaves a un contexto para que sea imprimido en el html.


#El comando curl para hacer el post es:
#curl -i -X POST 'Content-Type: application/json' -d '{"name":"Pabloski", "action":"testeando","message":"gaaa"}' http://127.0.0.1:8000/get/

@csrf_exempt
def get_data_http(request,*args,**kwargs):
    context = {}
    #Lo debe coger en una especie de formulario
    if request.method == 'POST': #Si el metodo es POST
        string_data = request.body.decode('utf-8')
        json_data = json.loads(string_data)
        print(json_data)
        # Ahora lo tendría que meter a la base de datos.
        models.Prueba_post.objects.create(
            name = json_data['name'],
            action = json_data['action'],
            message = json_data['message']
        )
    elif request.method == 'GET':
        
        #for num,data_object in enumerate(models.Prueba_post.objects.all()):
        #print(models.Prueba_post._meta.get_fields())
        #for num in range(models.Prueba_post.objects.all().count()):
            #obj = data_object.objects.get(id=num+1)
        #    print(dir(data_object))
            #obj=data_object.value()
            #print(obj._meta.get_fields())
        #    context['object'+str(num)] = obj
            #print([a for a in dir(obj) if not a.startswith('__')])
            #print(obj.name)
        checking=models.Prueba_post.objects.values('name','action','message')
        #print(checking)
        return HttpResponse(checking)
        #print(num)
        #print(context)
    else: 
        context = {"name":"Aun no hay data",
        "action":"Aun no hay data",
        "message":"aun no hay data"}
        
    return render(request,"get-data.html",context)