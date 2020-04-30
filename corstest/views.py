from django.shortcuts import render
from django.http import HttpResponse
from testsuite.settings import CURRENT_ORIGIN
from testsuite.settings import CURRENT_DOMAIN
from testsuite.settings import CURRENT_SCHEME
from testsuite.settings import CURRENT_PORT
from testsuite.settings import EXTERNAL_ORIGIN
from testsuite.settings import EXTERNAL_DOMAIN
from testsuite.settings import EXTERNAL_SCHEME
from testsuite.settings import EXTERNAL_PORT
from saveresult.utils import save
from django.contrib.staticfiles.templatetags.staticfiles import static

def index(request):
    response = HttpResponse('CORS test index')
    return response

# Sets up the tests for simple requests
def simple_setup(request, test_id):
    request_mode = 'simple'

    # compose response
    context = { 'test_id': test_id, 'mode': request_mode, 'external_origin': EXTERNAL_ORIGIN, 'current_origin': CURRENT_ORIGIN, "current_domain": CURRENT_DOMAIN, "current_port": CURRENT_PORT, "external_domain": EXTERNAL_DOMAIN, "external_port": EXTERNAL_PORT }
    response = render(request, 'corstest/simple_setup.html', context)

    # set a cookie to test sending of credentials
    response.set_cookie('cookie_cors_test', test_id)
    save(test_id, "cors_simple_setup", 'test_setup')
    return response

# Sets up the tests for complex requests
def complex_setup(request, test_id):
    request_mode = 'complex'

    # compose response
    context = { 'test_id': test_id, 'mode': request_mode, 'external_origin': EXTERNAL_ORIGIN, 'current_origin': CURRENT_ORIGIN, "current_domain": CURRENT_DOMAIN, "current_port": CURRENT_PORT, "external_domain": EXTERNAL_DOMAIN, "external_port": EXTERNAL_PORT }
    response = render(request, 'corstest/complex_setup.html', context)

    # set a cookie to test sending of credentials
    response.set_cookie('cookie_cors_test', test_id)
    save(test_id, "cors_complex_setup", 'test_setup')
    return response

# This is the resource endpoint called by the CORS requests
def resource(request, test_id, mode, value):

    # differentiate between preflight and resource requests
    if (request.method == "OPTIONS"):
        request_type = "preflight"        
    else:
        request_type = "resource"
    
    save(test_id, "cors_{value}_{mode}_{request_type}".format(value=value, mode=mode, request_type=request_type), 'request_received')

    # check if the cookie was sent with the request
    cookie_value = request.COOKIES.get('cookie_cors_test')
    if cookie_value is None:
        save(test_id, "cors_{value}_{mode}_{request_type}".format(mode=mode, value=value, request_type=request_type), 'cookie_not_set')

    elif cookie_value != test_id:
        save(test_id, "cors_{value}_{mode}_{request_type}".format(mode=mode, value=value, request_type=request_type), 'cookie_wrong_value: ' + cookie_value)

    elif cookie_value == test_id:
        save(test_id, "cors_{value}_{mode}_{request_type}".format(mode=mode, value=value, request_type=request_type), 'cookie_correct_value')

    # check if the authorization header was sent with the request
    authorization_header_value = request.META.get('HTTP_AUTHORIZATION')

    if authorization_header_value is None:
        save(test_id, "cors_{value}_{mode}_{request_type}".format(mode=mode, value=value, request_type=request_type), 'auth_header_not_set')

    elif authorization_header_value != "Basic dGVzdHVzZXI6dGVzdHBhc3N3b3Jk":
        save(test_id, "cors_{value}_{mode}_{request_type}".format(mode=mode, value=value, request_type=request_type), 'auth_header_wrong_value: ' + authorization_header_value)

    elif authorization_header_value == "Basic dGVzdHVzZXI6dGVzdHBhc3N3b3Jk":
        save(test_id, "cors_{value}_{mode}_{request_type}".format(mode=mode, value=value, request_type=request_type), 'auth_header_correct_value')

    # check if the custom request header was sent with the request
    requesttest_header_value = request.META.get('HTTP_X_REQUESTTESTHEADER')

    if requesttest_header_value is None:
        save(test_id, "cors_{value}_{mode}_{request_type}".format(mode=mode, value=value, request_type=request_type), 'requesttestheader_header_not_set')

    elif requesttest_header_value != "valid":
        save(test_id, "cors_{value}_{mode}_{request_type}".format(mode=mode, value=value, request_type=request_type), 'requesttestheader_header_wrong_value: ' + requesttest_header_value)

    elif requesttest_header_value == "valid":
        save(test_id, "cors_{value}_{mode}_{request_type}".format(mode=mode, value=value, request_type=request_type), 'requesttestheader_header_correct_value')

    # compose response
    context = { 'test_id': test_id, 'mode': mode, 'value': value, 'external_origin': EXTERNAL_ORIGIN, 'current_origin': CURRENT_ORIGIN, "current_domain": CURRENT_DOMAIN, "current_port": CURRENT_PORT, "external_domain": EXTERNAL_DOMAIN, "external_port": EXTERNAL_PORT }
    response = render(request, 'corstest/resource.html', context)

    # generate headers depending on the current scenario
    headers = generate_header(value)
    for header in headers:
        response[header["header_name"]] = header["header_value"]
        response["X-Responsetestheader"] = "valid"
    return response

def generate_header(value):
    if (value in ["default", "default_external"]):
        return []

    if (value in ["origin_null", "origin_null_external"]):
        return [ {"header_name": "Access-Control-Allow-Origin", "header_value": "null"} ]

    if (value in ["origin_all", "origin_all_external"]):
        return [ {"header_name": "Access-Control-Allow-Origin", "header_value": "*" } ]

    if (value in ["origin_valid", "origin_valid_external"]):
        return [ {"header_name": "Access-Control-Allow-Origin", "header_value": CURRENT_ORIGIN} ]

    if (value in ["origin_scheme_invalid", "origin_scheme_invalid_external"]):
        return [ {"header_name": "Access-Control-Allow-Origin", "header_value": "{scheme}://{domain}:{port}".format(scheme="ftp", domain=CURRENT_DOMAIN, port=CURRENT_PORT)} ]

    if (value in ["origin_domain_invalid", "origin_domain_invalid_external"]):
        return [ {"header_name": "Access-Control-Allow-Origin", "header_value": "{scheme}://{domain}:{port}".format(scheme=CURRENT_SCHEME, domain="invalid.test", port=CURRENT_PORT)} ]

    if (value in ["origin_port_invalid", "origin_port_invalid_external"]):
        return [ {"header_name": "Access-Control-Allow-Origin", "header_value": "{scheme}://{domain}:{port}".format(scheme=CURRENT_SCHEME, domain=CURRENT_DOMAIN, port="9999")} ]

    if (value in ["exposeheader_invalid", "exposeheader_invalid_external"]):
        return [ {"header_name": "Access-Control-Allow-Origin", "header_value": "*"}, {"header_name": "Access-Control-Expose-Headers", "header_value": "X-Invalidheader"} ]

    if (value in ["exposeheader_valid", "exposeheader_valid_external"]):
        return [ {"header_name": "Access-Control-Allow-Origin", "header_value": "*"}, {"header_name": "Access-Control-Expose-Headers", "header_value": "X-Responsetestheader"} ]

    if (value in ["credentials_all", "credentials_all_external"]):
        return [ {"header_name": "Access-Control-Allow-Origin", "header_value": "*"}, {"header_name": "Access-Control-Allow-Credentials", "header_value": "true"}, {"header_name": "Access-Control-Allow-Headers", "header_value": "Authorization"} ]

    if (value in ["credentials_origin_valid", "credentials_origin_valid_external"]):
        return [ {"header_name": "Access-Control-Allow-Origin", "header_value": CURRENT_ORIGIN}, {"header_name": "Access-Control-Allow-Credentials", "header_value": "true"}, {"header_name": "Access-Control-Allow-Headers", "header_value": "Authorization"} ]

    if (value in ["credentials_origin_invalid", "credentials_origin_invalid_external"]):
        return [ {"header_name": "Access-Control-Allow-Origin", "header_value": "http://invalid.test"}, {"header_name": "Access-Control-Allow-Credentials", "header_value": "true"}, {"header_name": "Access-Control-Allow-Headers", "header_value": "Authorization"} ]

    if (value in ["allowheaders_valid", "allowheaders_valid_external"]):
        return [ {"header_name": "Access-Control-Allow-Origin", "header_value": "*"}, {"header_name": "Access-Control-Allow-Headers", "header_value": "X-Requesttestheader"} ]

    if (value in ["allowheaders_invalid", "allowheaders_invalid_external"]):
        return [ {"header_name": "Access-Control-Allow-Origin", "header_value": "*"}, {"header_name": "Access-Control-Allow-Headers", "header_value": "X-InvalidRequesttestheader"} ]

    return []

