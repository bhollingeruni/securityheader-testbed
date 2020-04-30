import logging
from saveresult.models import TestResult

def save(test_id, result_key, result_value):
    save_to_log(test_id, result_key, result_value)
    save_to_db(test_id, result_key, result_value)

# alias for save() to prevent some import confusion
def save_entry(test_id, result_key, result_value):
    save(test_id, result_key, result_value)

def save_to_log(test_id, result_key, result_value):
    logger = logging.getLogger('testsuite')
    logger.info('%s|%s|%s', test_id, result_key, result_value)

def save_to_db(test_id, result_key, result_value):
    record = TestResult(test_id=test_id, result_key=result_key, result_value=result_value)
    record.save()