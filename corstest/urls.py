from django.urls import path

from . import views

urlpatterns = [
    path('simple_setup/<slug:test_id>/', views.simple_setup, name='corstest.simple_setup'),
    path('complex_setup/<slug:test_id>/', views.complex_setup, name='corstest.complex_setup'),
    path('resource/<slug:test_id>/<slug:mode>/<slug:value>/', views.resource, name='corstest.resource'),
    path('', views.index, name='index'),
]