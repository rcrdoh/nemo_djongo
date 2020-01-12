from django.urls import path
from . import views


urlpatterns = [
	path('get/',views.get_data_http,name='get_data_http'),
	path('',views.home_view,name='home')
]
