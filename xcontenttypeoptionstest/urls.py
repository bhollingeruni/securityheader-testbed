from django.urls import path

from . import views

urlpatterns = [
    path('none_setup/<slug:test_id>/', views.none_setup, name='xframeoptions_none_setup'),
    path('nosniff_setup/<slug:test_id>/', views.nosniff_setup, name='xframeoptions_nosniff_setup'),
    path('', views.index, name='index'),
]