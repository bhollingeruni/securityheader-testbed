from django.shortcuts import render
from saveresult.models import TestResult
from saveresult.utils import save
from testsuite.settings import SUBDOMAIN_ORIGIN
from testsuite.settings import CURRENT_ORIGIN
from testsuite.settings import CURRENT_SECURE_ORIGIN
from testsuite.settings import EXTERNAL_ORIGIN
from testsuite.settings import EXTERNAL_SECURE_ORIGIN
from django.shortcuts import redirect
from datetime import datetime

import uuid

def index(request):
    test_id = uuid.uuid4()
    context = {
        'test_id': test_id
    }

    # redirect to HTTP to avoid browsers blocking some test frames due to mixed content
    if request.is_secure():
        return redirect(CURRENT_ORIGIN)

    response = render(request, 'browsertest/index.html', context)

    return response

def test(request, test_id, test_type):
    if request.POST.get("device"):
        save(test_id, "device", request.POST.get("device"))

    if request.POST.get("notes"):
        save(test_id, "notes", request.POST.get("notes"))

    if request.POST.get("usage"):
        save(test_id, "usage", request.POST.get("usage"))

    save(test_id, "user_agent", request.META.get("HTTP_USER_AGENT"))

    # save current timestamp
    now = datetime.now()
    save(test_id, "timestamp", now.strftime("%Y-%m-%d %H:%M:%S"))

    test_templates = {
        "cookie": "browsertest/cookie.html",
        "xcontenttypeoptions": "browsertest/xcontenttypeoptions.html",
        "xframeoptions": "browsertest/xframeoptions.html",
        "referrerpolicy": "browsertest/referrerpolicy.html",
        "cors": "browsertest/cors.html",
        "hsts": "browsertest/hsts.html",
        "contentsecuritypolicy_connectsrc": "browsertest/contentsecuritypolicy_connectsrc.html",
        "contentsecuritypolicy_defaultsrc": "browsertest/contentsecuritypolicy_defaultsrc.html",
        "contentsecuritypolicy_frameancestors": "browsertest/contentsecuritypolicy_frameancestors.html",
        "contentsecuritypolicy_framesrc": "browsertest/contentsecuritypolicy_framesrc.html",
        "contentsecuritypolicy_imgsrc": "browsertest/contentsecuritypolicy_imgsrc.html",
        "contentsecuritypolicy_scriptsrc": "browsertest/contentsecuritypolicy_scriptsrc.html",
        "contentsecuritypolicy_stylesrc": "browsertest/contentsecuritypolicy_stylesrc.html",
        "contentsecuritypolicy_workersrc": "browsertest/contentsecuritypolicy_workersrc.html"
    }

    context = {
        'test_id': test_id,
        'subdomain_origin': SUBDOMAIN_ORIGIN,
        'current_origin': CURRENT_ORIGIN,
        'current_secure_origin': CURRENT_SECURE_ORIGIN,
        'external_origin': EXTERNAL_ORIGIN,
        'external_secure_origin': EXTERNAL_SECURE_ORIGIN
    }

    response = render(request, test_templates[test_type], context)

    return response