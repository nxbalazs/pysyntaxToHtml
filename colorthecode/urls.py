from django.urls import path
from . import views

app_name = 'colorthecode'


urlpatterns = [
    path('', views.colorthecode_view, name='index'),
]