from django.urls import path
from . import views

app_name='handler'

urlpatterns = [
	path('',views.home_view,name='home'),
	path('viewer/',views.viewer,name='viewer'),
	path('receiver/',views.receiver, name = 'receiver'),
]
