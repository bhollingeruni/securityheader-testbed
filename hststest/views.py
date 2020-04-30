from django.shortcuts import render
from django.http import HttpResponse
from testsuite.settings import CURRENT_SECURE_ORIGIN
from testsuite.settings import CURRENT_ORIGIN
from testsuite.settings import CURRENT_DOMAIN
from testsuite.settings import CURRENT_SCHEME
from testsuite.settings import CURRENT_PORT
from testsuite.settings import EXTERNAL_SUBDOMAIN_ORIGIN
from testsuite.settings import EXTERNAL_ORIGIN
from testsuite.settings import EXTERNAL_SECURE_ORIGIN
from testsuite.settings import EXTERNAL_DOMAIN
from testsuite.settings import EXTERNAL_SCHEME
from testsuite.settings import EXTERNAL_PORT
from saveresult.utils import save
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.views.decorators.clickjacking import xframe_options_exempt

# Create your views here.
def index(request):
    response = HttpResponse('HSTS test index')
    return response

# Serves the iframe setting up the check requests
# Needs to be called over HTTPS, otherwise browsers ignore the header
def setup(request, test_id):
    # compose response
    context = { 'test_id': test_id, 'external_origin': EXTERNAL_ORIGIN, 'current_origin': CURRENT_ORIGIN, "external_subdomain_origin": EXTERNAL_SUBDOMAIN_ORIGIN, "current_secure_origin": CURRENT_SECURE_ORIGIN }
    response = render(request, 'hststest/setup.html', context)
    save(test_id, "hsts_setup", 'test_setup')
    return response

# Contains the two check requests to avoid cross domain entanglements
@xframe_options_exempt
def frame(request, test_id):
    context = { 'test_id': test_id, 'external_origin': EXTERNAL_ORIGIN, 'external_secure_origin': EXTERNAL_SECURE_ORIGIN, 'current_origin': CURRENT_ORIGIN, "external_subdomain_origin": EXTERNAL_SUBDOMAIN_ORIGIN }
    response = render(request, 'hststest/frame.html', context)
    save(test_id, "hsts_frame", 'frame_request_received')
    return response

# Sets up the check request by setting the HSTS header
# Needs to be called over HTTPS, otherwise browsers ignore the header
def check_setup(request, test_id):
    response = HttpResponse('HSTS test check setup')
    save(test_id, "hsts_check_setup", 'check_setup_request_received')
    response["Strict-Transport-Security"] = "max-age=30; includeSubDomains"
    response["Access-Control-Allow-Origin"] = "*"
    return response

# Checks if the request was redirected to HTTPS
@xframe_options_exempt
def check_scheme(request, test_id):
    save(test_id, "hsts_scheme_check", 'check_scheme_request_received')
    if request.is_secure():
        save(test_id, "hsts_scheme_check", "request_sent_over_https")
    else:
        save(test_id, "hsts_scheme_check", "request_sent_over_http")
    response = HttpResponse('HSTS test check scheme')
    response["Access-Control-Allow-Origin"] = "*"
    return response

# Checks if the request to the subdomain was redirected to HTTPS
@xframe_options_exempt
def check_scheme_subdomain(request, test_id):
    save(test_id, "hsts_scheme_subdomain_check", 'check_scheme_subdomain_request_received')
    if request.is_secure():
        save(test_id, "hsts_scheme_subdomain_check", "request_sent_over_https")
    else:
        save(test_id, "hsts_scheme_subdomain_check", "request_sent_over_http")
    response = HttpResponse('HSTS test check scheme subdomain')
    response["Access-Control-Allow-Origin"] = "*"
    return response
