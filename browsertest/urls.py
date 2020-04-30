from django.urls import path

from . import views

urlpatterns = [
    path('test/<slug:test_id>/<slug:test_type>/', views.test, name='browsertest.test'),
    path('', views.index, name='index'),
]