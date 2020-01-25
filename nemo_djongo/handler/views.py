from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
#from handler.models import Nodos
from . import models
import json


#El comando curl para hacer el post desde terminal es:
#curl -i -X POST 'Content-Type: application/json' -d '{"name":"Pabloski", "action":"testeando","message":"gaaa"}' http://127.0.0.1:8000/handler/receiver/


# Create your views here.


def home_view(request,*args,**kwargs):
    return render(request, "home.html",{})

#def display_data_view(request, *args, **kwargs):
#    return render(request, "display-data.html",{})

# La funcion get_data_http detectara si el request es un POST. Si lo es, 
# hara un decode del request(pq viene en bytes) para luego parsear todas las palabras que esten entre
# comillas. Asignara cada palabra segun su id o llave detectando quien va primero (y asumiendo que las llaves
# siempre van primero). Luego, asignara estas llaves a un contexto para que sea imprimido en el html.

@require_http_methods(['POST'])
@csrf_exempt## this allows to avoid csrf protection , in future we have to improve the security limiting the ip from it will receive data
def receiver(request,*args,**kwargs):
    #context = {}
    #Lo debe coger en una especie de formulario
    #if request.method == 'POST': #Si el metodo es POST
    #string_data = request.body.decode('utf-8')
    json_data = json.loads(json.loads(request.body))
    print(request.body)
    print(type(json_data))
    print(json_data)
    # Ahora lo tendría que meter a la base de datos.
    models.Prueba_post.objects.create(
        name = json_data['name'],
        action = json_data['action'],
        message = json_data['message']
    )


    return HttpResponse(json_data)

@require_http_methods(['GET'])
def viewer(request,*args,**kwargs):

	context=models.Prueba_post.objects.values('name','action','message')

	#posible bug cuando no haya datos en la base de datos 
	#verificar que arroja el query superior cuando no hayan datos

	if context is None:
		context = {"name":"Aun no hay data",
		"action":"Aun no hay data",
		"message":"aun no hay data"}

	#return HttpResponse(context)
	return render(request,'viewer.html',{'context':context})