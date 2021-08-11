from django.urls import path

from . import views

app_name = 'dictionary'

urlpatterns = [
    path('', views.base, name='base'),
    path('results/', views.results, name='results')
]
