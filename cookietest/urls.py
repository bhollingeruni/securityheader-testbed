from django.urls import path

from . import views

urlpatterns = [
    path('header_setup/<slug:test_id>/', views.header_setup, name='cookie_header_setup'),
    path('header_check/<slug:test_id>/', views.header_check, name='cookie_header_check'),
    path('httponly_setup/<slug:test_id>/', views.httponly_setup, name='cookie_httponly_setup'),
    path('httponly_check/<slug:test_id>/', views.httponly_check, name='cookie_httponly_check'),
    path('expires_setup/<slug:test_id>/', views.expires_setup, name='cookie_expires_setup'),
    path('expires_check/<slug:test_id>/', views.expires_check, name='cookie_expires_check'),
    path('maxage_setup/<slug:test_id>/', views.maxage_setup, name='cookie_maxage_setup'),
    path('maxage_check/<slug:test_id>/', views.maxage_check, name='cookie_maxage_check'),
    path('subdomain_setup/<slug:test_id>/', views.subdomain_setup, name='cookie_subdomain_setup'),
    path('subdomain_check/<slug:test_id>/', views.subdomain_check, name='cookie_subdomain_check'),
    path('path_setup/<slug:test_id>/', views.path_setup, name='cookie_path_setup'),
    path('path_check/<slug:test_id>/', views.path_check, name='cookie_path_check'),
    path('domain_setup/<slug:test_id>/', views.domain_setup, name='cookie_domain_setup'),
    path('domain_check/<slug:test_id>/', views.domain_check, name='cookie_domain_check'),
    path('domainreverse_setup/<slug:test_id>/', views.domainreverse_setup, name='cookie_domainreverse_setup'),
    path('domainreverse_check/<slug:test_id>/', views.domainreverse_check, name='cookie_domainreverse_check'),
    path('secure_setup/<slug:test_id>/', views.secure_setup, name='cookie_secure_setup'),
    path('secure_check/<slug:test_id>/', views.secure_check, name='cookie_secure_check'),
    path('securehttps_setup/<slug:test_id>/', views.securehttps_setup, name='cookie_securehttps_setup'),
    path('securehttps_check/<slug:test_id>/', views.securehttps_check, name='cookie_securehttps_check'),
    path('samesite_setup/<slug:test_id>/', views.samesite_setup, name='cookie_samesite_setup'),
    path('samesite_check/<slug:test_id>/<slug:value>/', views.samesite_check, name='cookie_samesite_check'),
    path('', views.index, name='index'),
]