from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.staticfiles.templatetags.staticfiles import static
import logging
from testsuite.settings import CURRENT_ORIGIN
from saveresult.utils import save

def index(request):
    response = HttpResponse('X-Content-type-Options test index')
    return response



#-----------------------------------------------------------------------------------------------------------------------
# Test value: header not set
#-----------------------------------------------------------------------------------------------------------------------

def none_setup(request, test_id):
    # return JS code to execute
    response = HttpResponse('save_result("{test_id}", "xcontenttypeoptions_none_client_check", "script_executed");'.format(test_id=test_id))
    save(test_id, "xcontenttypeoptions_none", "test_setup")
    return response



#-----------------------------------------------------------------------------------------------------------------------
# Test value: nosniff
#-----------------------------------------------------------------------------------------------------------------------

def nosniff_setup(request, test_id):
    # return JS code to execute
    response = HttpResponse('save_result("{test_id}", "xcontenttypeoptions_nosniff_client_check", "script_executed")'.format(test_id=test_id))
    response['X-Content-type-Options'] = 'nosniff'
    save(test_id, "xcontenttypeoptions_nosniff", "test_setup")
    return response