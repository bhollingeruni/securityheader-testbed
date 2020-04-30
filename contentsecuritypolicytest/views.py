from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from saveresult.utils import save
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.conf import settings
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from testsuite.settings import CURRENT_ORIGIN
from testsuite.settings import CURRENT_DOMAIN
from testsuite.settings import CURRENT_SCHEME
from testsuite.settings import CURRENT_PORT
from testsuite.settings import EXTERNAL_ORIGIN
from testsuite.settings import EXTERNAL_DOMAIN
from testsuite.settings import EXTERNAL_SCHEME
from testsuite.settings import EXTERNAL_PORT
from django.views.decorators.clickjacking import xframe_options_exempt
import hashlib
import base64

# Create your views here.
def index(request):
    response = HttpResponse('Content-Security-Policy test index')
    return response



# ----------------------------------------------------------------------------------------------------------------------
# Test directive: frame-src
# ----------------------------------------------------------------------------------------------------------------------

def framesrc_setup(request, test_id, value):
    formatted_value = format_value(value)
    save(test_id, "contentsecuritypolicy_framesrc_{value}_setup".format(value=value), 'test_setup')
    # initialize frame as not loaded. This will be overwritten by the ajax request of the loaded frame
    save(test_id, "contentsecuritypolicy_framesrc_{value}_check".format(value=value), 'frame_request_not_received')

    # compose response
    context = { 'test_id': test_id, 'value': value, 'external_origin': EXTERNAL_ORIGIN, 'current_origin': CURRENT_ORIGIN, "current_domain": CURRENT_DOMAIN, "current_port": CURRENT_PORT, "external_domain": EXTERNAL_DOMAIN, "external_port": EXTERNAL_PORT}
    response = render(request, 'contentsecuritypolicytest/framesrc_setup.html', context)
    response['Content-Security-Policy'] = "frame-src {value}".format(value=formatted_value)
    return response

@xframe_options_exempt
def framesrc_frame(request, test_id, value):
    context = { 'test_id': test_id, 'value': value }
    save(test_id, "contentsecuritypolicy_framesrc_{value}_frame".format(value=value), 'request_received')
    # update test result
    save(test_id, "contentsecuritypolicy_framesrc_{value}_check".format(value=value), 'frame_not_loaded')
    response = render(request, 'contentsecuritypolicytest/framesrc_frame.html', context)
    return response

def framesrc_check(request, test_id, value):
    # update test result
    save(test_id, "contentsecuritypolicy_framesrc_{value}_check".format(value=value), 'frame_loaded')
    return HttpResponse('Content-Security-Policy contentsecuritypolicy_framesrc_check_' + value)



# ----------------------------------------------------------------------------------------------------------------------
# Test directive: img-src
# ----------------------------------------------------------------------------------------------------------------------

def imgsrc_setup(request, test_id, value):
    formatted_value = format_value(value)
    save(test_id, "contentsecuritypolicy_imgsrc_{value}_setup".format(value=value), 'test_setup')
    # initialize frame as not loaded. This will be overwritten by the ajax request of the loaded frame
    save(test_id, "contentsecuritypolicy_imgsrc_{value}_check".format(value=value), 'image_request_not_received')

    # compose response
    context = { 'test_id': test_id, 'value': value, 'external_origin': EXTERNAL_ORIGIN, 'current_origin': CURRENT_ORIGIN, "current_domain": CURRENT_DOMAIN, "current_port": CURRENT_PORT, "external_domain": EXTERNAL_DOMAIN, "external_port": EXTERNAL_PORT }
    response = render(request, 'contentsecuritypolicytest/imgsrc_setup.html', context)
    response['Content-Security-Policy'] = "img-src {value}".format(value=formatted_value)
    return response

def imgsrc_check(request, test_id, value):
    # update test result
    save(test_id, "contentsecuritypolicy_imgsrc_{value}_check".format(value=value), 'image_request_received')

    # return a checkmark image
    image_path = settings.BASE_DIR + "/files/images/checkmark.png"
    with open(image_path, "rb") as f:
        return HttpResponse(f.read(), content_type="image/jpeg")



# ----------------------------------------------------------------------------------------------------------------------
# Test directive: script-src
# ----------------------------------------------------------------------------------------------------------------------

def scriptsrc_setup(request, test_id, value):
    context = { 'test_id': test_id, 'value': value, 'external_origin': EXTERNAL_ORIGIN, 'current_origin': CURRENT_ORIGIN, "current_domain": CURRENT_DOMAIN, "current_port": CURRENT_PORT, "external_domain": EXTERNAL_DOMAIN, "external_port": EXTERNAL_PORT }
    # add an inline script as alternative test case to the external script
    context['inline_script'] = render_template(request, context, 'contentsecuritypolicytest/scriptsrc_inline_script.js')
    context['unsafeeval_inline_script'] = render_template(request, context, 'contentsecuritypolicytest/scriptsrc_unsafeeval_inline_script.js')
    context['strictdynamic_inline_script'] = render_template(request, context, 'contentsecuritypolicytest/scriptsrc_strictdynamic_inline_script.js')

    context['url_script'] = render_template(request, context, 'contentsecuritypolicytest/scriptsrc_url_script.js')
    context['unsafeeval_url_script'] = render_template(request, context, 'contentsecuritypolicytest/scriptsrc_unsafeeval_url_script.js')
    context['strictdynamic_url_script'] = render_template(request, context, 'contentsecuritypolicytest/scriptsrc_strictdynamic_url_script.js')

    formatted_value = format_value(value, request, context, 'contentsecuritypolicytest/scriptsrc_script.js')

    save(test_id, "contentsecuritypolicy_scriptsrc_{value}_setup".format(value=value), 'test_setup')
    # initialize frame as not loaded. This will be overwritten by the ajax request of the loaded frame
    save(test_id, "contentsecuritypolicy_scriptsrc_{value}_check".format(value=value), 'script_request_not_received')

    # compose response
    response = render(request, 'contentsecuritypolicytest/scriptsrc_setup.html', context)

    #sha-XXX directive only allows inline scripts => generate hash of inline script and put it into the directive
    if (value in ['sha256_valid', 'sha256_invalid', 'sha384_valid', 'sha384_invalid', 'sha512_valid', 'sha512_invalid', 'strictdynamic_hash_valid', 'strictdynamic_hash_invalid']):
        formatted_inline_value = format_value(value, request, context, 'contentsecuritypolicytest/scriptsrc_inline_script.js')
        csp_directive = "script-src {value}".format(value=formatted_inline_value)
    else:
        csp_directive = "script-src {value}".format(value=formatted_value)

    response['Content-Security-Policy'] = csp_directive
    return response

def scriptsrc_script(request, test_id, value):
    context = { 'test_id': test_id, 'value': value }
    save(test_id, "contentsecuritypolicy_scriptsrc_{value}_script".format(value=value), 'request_received')
    # update test result
    save(test_id, "contentsecuritypolicy_scriptsrc_{value}_check".format(value=value), 'script_request_received')

    return render(request, 'contentsecuritypolicytest/scriptsrc_script.js', context,
                            content_type="application/x-javascript")

def scriptsrc_unsafeeval_script(request, test_id, value):
    context = { 'test_id': test_id, 'value': value }
    save(test_id, "contentsecuritypolicy_scriptsrc_{value}_unsafeeval_script".format(value=value), 'request_received')
    # update test result
    save(test_id, "contentsecuritypolicy_scriptsrc_{value}_unsafeeval_check".format(value=value), 'script_request_received')

    return render(request, 'contentsecuritypolicytest/scriptsrc_unsafeeval_script.js', context,
                            content_type="application/x-javascript")

def scriptsrc_strictdynamic_script(request, test_id, value):
    context = { 'test_id': test_id, 'value': value }
    save(test_id, "contentsecuritypolicy_scriptsrc_{value}_strictdynamic_script".format(value=value), 'request_received')
    # update test result
    save(test_id, "contentsecuritypolicy_scriptsrc_{value}_strictdynamic_check".format(value=value), 'script_request_received')

    return render(request, 'contentsecuritypolicytest/scriptsrc_strictdynamic_script.js', context,
                            content_type="application/x-javascript")

# serves the sub-script inserted during the strict-dynamic test. Is called either by a parser-inserted or non-parser-inserted scripts
def scriptsrc_strictdynamic_inserted_script(request, test_id, value):
    context = { 'test_id': test_id, 'value': value }
    save(test_id, "contentsecuritypolicy_scriptsrc_{value}_strictdynamic_inserted_script".format(value=value), 'request_received')
    # update test result
    save(test_id, "contentsecuritypolicy_scriptsrc_{value}_strictdynamic_inserted_check".format(value=value), 'script_request_received')

    return render(request, 'contentsecuritypolicytest/scriptsrc_strictdynamic_inserted_script.js', context,
                            content_type="application/x-javascript")

def scriptsrc_check(request, test_id, value):
    # update test result
    save(test_id, "contentsecuritypolicy_scriptsrc_{value}_check".format(value=value), 'script_executed')
    return HttpResponse('Content-Security-Policy contentsecuritypolicy_scriptsrc_check_' + value)



# ----------------------------------------------------------------------------------------------------------------------
# Test directive: frame-ancestors
# ----------------------------------------------------------------------------------------------------------------------

def frameancestors_setup(request, test_id, value):
    formatted_value = format_value(value)
    save(test_id, "contentsecuritypolicy_frameancestors_{value}_setup".format(value=value), 'test_setup')
    # initialize frame as not loaded. This will be overwritten by the ajax request of the loaded frame
    save(test_id, "contentsecuritypolicy_frameancestors_{value}_check".format(value=value), 'frame_request_not_received')

    # compose response
    context = { 'test_id': test_id, 'value': value }
    response = render(request, 'contentsecuritypolicytest/frameancestors_setup.html', context)
    response['Content-Security-Policy'] = "frame-ancestors {value}".format(value=formatted_value)
    return response

def frameancestors_frame_outer(request, test_id, value):
    context = { 'test_id': test_id, 'value': value }
    save(test_id, "contentsecuritypolicy_frameancestors_{value}_frame_outer".format(value=value), 'request_received')
    # update test result
    save(test_id, "contentsecuritypolicy_frameancestors_{value}_check".format(value=value), 'outer_frame_not_loaded')
    return render(request, 'contentsecuritypolicytest/frameancestors_frame_outer.html', context)

# The inner iframe checks if directory holds for ancestors that are not direct parents
def frameancestors_frame_inner(request, test_id, value):
    context = { 'test_id': test_id, 'value': value }
    save(test_id, "contentsecuritypolicy_frameancestors_{value}_frame_inner".format(value=value), 'request_received')
    # update test result
    save(test_id, "contentsecuritypolicy_frameancestors_{value}_check".format(value=value), 'inner_frame_not_loaded')
    return render(request, 'contentsecuritypolicytest/frameancestors_frame_inner.html', context)

def frameancestors_check(request, test_id, value):
    # update test result
    save(test_id, "contentsecuritypolicy_frameancestors_{value}_check".format(value=value), 'frame_loaded')
    return HttpResponse('Content-Security-Policy contentsecuritypolicy_frameancestors_check_' + value)



# ----------------------------------------------------------------------------------------------------------------------
# Test directive: default-src
# ----------------------------------------------------------------------------------------------------------------------

def defaultsrc_scriptsrc_setup(request, test_id, value):

    context = { 'test_id': test_id, 'value': value , 'external_origin': EXTERNAL_ORIGIN, 'current_origin': CURRENT_ORIGIN, "current_domain": CURRENT_DOMAIN, "current_port": CURRENT_PORT, "external_domain": EXTERNAL_DOMAIN, "external_port": EXTERNAL_PORT }
    # add an inline script as alternative test case to the external script
    context['inline_script'] = render_template(request, context, 'contentsecuritypolicytest/defaultsrc_inline_script.js')
    context['unsafeeval_inline_script'] = render_template(request, context, 'contentsecuritypolicytest/defaultsrc_unsafeeval_inline_script.js')
    context['strictdynamic_inline_script'] = render_template(request, context, 'contentsecuritypolicytest/defaultsrc_strictdynamic_inline_script.js')

    context['url_script'] = render_template(request, context, 'contentsecuritypolicytest/defaultsrc_url_script.js')
    context['unsafeeval_url_script'] = render_template(request, context, 'contentsecuritypolicytest/defaultsrc_unsafeeval_url_script.js')
    context['strictdynamic_url_script'] = render_template(request, context, 'contentsecuritypolicytest/defaultsrc_strictdynamic_url_script.js')

    formatted_value = format_value(value, request, context, 'contentsecuritypolicytest/defaultsrc_script.js')

    save(test_id, "contentsecuritypolicy_defaultsrc_scriptsrc_{value}_setup".format(value=value), 'test_setup')
    # initialize frame as not loaded. This will be overwritten by the ajax request of the loaded frame
    save(test_id, "contentsecuritypolicy_defaultsrc_scriptsrc_{value}_check".format(value=value), 'script_request_not_received')

    # compose response
    response = render(request, 'contentsecuritypolicytest/defaultsrc_scriptsrc_setup.html', context)

    #sha-XXX directive only allows inline scripts => generate hash of inline script and put it into the directive
    if (value in ['sha256_valid', 'sha256_invalid', 'sha384_valid', 'sha384_invalid', 'sha512_valid', 'sha512_invalid', 'strictdynamic_hash_valid', 'strictdynamic_hash_invalid']):
        formatted_inline_value = format_value(value, request, context, 'contentsecuritypolicytest/defaultsrc_inline_script.js')
        csp_directive = "default-src {value}".format(value=formatted_inline_value) + "; connect-src *; img-src *; frame-src *"
    else:
        csp_directive = "default-src {value}".format(value=formatted_value) + "; connect-src *; img-src *; frame-src *"

    response['Content-Security-Policy'] = csp_directive
    return response

def defaultsrc_framesrc_setup(request, test_id, value):
    formatted_value = format_value(value)
    save(test_id, "contentsecuritypolicy_defaultsrc_framesrc_{value}_setup".format(value=value), 'test_setup')
    # initialize frame as not loaded. This will be overwritten by the ajax request of the loaded frame
    save(test_id, "contentsecuritypolicy_defaultsrc_framesrc_{value}_check".format(value=value), 'frame_request_not_received')

    # compose response
    context = { 'test_id': test_id, 'value': value, 'external_origin': EXTERNAL_ORIGIN, 'current_origin': CURRENT_ORIGIN, "current_domain": CURRENT_DOMAIN, "current_port": CURRENT_PORT, "external_domain": EXTERNAL_DOMAIN, "external_port": EXTERNAL_PORT}
    response = render(request, 'contentsecuritypolicytest/defaultsrc_framesrc_setup.html', context)
    response['Content-Security-Policy'] = "default-src {value}".format(value=formatted_value) + "; script-src *; connect-src *; img-src *"
    return response

def defaultsrc_imgsrc_setup(request, test_id, value):
    formatted_value = format_value(value)
    save(test_id, "contentsecuritypolicy_defaultsrc_imgsrc_{value}_setup".format(value=value), 'test_setup')
    # initialize frame as not loaded. This will be overwritten by the ajax request of the loaded frame
    save(test_id, "contentsecuritypolicy_defaultsrc_imgsrc_{value}_check".format(value=value), 'image_request_not_received')

    # compose response
    context = { 'test_id': test_id, 'value': value, 'external_origin': EXTERNAL_ORIGIN, 'current_origin': CURRENT_ORIGIN, "current_domain": CURRENT_DOMAIN, "current_port": CURRENT_PORT, "external_domain": EXTERNAL_DOMAIN, "external_port": EXTERNAL_PORT }
    response = render(request, 'contentsecuritypolicytest/defaultsrc_imgsrc_setup.html', context)
    response['Content-Security-Policy'] = "default-src {value}".format(value=formatted_value) + "; script-src *; connect-src *; frame-src *"
    return response

def defaultsrc_stylesrc_setup(request, test_id, value):
    context = { 'test_id': test_id, 'value': value, 'external_origin': EXTERNAL_ORIGIN, 'current_origin': CURRENT_ORIGIN, "current_domain": CURRENT_DOMAIN, "current_port": CURRENT_PORT, "external_domain": EXTERNAL_DOMAIN, "external_port": EXTERNAL_PORT }
    formatted_value = format_value(value, request, context, 'contentsecuritypolicytest/defaultsrc_stylesrc_stylesheet.css')

    context['inline_stylesheet'] = render_template(request, context, 'contentsecuritypolicytest/defaultsrc_stylesrc_inline_stylesheet.css')

    save(test_id, "contentsecuritypolicy_defaultsrc_stylesrc_{value}_setup".format(value=value), 'test_setup')
    save(test_id, "contentsecuritypolicy_defaultsrc_stylesrc_{value}_check".format(value=value), 'stylesheet_request_not_received')

    # compose response
    response = render(request, 'contentsecuritypolicytest/defaultsrc_stylesrc_setup.html', context)

    #sha-XXX directive only allows inline scripts => generate hash of inline script and put it into the directive
    if (value in ['sha256_valid', 'sha256_invalid', 'sha384_valid', 'sha384_invalid', 'sha512_valid', 'sha512_invalid', 'strictdynamic_hash_valid', 'strictdynamic_hash_invalid']):
        formatted_inline_value = format_value(value, request, context, 'contentsecuritypolicytest/defaultsrc_stylesrc_inline_stylesheet.css')
        csp_directive = "default-src {value}".format(value=formatted_inline_value) + "; script-src *; connect-src *; img-src *"
    else:
        csp_directive = "default-src {value}".format(value=formatted_value) + "; script-src *; connect-src *; img-src *"

    response['Content-Security-Policy'] = csp_directive
    response["Link"] = "<{current_origin}/contentsecuritypolicytest/defaultsrc_stylesrc_stylesheet/{test_id}/{value}/link_header>; rel=\"stylesheet\", ".format(current_origin=CURRENT_ORIGIN, test_id=test_id, value=value) + "<{external_origin}/contentsecuritypolicytest/defaultsrc_stylesrc_stylesheet/{test_id}/{value}/link_header_external>; rel=\"stylesheet\"".format(external_origin=EXTERNAL_ORIGIN, test_id=test_id, value=value)
    return response

def defaultsrc_stylesrc_stylesheet(request, test_id, value, element_id):
    context = { 'test_id': test_id, 'value': value, 'element_id': element_id }
    save(test_id, "contentsecuritypolicy_defaultsrc_stylesrc_{value}_{element_id}_stylesheet".format(value=value, element_id=element_id), 'request_received')
    # update test result
    save(test_id, "contentsecuritypolicy_defaultsrc_stylesrc_{value}_{element_id}_check".format(value=value, element_id=element_id), 'stylesheet_request_received')

    return render(request, 'contentsecuritypolicytest/defaultsrc_stylesrc_stylesheet.css', context,
                            content_type="text/css")


def defaultsrc_script(request, test_id, value):
    context = { 'test_id': test_id, 'value': value }
    save(test_id, "contentsecuritypolicy_defaultsrc_scriptsrc_{value}_script".format(value=value), 'request_received')
    # update test result
    save(test_id, "contentsecuritypolicy_defaultsrc_scriptsrc_{value}_check".format(value=value), 'script_request_received')

    return render(request, 'contentsecuritypolicytest/defaultsrc_script.js', context,
                            content_type="application/x-javascript")

def defaultsrc_unsafeeval_script(request, test_id, value):
    context = { 'test_id': test_id, 'value': value }
    save(test_id, "contentsecuritypolicy_defaultsrc_scriptsrc_unsafeeval_{value}_script".format(value=value), 'request_received')
    # update test result
    save(test_id, "contentsecuritypolicy_defaultsrc_scriptsrc_unsafeeval_{value}_check".format(value=value), 'script_request_received')

    return render(request, 'contentsecuritypolicytest/defaultsrc_unsafeeval_script.js', context,
                            content_type="application/x-javascript")

def defaultsrc_strictdynamic_script(request, test_id, value):
    context = { 'test_id': test_id, 'value': value }
    save(test_id, "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_{value}_script".format(value=value), 'request_received')
    # update test result
    save(test_id, "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_{value}_check".format(value=value), 'script_request_received')

    return render(request, 'contentsecuritypolicytest/defaultsrc_strictdynamic_script.js', context,
                            content_type="application/x-javascript")

# serves the sub-script inserted during the strict-dynamic test. Is called either by a parser-inserted or non-parser-inserted scripts
def defaultsrc_strictdynamic_inserted_script(request, test_id, value):
    context = { 'test_id': test_id, 'value': value }
    save(test_id, "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_inserted_{value}_script".format(value=value), 'request_received')
    # update test result
    save(test_id, "contentsecuritypolicy_defaultsrc_scriptsrc_strictdynamic_inserted_{value}_check".format(value=value), 'script_request_received')

    return render(request, 'contentsecuritypolicytest/defaultsrc_strictdynamic_inserted_script.js', context,
                            content_type="application/x-javascript")

@xframe_options_exempt
def defaultsrc_frame(request, test_id, value):
    context = { 'test_id': test_id, 'value': value }
    save(test_id, "contentsecuritypolicy_defaultsrc_framesrc_{value}_frame".format(value=value), 'request_received')
    # update test result
    save(test_id, "contentsecuritypolicy_defaultsrc_framesrc_{value}_check".format(value=value), 'frame_not_loaded')
    return render(request, 'contentsecuritypolicytest/defaultsrc_frame.html', context)


def defaultsrc_frame_outer(request, test_id, value):
    context = { 'test_id': test_id, 'value': value }
    save(test_id, "contentsecuritypolicy_defaultsrc_framesrc_{value}_frame_outer".format(value=value), 'request_received')
    # update test result
    save(test_id, "contentsecuritypolicy_defaultsrc_framesrc_{value}_check".format(value=value), 'outer_frame_not_loaded')
    return render(request, 'contentsecuritypolicytest/defaultsrc_frame_outer.html', context)

def defaultsrc_frame_inner(request, test_id, value):
    context = { 'test_id': test_id, 'value': value }
    save(test_id, "contentsecuritypolicy_defaultsrc_framesrc_{value}_frame_inner".format(value=value), 'request_received')
    # update test result
    save(test_id, "contentsecuritypolicy_defaultsrc_framesrc_{value}_check".format(value=value), 'inner_frame_not_loaded')
    return render(request, 'contentsecuritypolicytest/defaultsrc_frame_inner.html', context)

def defaultsrc_workersrc_setup(request, test_id, value):
    formatted_value = format_value(value)
    save(test_id, "contentsecuritypolicy_defaultsrc_workersrc_{value}_setup".format(value=value), 'test_setup')

    # compose response
    context = { 'test_id': test_id, 'value': value, 'external_origin': EXTERNAL_ORIGIN, 'current_origin': CURRENT_ORIGIN, "current_domain": CURRENT_DOMAIN, "current_port": CURRENT_PORT, "external_domain": EXTERNAL_DOMAIN, "external_port": EXTERNAL_PORT }
    response = render(request, 'contentsecuritypolicytest/defaultsrc_workersrc_setup.html', context)
    response['Content-Security-Policy'] = "default-src {value}".format(value=formatted_value) + "; script-src * 'unsafe-inline'; connect-src *; img-src *"
    return response

def defaultsrc_workersrc_script(request, test_id, value):
    context = { 'test_id': test_id, 'value': value }
    save(test_id, "contentsecuritypolicy_defaultsrc_workersrc_{value}_script".format(value=value), 'request_received')
    # update test result
    save(test_id, "contentsecuritypolicy_defaultsrc_workersrc_{value}_check".format(value=value), 'script_request_received')
    response = render(request, 'contentsecuritypolicytest/defaultsrc_workersrc_script.js', context, content_type="application/x-javascript")
    return response

def defaultsrc_workersrc_check(request, test_id, value):
    # update test result
    save(test_id, "contentsecuritypolicy_defaultsrc_workersrc_{value}_check".format(value=value), 'worker_request_received')

    # return a checkmark image
    response = HttpResponse('Content-Security-Policy contentsecuritypolicy_defaultsrc_workersrc_check_' + value)
    return response

def defaultsrc_check(request, test_id, value):
    # update test result
    save(test_id, "contentsecuritypolicy_defaultsrc_{value}_check".format(value=value), 'check_successful')
    return HttpResponse("Check successful")



# ----------------------------------------------------------------------------------------------------------------------
# Test directive: connect-src
# ----------------------------------------------------------------------------------------------------------------------

def connectsrc_setup(request, test_id, value):
    formatted_value = format_value(value)
    save(test_id, "contentsecuritypolicy_connectsrc_{value}_setup".format(value=value), 'test_setup')
    # initialize frame as not loaded. This will be overwritten by the ajax request of the loaded frame
    save(test_id, "contentsecuritypolicy_connectsrc_{value}_check".format(value=value), 'connect_request_not_received')

    # compose response
    context = { 'test_id': test_id, 'value': value, 'external_origin': EXTERNAL_ORIGIN, 'current_origin': CURRENT_ORIGIN, "current_domain": CURRENT_DOMAIN, "current_port": CURRENT_PORT, "external_domain": EXTERNAL_DOMAIN, "external_port": EXTERNAL_PORT}
    response = render(request, 'contentsecuritypolicytest/connectsrc_setup.html', context)
    response['Content-Security-Policy'] = "connect-src {value}".format(value=formatted_value)
    return response

# csrf exempt since <a ping> posts here
@csrf_exempt
def connectsrc_check(request, test_id, value):
    # update test result
    save(test_id, "contentsecuritypolicy_connectsrc_{value}_check".format(value=value), 'check_successful')
    response = HttpResponse('Content-Security-Policy contentsecuritypolicy_connectsrc_check_' + value)
    response["Access-Control-Allow-Origin"] = "*"
    return response



# ----------------------------------------------------------------------------------------------------------------------
# Test directive: style-src
# ----------------------------------------------------------------------------------------------------------------------

def stylesrc_setup(request, test_id, value):
    context = { 'test_id': test_id, 'value': value, 'external_origin': EXTERNAL_ORIGIN, 'current_origin': CURRENT_ORIGIN, "current_domain": CURRENT_DOMAIN, "current_port": CURRENT_PORT, "external_domain": EXTERNAL_DOMAIN, "external_port": EXTERNAL_PORT }
    formatted_value = format_value(value, request, context, 'contentsecuritypolicytest/stylesrc_stylesheet.css')

    context['inline_stylesheet'] = render_template(request, context, 'contentsecuritypolicytest/stylesrc_inline_stylesheet.css')

    save(test_id, "contentsecuritypolicy_stylesrc_{value}_setup".format(value=value), 'test_setup')
    save(test_id, "contentsecuritypolicy_stylesrc_{value}_check".format(value=value), 'stylesheet_request_not_received')

    # compose response
    response = render(request, 'contentsecuritypolicytest/stylesrc_setup.html', context)

    #sha-XXX directive only allows inline scripts => generate hash of inline script and put it into the directive
    if (value in ['sha256_valid', 'sha256_invalid', 'sha384_valid', 'sha384_invalid', 'sha512_valid', 'sha512_invalid', 'strictdynamic_hash_valid', 'strictdynamic_hash_invalid']):
        formatted_inline_value = format_value(value, request, context, 'contentsecuritypolicytest/stylesrc_inline_stylesheet.css')
        csp_directive = "style-src {value}".format(value=formatted_inline_value)
    else:
        csp_directive = "style-src {value}".format(value=formatted_value)

    response['Content-Security-Policy'] = csp_directive
    response["Link"] = "<{current_origin}/contentsecuritypolicytest/stylesrc_stylesheet/{test_id}/{value}/link_header>; rel=\"stylesheet\", ".format(current_origin=CURRENT_ORIGIN, test_id=test_id, value=value) + "<{external_origin}/contentsecuritypolicytest/stylesrc_stylesheet/{test_id}/{value}/link_header_external>; rel=\"stylesheet\"".format(external_origin=EXTERNAL_ORIGIN, test_id=test_id, value=value)
    return response

def stylesrc_stylesheet(request, test_id, value, element_id):
    context = { 'test_id': test_id, 'value': value, 'element_id': element_id }
    save(test_id, "contentsecuritypolicy_stylesrc_{value}_{element_id}_stylesheet".format(value=value, element_id=element_id), 'request_received')
    # update test result
    save(test_id, "contentsecuritypolicy_stylesrc_{value}_{element_id}_check".format(value=value, element_id=element_id), 'stylesheet_request_received')

    return render(request, 'contentsecuritypolicytest/stylesrc_stylesheet.css', context,
                            content_type="text/css")

def stylesrc_check(request, test_id, value):
    # update test result
    save(test_id, "contentsecuritypolicy_stylesrc_{value}_check".format(value=value), 'check_successful')
    response = HttpResponse('Content-Security-Policy contentsecuritypolicy_stylesrc_check_' + value)
    return response



# ----------------------------------------------------------------------------------------------------------------------
# Test directive: worker-src
# ----------------------------------------------------------------------------------------------------------------------

def workersrc_setup(request, test_id, value):
    formatted_value = format_value(value)
    save(test_id, "contentsecuritypolicy_workersrc_{value}_setup".format(value=value), 'test_setup')

    # compose response
    context = { 'test_id': test_id, 'value': value, 'external_origin': EXTERNAL_ORIGIN, 'current_origin': CURRENT_ORIGIN, "current_domain": CURRENT_DOMAIN, "current_port": CURRENT_PORT, "external_domain": EXTERNAL_DOMAIN, "external_port": EXTERNAL_PORT }
    response = render(request, 'contentsecuritypolicytest/workersrc_setup.html', context)
    response['Content-Security-Policy'] = "worker-src {value}".format(value=formatted_value)
    return response

def workersrc_script(request, test_id, value):
    context = { 'test_id': test_id, 'value': value }
    save(test_id, "contentsecuritypolicy_workersrc_{value}_script".format(value=value), 'request_received')
    # update test result
    save(test_id, "contentsecuritypolicy_workersrc_{value}_check".format(value=value), 'script_request_received')

    return render(request, 'contentsecuritypolicytest/workersrc_script.js', context,
                            content_type="application/x-javascript")


def workersrc_check(request, test_id, value):
    # update test result
    save(test_id, "contentsecuritypolicy_workersrc_{value}_check".format(value=value), 'worker_request_received')

    # return a checkmark image
    response = HttpResponse('Content-Security-Policy contentsecuritypolicy_workersrc_check_' + value)
    return response



# ----------------------------------------------------------------------------------------------------------------------
# Utility functions
# ----------------------------------------------------------------------------------------------------------------------

def format_value(value, request=False, context=False, template_path=False):
    if (value in ["none", "self"]):
        return "'{value}'".format(value=value)

    if (value in ["http", "https", "ws"]):
        return "{value}:".format(value=value)

    if (value == "host_valid"):
        return CURRENT_ORIGIN

    if (value == "host_invalid_domain"):
        return "{scheme}://{domain}:{port}".format(scheme=CURRENT_SCHEME, domain="invalid.invalid", port=CURRENT_PORT)

    if (value == "host_invalid_port"):
        return "{scheme}://{domain}:{port}".format(scheme=CURRENT_SCHEME, domain=CURRENT_DOMAIN, port="8001")

    if (value == "host_invalid_scheme"):
        return "{scheme}://{domain}:{port}".format(scheme="ftp", domain=CURRENT_DOMAIN, port=CURRENT_PORT)

    if (value == "nonce_valid"):
        return "'nonce-validnonce'"

    if (value == "nonce_invalid"):
        return "'nonce-invalidnonce'"

    if (value == "sha256_valid"):
        return "'sha256-" + hash_template(request, context, template_path, "sha256") + "' 'sha-256-" + hash_string("Check successful", "sha256") + "'"

    if (value == "sha256_invalid"):
        return "'sha256-invalidhash'"

    if (value == "sha384_valid"):
        return "'sha384-" + hash_template(request, context, template_path, "sha384") + "'"

    if (value == "sha384_invalid"):
        return "'sha384-invalidhash'"

    if (value == "sha512_valid"):
        return "'sha512-" + hash_template(request, context, template_path, "sha512") + "'"

    if (value == "sha512_invalid"):
        return "'sha512-invalidhash'"

    if (value == "unsafeinline"):
        return "'unsafe-inline'"

    if (value == "unsafeeval"):
        return "'self' 'unsafe-eval' 'unsafe-inline'"

    if (value == "strictdynamic_host"):
        # not allowed since strict-dynamic disabled host-based whitelisting
        return "http://testsuite.invalid 'strict-dynamic'"

    if (value == "strictdynamic_scheme"):
        # not allowed since strict-dynamic disabled host-based whitelisting
        return "ftp: 'strict-dynamic'"

    if (value == "strictdynamic_self"):
        # not allowed since strict-dynamic disabled self-whitelisting
        return "'self' 'strict-dynamic'"

    if (value == "strictdynamic_unsafeinline"):
        # not allowed since strict-dynamic disables unsafe-inline directive
        return "'unsafe-inline' 'strict-dynamic'"

    if (value == "strictdynamic_hash_valid"):
        # allowed since strict-dynamic respects sha256 directive
        return "'sha256-" + hash_template(request, context, template_path, "sha256") + "' 'strict-dynamic'"

    if (value == "strictdynamic_hash_invalid"):
        # not allowed since strict-dynamic respects sha256 directive
        return "'sha256-invalidhash' 'strict-dynamic'"

    if (value == "strictdynamic_nonce_valid"):
        # allowed since strict-dynamic respects nonce directive
        return "'nonce-validnonce' 'strict-dynamic'"

    if (value == "strictdynamic_nonce_invalid"):
        # not allowed since strict-dynamic respects nonce directive
        return "'nonce-invalidnonce' 'strict-dynamic'"

    return value

def hash_template(request, context, template_path, algorithm):
    rendered_template = render_template(request, context, template_path)
    return hash_string(rendered_template, algorithm)

def hash_string(string, algorithm):
    if (algorithm == "sha256"):
        hash = hashlib.sha256(string.encode()).digest()

    if (algorithm == "sha384"):
        hash = hashlib.sha384(string.encode()).digest()

    if (algorithm == "sha512"):
        hash = hashlib.sha512(string.encode()).digest()

    encoded = base64.b64encode(hash)
    return str(encoded, "utf-8")

def render_template(request, context, template_path):
    template = loader.get_template(template_path)
    return template.render(context, request)

