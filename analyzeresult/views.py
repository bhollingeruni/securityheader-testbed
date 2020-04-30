import os
import pprint
from django.shortcuts import render
from django.http import HttpResponse
from saveresult.models import TestResult
from analyzeresult.utils import get_all_testgroups
from analyzeresult.utils import get_all_testdefinitions
from analyzeresult.operators import OPERATOR_EQUALS
from analyzeresult.operators import OPERATOR_NOT_IN_RESULT

DEVICE_MAPPING = {
  "081bfbdb-956d-4565-8100-6d6fd0055db6": "Amazon FireTV Stick (5.1.1)",
  "c26f5245-2eaa-4058-982a-0c6cb79114b4": "Amazon FireTV Stick (7.1.2)",
  "075ec500-a7b5-422b-9ce1-482040d4b9d7": "Kindle 4",
  "4928e1b3-2e09-4fb8-b290-b0aad38b3b09": "Playstation 4",
  "3e7a02ba-8216-40f9-a896-1c5a7b948afc": "Samsung TV 6 Series 55",
  "486e0127-f520-47e6-8bcf-f4c18a5cf345": "Samsung TV GQ49Q6FNGTXZG",
  "1324ae41-c0d1-49de-930f-2ff34686fb53": "Samsung TV UE40F6500",
  "54857ddb-7e7d-4de4-bf84-f8251b709fea": "Samsung TV UE55MU6179U",
  "ad99c498-cba1-4b0b-a164-5ac1e1b4089c": "Samsung TV Unknown model",
  "ca7dc13f-8e9d-47dc-95e6-d3f9d5bada66": "Sony TV KD-65XE9005",
  "2c4c362d-fd12-45fa-bd1f-5d58af39d9fe": "Switch Lite",
  "b815ea88-bb5a-4fbb-bbe2-485a6bf122a5": "UNKNOWN1",
  "96da080e-b1b5-4e75-974d-3746c08f5092": "UNKNOWN2",
}

# Create your views here.
def index(request):
    return HttpResponse("Results index")

def list(request):
    record_set = TestResult.objects.all()
    result_set = preprocess(record_set)

    all_testresults = get_all_testresults(result_set)

    # create result tables grouped by header
    create_tables(all_testresults)

    # create result tables grouped by device
    create_testgroup_table_by_device(result_set)
    create_subtestgroup_tables_by_device(result_set)
    return HttpResponse("List results")

def create_appendix(result_set):
    table_root_path = "/Users/bhollinger/work/code/uni/bachelor/thesis/Tables"

    if (not os.path.exists(table_root_path)):
        os.mkdir(table_root_path)

    filehandle = open("{path}/{filename}.tex".format(path=table_root_path, filename="all_testresults"), "w")
    filebuffer = []

    for test_id in DEVICE_MAPPING:
        results = result_set[test_id]
        filebuffer = filebuffer + ["\\section{{ {device} }}".format(device=DEVICE_MAPPING[test_id])]

        for result_key in results:
            result_value = results[result_key]
            result_key_string = result_key.replace("_", "\_")
            result_value_string = " ".join(result_value).replace("_", "\_")
            filebuffer = filebuffer + ["{result_key}: {result_value} \\\\".format(result_key=result_key_string, result_value=result_value_string)]

    filehandle.writelines("%s\n" % line for line in filebuffer)
    filehandle.close()


def create_tables(result_set):
    table_root_path = "/Users/bhollinger/work/code/uni/bachelor/thesis/Tables"

    if (not os.path.exists(table_root_path)):
        os.mkdir(table_root_path)

    all_groups_filehandle = open("{path}/{filename}.tex".format(path=table_root_path, filename="all_testgroups"), "w")
    all_groups_filebuffer = ["\\begin{center}\\begin{tabular}{ | p{5cm} | l | l |} \hline Test & Pass (\%) & Fail (\%) \\\\ \hline"]

    for testgroup_result in result_set:
        test_groupname = testgroup_result["testgroup_name"].replace("_", "\_")
        test_group_passed_percent = round(testgroup_result["passed_percent"], 2)
        test_group_failed_percent = round(100 - round(testgroup_result["passed_percent"], 2), 2)

        all_groups_filebuffer = all_groups_filebuffer + ["{test} & {passed} & {failed} \\\\ \hline".format(test=test_groupname, passed=test_group_passed_percent, failed=test_group_failed_percent)]
        test_group_root_path = table_root_path + "/" + testgroup_result["testgroup_name"]

        # create directory for test group
        if (not os.path.exists(test_group_root_path)):
            os.mkdir(test_group_root_path)

        test_subgroup_filehandle = open("{path}/{filename}.tex".format(path=test_group_root_path, filename=testgroup_result["testgroup_name"]), "w")
        test_subgroup_filebuffer = ["\\begin{center}\\begin{tabular}{ | p{12cm} | c | c |} \hline Test & Pass (\%) & Fail (\%) \\\\ \hline"]

        for test_subgroup_result in testgroup_result["subgroup_results"]:
            test_subgroup_name = test_subgroup_result["testsubgroup_name"].replace("_", "\_")
            test_subgroup_passed_percent = round(test_subgroup_result["passed_percent"], 2)
            test_subgroup_failed_percent = round(100 - round(test_subgroup_result["passed_percent"], 2),2)
            # create table file for test subgroup
            test_subgroup_filebuffer = test_subgroup_filebuffer + ["{test} & {passed} & {failed} \\\\ \hline".format(test=test_subgroup_name, passed=test_subgroup_passed_percent, failed=test_subgroup_failed_percent)]

            test_filehandle = open("{path}/{filename}.tex".format(path=test_group_root_path, filename=test_subgroup_result["testsubgroup_name"]), "w")
            test_filebuffer = ["\\begin{center}\\begin{tabular}{ | p{9cm} | c | c | c | p{5cm} |} \hline Test & Pass (\%) & Fail (\%) & Total & Passed & Failed \\\\ \hline"]

            for test_result in test_subgroup_result["test_results"]:

                test_name = test_result["test_name"].replace("_", "\_")
                test_passed_percent = round(test_result["passed_percent"], 2)
                test_failed_percent = round(100 - round(test_result["passed_percent"], 2),2)
                test_devices_passed = ' \n '.join(map(map_device, test_result["devices_passed"]))
                test_devices_failed = ' \n '.join(map(map_device, test_result["devices_failed"]))
                test_total = test_result["total"]
                test_filebuffer = test_filebuffer + ["\n\n\n{test} & {passed} & {failed} & {total} & \n\n PASSED: {passed_devices} & \n\n FAILED: {failed_devices} \\\\ \hline".format(test=test_name, passed=test_passed_percent, failed=test_failed_percent, total=test_total, passed_devices=test_devices_passed, failed_devices=test_devices_failed)]

            test_filebuffer = test_filebuffer + ["\end{tabular} \end{center}"]
            test_filehandle.writelines("%s\n" % line for line in test_filebuffer)
            test_filehandle.close()

        test_subgroup_filebuffer = test_subgroup_filebuffer + ["\end{tabular} \end{center}"]
        test_subgroup_filehandle.writelines("%s\n" % line for line in test_subgroup_filebuffer)
        test_subgroup_filehandle.close()

    all_groups_filebuffer = all_groups_filebuffer + ["\end{tabular} \end{center}"]
    all_groups_filehandle.writelines("%s\n" % line for line in all_groups_filebuffer)
    all_groups_filehandle.close()


def create_testgroup_table_by_device(result_set):
    table_root_path = "/Users/bhollinger/work/code/uni/bachelor/thesis/Tables/byDevice"

    if (not os.path.exists(table_root_path)):
        os.mkdir(table_root_path)

    # create table: devices -> testgroup
    all_groups_filehandle = open("{path}/{filename}.tex".format(path=table_root_path, filename="all_testgroups"), "w")
    all_groups_filebuffer = ["\\begin{tabular}{ | p{5cm} | l | l | l | l | l | l | l |} \hline & Cookie & CORS & CSP & HSTS & RefPol & XCTO & XFO \\\\ \hline"]

    for test_id in DEVICE_MAPPING:
        result_count = {}
        device = DEVICE_MAPPING[test_id]
        print(device)
        for test_group in get_all_testgroups():
            result_count[test_group] = {
                    "passed": 0,
                    "total": 0,
                    "percent": 0.0
                }
            for test_definition in get_all_testdefinitions():
                if (test_definition["group"] != test_group):
                    continue

                result = result_set[test_id]
                if test_definition["setup"] and test_definition["setup"] not in result:
                    continue

                # workersrc: discard result if workers are not supported
                if result[test_definition["setup"]] in ["worker_register_not_supported", "worker_not_supported"]:
                    continue

                result_count[test_group]["total"] = result_count[test_group]["total"] + 1

                if (len(test_definition["success"]) > 1):
                    if (test_definition["success"]["operator"] == OPERATOR_EQUALS and test_definition["name"] in result and test_definition["success"]["value"] in result[test_definition["name"]]):
                        result_count[test_group]["passed"] = result_count[test_group]["passed"] + 1

                    if (test_definition["success"]["operator"] == OPERATOR_NOT_IN_RESULT and test_definition["name"] not in result):
                        result_count[test_group]["passed"] = result_count[test_group]["passed"] + 1

                if (len(test_definition["fail"]) > 1):
                    if (not (test_definition["fail"]["operator"] == OPERATOR_EQUALS and (test_definition["name"] in result and test_definition["fail"]["value"] in result[test_definition["name"]]))):
                        # fail condition was evaded
                        result_count[test_group]["passed"] = result_count[test_group]["passed"] + 1

            if result_count[test_group]["total"] != 0.0:
                result_count[test_group]["percent"] = round(result_count[test_group]["passed"] / result_count[test_group]["total"] * 100, 2)

        cookie = result_count["cookie"]["percent"]
        cors = result_count["cors"]["percent"]
        csp = result_count["contentsecuritypolicy"]["percent"]
        hsts = result_count["hsts"]["percent"]
        refpol = result_count["referrerpolicy"]["percent"]
        xtco = result_count["xcontenttypeoptions"]["percent"]
        xfo = result_count["xframeoptions"]["percent"]

        all_groups_filebuffer = all_groups_filebuffer + ["{device} & {cookie}\% & {cors}\% & {csp}\% & {hsts}\% & {refpol}\% & {xtco}\% & {xfo}\% \\\\ \hline".format(device=device, cookie=cookie, cors=cors, csp=csp, hsts=hsts, refpol=refpol, xtco=xtco, xfo=xfo)]

    all_groups_filebuffer = all_groups_filebuffer + ["\end{tabular}"]
    all_groups_filehandle.writelines("%s\n" % line for line in all_groups_filebuffer)
    all_groups_filehandle.close()

def create_subtestgroup_tables_by_device(result_set):
    table_root_path = "/Users/bhollinger/work/code/uni/bachelor/thesis/Tables/byDevice"

    if (not os.path.exists(table_root_path)):
        os.mkdir(table_root_path)

    for test_group in get_all_testgroups():
        testgroup_results = {}
        for test_id in DEVICE_MAPPING:
            result_count = {}
            device = DEVICE_MAPPING[test_id]

            for test_subgroup in get_all_testgroups()[test_group]:
                short_name = test_subgroup.replace(test_group + "_", "")

                # lump all defaultsrc subgroups together
                if "defaultsrc" in short_name:
                    short_name = "defaultsrc"

                result_count[test_subgroup] = {
                        "short_name": short_name,
                        "passed": 0,
                        "total": 0,
                        "percent": 0.0
                    }
                for test_definition in get_all_testdefinitions():
                    if (test_definition["subgroup"] != test_subgroup):
                        continue

                    result = result_set[test_id]
                    if test_definition["setup"] and test_definition["setup"] not in result:
                        continue

                    # workersrc: discard result if workers are not supported
                    if result[test_definition["setup"]] in ["worker_register_not_supported", "worker_not_supported"]:
                        continue

                    result_count[test_subgroup]["total"] = result_count[test_subgroup]["total"] + 1

                    if (len(test_definition["success"]) > 1):
                        if (test_definition["success"]["operator"] == OPERATOR_EQUALS and test_definition["name"] in result and test_definition["success"]["value"] in result[test_definition["name"]]):
                            result_count[test_subgroup]["passed"] = result_count[test_subgroup]["passed"] + 1

                        if (test_definition["success"]["operator"] == OPERATOR_NOT_IN_RESULT and test_definition["name"] not in result):
                            result_count[test_subgroup]["passed"] = result_count[test_subgroup]["passed"] + 1

                    if (len(test_definition["fail"]) > 1):
                        if (not (test_definition["fail"]["operator"] == OPERATOR_EQUALS and (test_definition["name"] in result and test_definition["fail"]["value"] in result[test_definition["name"]]))):
                            # fail condition was evaded
                            result_count[test_subgroup]["passed"] = result_count[test_subgroup]["passed"] + 1

                if result_count[test_subgroup]["total"] != 0.0:
                    result_count[test_subgroup]["percent"] = round(result_count[test_subgroup]["passed"] / result_count[test_subgroup]["total"] * 100, 2)

            testgroup_results[test_id] = result_count

        # construct file header
        subgroup_count = len(get_all_testgroups()[test_group])
        alignment_string = " c |"*subgroup_count

        test_group_filehandle = open("{path}/{filename}.tex".format(path=table_root_path, filename=test_group), "w")
        test_group_filebuffer = ["\\begin{tabular}{ | p{5cm} |" + alignment_string + "} \hline"]

        # add header consisting of sub group names
        subgroup_name_line = ""
        for sg in get_all_testgroups()[test_group]:
            short_name = sg.replace(test_group + "_", "")
            short_name = short_name.replace("_", "\_")
            # lump all defaultsrc subgroups together
            if "defaultsrc" in short_name:
                short_name = "defaultsrc"

            subgroup_name_line = subgroup_name_line + "& " + short_name

        test_group_filebuffer = test_group_filebuffer + [subgroup_name_line + " \\\\ \hline"]

        # add one line per device
        for test_id in testgroup_results:
            testgroup_result = testgroup_results[test_id]
            device_line = ""
            first_subgroup = True
            for test_subgroup in get_all_testgroups()[test_group]:
                if first_subgroup:
                    device_line = "{device} & {result_percent}\%".format(device=DEVICE_MAPPING[test_id], result_percent=testgroup_result[test_subgroup]["percent"])
                    first_subgroup = False
                else:
                    device_line = device_line + " & {result_percent}\%".format(result_percent=testgroup_result[test_subgroup]["percent"])

            device_line = [device_line + " \\\\ \hline"]
            test_group_filebuffer = test_group_filebuffer + device_line

        test_group_filebuffer = test_group_filebuffer + ["\end{tabular}"]
        test_group_filehandle.writelines("%s\n" % line for line in test_group_filebuffer)
        test_group_filehandle.close()

def get_testcount(result_set, test_definition):
    testcount = 0
    for result in result_set.values():
        if test_definition["setup"] in result:
            testcount = testcount + 1
    return testcount

def get_all_testresults(result_set):
    all_testresults = []
    for testgroup in get_all_testgroups():
        all_testresults = all_testresults + [get_testgroupresult(result_set, testgroup)]
    return all_testresults

def get_testgroupresult(result_set, group_name):
    result = {
        "testgroup_name": group_name,
        "total": 0,
        "passed_count": 0,
        "passed_percent": 0,
        "setup_missing_count": 0,
        "subgroup_results": []
    }

    test_groups = get_all_testgroups()

    for test_subgroup in test_groups[group_name]:
        subgroup_result = get_testsubgroupresult(result_set, test_subgroup)
        result["total"] = result["total"] + subgroup_result["total"]
        result["passed_count"] = result["passed_count"] + subgroup_result["passed_count"]
        result["setup_missing_count"] = result["setup_missing_count"] + subgroup_result["setup_missing_count"]
        result["subgroup_results"].append(subgroup_result)

    if (result["total"] == 0):
        result["passed_percent"] = 0
    else:
        result["passed_percent"] = result["passed_count"] / result["total"] * 100

    return result

def get_testsubgroupresult(result_set, subgroup_name):
    result = {
        "testsubgroup_name": subgroup_name,
        "total": 0,
        "passed_count": 0,
        "passed_percent": 0,
        "setup_missing_count": 0,
        "test_results": []
    }

    test_definitions = get_all_testdefinitions()
    for test_definition in test_definitions:
        if (test_definition["subgroup"] != subgroup_name):
            continue
        test_result = get_testresult(result_set, test_definition)
        result["total"] = result["total"] + test_result["total"]
        result["passed_count"] = result["passed_count"] + test_result["passed_count"]
        result["setup_missing_count"] = result["setup_missing_count"] + test_result["setup_missing_count"]
        result["test_results"].append(test_result)

    if (result["total"] == 0):
        result["passed_percent"] = 0
    else:
        result["passed_percent"] = result["passed_count"] / result["total"] * 100

    return result


def get_testresult(result_set, test_definition):
    result_count = {
        "test_name": test_definition["name"],
        "total": 0,
        "passed_count": 0,
        "passed_percent": 0,
        "setup_missing_count": 0,
        "worker_not_supported": 0,
        "devices_passed": [],
        "devices_failed": [],
        "devices_setup_missing": [],
        "devices_worker_not_supported": [],
    }

    for test_id in result_set:
        result = result_set[test_id]
        if test_definition["setup"] and test_definition["setup"] not in result:
            result_count["setup_missing_count"] = result_count["setup_missing_count"] + 1
            result_count["devices_setup_missing"].append(test_id)
            continue

        # workersrc: discard result if workers are not supported
        if result[test_definition["setup"]] in ["worker_register_not_supported", "worker_not_supported"]:
            result_count["worker_not_supported"] = result_count["worker_not_supported"] + 1
            result_count["devices_worker_not_supported"].append(test_id)
            continue

        result_count["total"] = result_count["total"] + 1

        if (len(test_definition["success"]) > 1):
            if (test_definition["success"]["operator"] == OPERATOR_EQUALS and test_definition["name"] in result and test_definition["success"]["value"] in result[test_definition["name"]]):
                result_count["passed_count"] = result_count["passed_count"] + 1
                result_count["devices_passed"].append(test_id)

            if (test_definition["success"]["operator"] == OPERATOR_NOT_IN_RESULT and test_definition["name"] not in result):
                result_count["passed_count"] = result_count["passed_count"] + 1
                result_count["devices_passed"].append(test_id)

        if (len(test_definition["fail"]) > 1):
            if (not (test_definition["fail"]["operator"] == OPERATOR_EQUALS and (test_definition["name"] in result and test_definition["fail"]["value"] in result[test_definition["name"]]))):
                # fail condition was evaded
                result_count["passed_count"] = result_count["passed_count"] + 1
                result_count["devices_passed"].append(test_id)

        if test_id not in result_count["devices_passed"]:
            result_count["devices_failed"].append(test_id)

    if (result_count["total"] == 0):
        result_count["passed_percent"] = 0
    else:
        result_count["passed_percent"] = result_count["passed_count"] / result_count["total"] * 100

    return result_count

def print_metadata(record_set, result_set):
    print("Length of record_set: {length}".format(length=record_set.count()))
    result_count = 0
    for result in result_set:
        result_count = result_count + len(result_set[result])
    print("Number of entries in result_set: {length}".format(length=result_count))

# Restructure result set and prune print_groupresultall results that are getting overwritten by later results
def preprocess(record_set):
    result_set = {}
    for record in record_set:
        test_id = record.test_id
        result_key = record.result_key
        result_value = record.result_value
        if not test_id in result_set:
            print("Creating new test result: " + test_id)
            result_set[test_id] = {}

        if not result_key in result_set[test_id]:
            result_set[test_id][result_key] = []

        if "device" == result_key:
            result_value = "unknown" if result_value == "" else result_value

        # implement exceptions for some tests
        # CORS: check for resource received or not when checking client-side
        if "cors_complex_credentials" in result_key:
            if (result_value in ["resource_received", "resource_not_received"]):
                result_set[test_id][result_key].append(result_value)
            else:
                continue

        # CORS: only check for correct auth header when testing credential server-side
        if "cors_credentials" in result_key:
            if (result_value in ["auth_header_correct_value", "auth_header_not_set"]):
                result_set[test_id][result_key].append(result_value)
            else:
                continue

        # CORS: check for resource received or not when checking allow-headers client-side
        if "cors_complex_allowheaders" in result_key:
            if (result_value in ["resource_received", "resource_not_received"]):
                result_set[test_id][result_key].append(result_value)
            else:
                continue

        # CORS: only check for correct custom header when testing allow-headers server-side
        if "cors_allowheaders_valid_complex" in result_key:
            if (result_value in ["requesttestheader_header_correct_value", "requesttestheader_header_not_set"]):
                print(test_id)
                result_set[test_id][result_key].append(result_value)
            else:
                result_set[test_id][result_key] = ["unknown_result"]
                continue

        # CORS: only check for correct custom header when testing allow-headers server-side
        if "cors_allowheaders_invalid_complex" in result_key:
            if (result_value in ["requesttestheader_header_correct_value", "requesttestheader_header_not_set"]):
                print(test_id)
                result_set[test_id][result_key].append(result_value)
            else:
                result_set[test_id][result_key] = ["unknown_result"]
                continue

        # CORS: discard "resource_received" result in case we are testing for exposed headers in CORS tests
        if "exposeheader" in result_key:
            if (result_value in ["header_accessed", "header_not_accessed"]):
                result_set[test_id][result_key].append(result_value)
            else:
                continue

        # X-Frame-Options: discard all but the last result entry to prevent counting user misclicks
        if "xframeoptions" in result_key:
            result_set[test_id][result_key] = [result_value]
            continue

        result_set[test_id][result_key].append(result_value)

    return result_set

def print_testgroupresult(testgroup_result):

    print("\t\n-----------------------------------------------------------------------------")
    print("\tResults for group " + testgroup_result["testgroup_name"])
    print("\tNumber of tests: {test_count}".format(test_count=testgroup_result["total"]))
    print("\tNumber of passed tests: {test_count}".format(test_count=testgroup_result["passed_count"]))
    print("\tPercent of passed tests: {test_count}".format(test_count=testgroup_result["passed_percent"]))
    print("\tNumber of missing setups: {test_count}".format(test_count=testgroup_result["setup_missing_count"]))

    for testsubgroup_result in testgroup_result["subgroup_results"]:
        print_testsubgroupresult(testsubgroup_result)

    return

def print_testsubgroupresult(testsubgroup_result):

    print("\t\t\n-----------------------------------------------------------------------------")
    print("\t\tResults for subgroup " + testsubgroup_result["testsubgroup_name"])
    print("\t\tNumber of tests: {test_count}".format(test_count=testsubgroup_result["total"]))
    print("\t\tNumber of passed tests: {test_count}".format(test_count=testsubgroup_result["passed_count"]))
    print("\t\tPercent of passed tests: {test_count}".format(test_count=testsubgroup_result["passed_percent"]))
    print("\t\tNumber of missing setups: {test_count}".format(test_count=testsubgroup_result["setup_missing_count"]))

    for test_result in testsubgroup_result["test_results"]:
        print_testresult(test_result)

    return

def print_testresult(test_result):

    print("\t\t\t\n-----------------------------------------------------------------------------")
    print("\t\t\tResults for test " + test_result["test_name"])
    print("\t\t\tNumber of tests: {test_count}".format(test_count=test_result["total"]))
    print("\t\t\tNumber of passed tests: {test_count}".format(test_count=test_result["passed_count"]))
    print("\t\t\tPercent of passed tests: {test_count}".format(test_count=test_result["passed_percent"]))
    print("\t\t\tNumber of missing setups: {test_count}".format(test_count=test_result["setup_missing_count"]))
    print("\t\t\tNumber of unsupported workers: {test_count}".format(test_count=test_result["worker_not_supported"]))

    return

def map_device(test_id):
    return DEVICE_MAPPING[test_id]