from django.urls import path

from . import views

urlpatterns = [
    path('save/<slug:test_id>/<slug:result_key>/<slug:result_value>/', views.save, name='saveresult_save'),
    path('', views.index, name='index'),
]