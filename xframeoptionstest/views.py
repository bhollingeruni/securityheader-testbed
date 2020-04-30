from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from saveresult.utils import save
from testsuite.settings import CURRENT_ORIGIN

def index(request):
    response = HttpResponse('X-Frame-Options test index')
    return response



#-----------------------------------------------------------------------------------------------------------------------
# Test value: none
#-----------------------------------------------------------------------------------------------------------------------

def none_setup(request, test_id):
    response = HttpResponse('Loaded successfully')
    save(test_id, "xframeoptions_none", "test_setup")
    return response



#-----------------------------------------------------------------------------------------------------------------------
# Test value: deny
#-----------------------------------------------------------------------------------------------------------------------

def deny_setup(request, test_id):
    response = HttpResponse('Loaded successfully')
    response['X-Frame-Options'] = 'deny'
    save(test_id, "xframeoptions_deny", "test_setup")
    return response



#-----------------------------------------------------------------------------------------------------------------------
# Test value: sameorigin
#-----------------------------------------------------------------------------------------------------------------------

def sameorigin_setup(request, test_id):
    response = HttpResponse('Loaded successfully')
    response['X-Frame-Options'] = 'sameorigin'
    save(test_id, "xframeoptions_sameorigin", "test_setup")

    return response



#-----------------------------------------------------------------------------------------------------------------------
# Test value: allow-from
#-----------------------------------------------------------------------------------------------------------------------

def allowfrom_valid_setup(request, test_id):
    response = HttpResponse('Loaded successfully')
    response['X-Frame-Options'] = 'allow-from ' + CURRENT_ORIGIN
    save(test_id, "xframeoptions_allowfrom_valid", "test_setup")
    return response

def allowfrom_invalid_setup(request, test_id):
    response = HttpResponse('Loaded successfully')
    response['X-Frame-Options'] = 'allow-from http://invalid.test/'
    save(test_id, "xframeoptions_allowfrom_invalid", "test_setup")
    return response

