from django.urls import path

from . import views

urlpatterns = [
    path('none_setup/<slug:test_id>/', views.none_setup, name='xframeoptions_none_setup'),
    path('deny_setup/<slug:test_id>/', views.deny_setup, name='xframeoptions_deny_setup'),
    path('sameorigin_setup/<slug:test_id>/', views.sameorigin_setup, name='xframeoptions_sameorigin_setup'),
    path('allowfrom_valid_setup/<slug:test_id>/', views.allowfrom_valid_setup, name='xframeoptions_allowfrom_valid_setup'),
    path('allowfrom_invalid_setup/<slug:test_id>/', views.allowfrom_invalid_setup, name='xframeoptions_allowfrom_invalid_setup'),
    path('', views.index, name='index'),
]