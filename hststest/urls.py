from django.urls import path

from . import views

urlpatterns = [
    path('setup/<slug:test_id>/', views.setup, name='corstest.setup'),
    path('frame/<slug:test_id>/', views.frame, name='corstest.frame'),
    path('check_setup/<slug:test_id>/', views.check_setup, name='corstest.check_setup'),
    path('check_scheme/<slug:test_id>/', views.check_scheme, name='corstest.check_scheme'),
    path('check_scheme_subdomain/<slug:test_id>/', views.check_scheme_subdomain, name='corstest.check_scheme_subdomain'),
    path('', views.index, name='index'),
]