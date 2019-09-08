from django.test import TestCase

# Create your tests here.
from . import models
from . import views
from datetime import datetime


class TestModel(TestCase):
    def test_get_recent_n_records(self):
        n = 10
        time, value = models.get_recent_n_records(10)

    def test_get_pred_and_record(self):
        n = 10
        m = 5
        date_time, data_value, pred_future_date_1, pred_future_1, pred_future_date_m, pred_future_m = models.get_pred_and_record(n, m)
