from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
#from handler.models import Nodos
from . import models
import json
import socketio

#socketio necesita la libreria requests de python
sio = socketio.Client()
sio.connect('http://localhost:3000')


@sio.on("post_received")
def message_handler(msg):
    print('inside post_receiver')
    print(msg)
    #msg tipo dict

#El comando curl para hacer el post desde terminal es:
#curl -i -X POST 'Content-Type: application/json' -d '{"name":"Pabloski", "action":"testeando","message":"gaaa"}' http://127.0.0.1:8000/handler/receiver/

def home_view(request,*args,**kwargs):
    return render(request, "home.html",{})

# La funcion get_data_http detectara si el request es un POST. Si lo es, 
# hara un decode del request(pq viene en bytes) para luego parsear todas las palabras que esten entre
# comillas. Asignara cada palabra segun su id o llave detectando quien va primero (y asumiendo que las llaves
# siempre van primero). Luego, asignara estas llaves a un contexto para que sea imprimido en el html.

# this allows to avoid csrf protection in that URL, in future a restriction ip condition will be added

"""
@require_http_methods(['POST'])
@csrf_exempt
def receiver(request,*args,**kwargs):

    #string_data = request.body.decode('utf-8')
    json_data = json.loads(json.loads(request.body))
    print(request.body)
    print(type(json_data))
    print(json_data)
    
    #Ahora lo tendría que añadir a la base de datos.

    models.Prueba_post.objects.create(
        name = json_data['name'],
        action = json_data['action'],
        message = json_data['message']
    )

    return HttpResponse(json_data)
"""

@require_http_methods(['GET'])
def viewer(request,*args,**kwargs):

	context=models.Prueba_post.objects.values('name','action','message')

	#posible bug cuando no haya datos en la base de datos 
	#verificar que arroja el query superior cuando no hayan datos

	if context is None:
		context = {"name":"Aun no hay data",
		"action":"Aun no hay data",
		"message":"aun no hay data"}

	return render(request,'viewer.html',{'context':context})