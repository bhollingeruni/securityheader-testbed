from django.db import models

# Create your models here.
class TestResult(models.Model):
    test_id = models.CharField(max_length=1000)
    result_key = models.CharField(max_length=1000)
    result_value = models.CharField(max_length=1000)

    def __str__(self):
        return self.test_id + " " + self.result_key + "_" + self.result_value