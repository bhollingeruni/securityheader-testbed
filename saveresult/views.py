from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from saveresult.utils import save_entry
import logging

# Create your views here.
def index(request):
    response = HttpResponse('Index')
    return response


@csrf_exempt
def save(request, test_id, result_key, result_value):
    save_entry(test_id, result_key, result_value)
    # TODO: save result to DB
    response = HttpResponse('Save result ' + test_id + ' ' + result_key + ': ' + result_value)
    return response
