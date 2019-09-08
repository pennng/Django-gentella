from __future__ import unicode_literals

import time
from datetime import datetime
import gentelella.settings as ENV

import pymongo
import numpy as np
# Create your models here.
from matplotlib import pyplot

_database_name = 'mydb'

db_client = pymongo.MongoClient(ENV.DB_URL, port=27018)

mydb = db_client.get_database(_database_name)
sensor = mydb.get_collection('middle2')
pred = mydb.get_collection('middle')
org = mydb.get_collection('sensor3')


def get_current_info():
    record = sensor.find_one(limit=1, sort=[('time', -1)])
    res = {}
    if record:
        res['tem'] = record.get('tem')
        res['time'] = record.get('time')
    return res


def get_outliers_info():
    mu = 19.20
    std = 2.85
    control = 1

    res = {}

    return res


def get_recent_n_records(n):
    record = sensor.find(limit=n, sort=[('_id', -1)])
    data_value = []
    date_time = []
    for item in record:
        date_time.append(item.get('time'))
        data_value.append(item.get('tem'))
    return date_time, data_value


def get_pred_and_record(n, m):
    a = time.time()
    record = pred.find(limit=n + m, sort=[('_id', -1)])
    _time = []
    data_value = []
    date_time = []
    pred_value = []

    for item in record:
        date_time.append(item.get('time').timestamp())
        data_value.append(item.get('tem'))
        pred_value.append(item.get("pred_value"))

    pred_value = np.array(pred_value)
    date_time = date_time[:n - 1]
    data_value = data_value[:n - 1]
    pred_future = pred_value[0].tolist()[:m]
    pred_future_date = []
    for i in range(m):
        pred_future_date.append(date_time[0] + (i + 1) * 900)

    pred_future.reverse()
    pred_future_date.reverse()

    pred_his_1 = pred_value[1: n+1, 0].tolist()
    pred_his_m = pred_value[0: n + m, m-1].tolist()

    pred_future_1 = pred_future + pred_his_1
    pred_future_m = pred_his_m

    pred_future_date_1 = pred_future_date + date_time
    pred_future_date_m = pred_future_date + date_time
    b = time.time() - a

    return date_time, data_value, pred_future_date_1, pred_future_1, pred_future_date_m, pred_future_m


def list_to_datetime(list: list):
    res = []
    for i in list:
        res.append(datetime.fromtimestamp(i))
    return res


def get_live_data(n):
    records = org.find(limit=n, sort=[('_id', -1)])
    res = {
        's1': [],
        's2': [],
        's3': [],
        'time': [],
        'cleand': [],
        'min': 0,
        'max': 0,
    }
    for item in records:
        res['s1'].append(item.get('tem_1'))
        res['s2'].append(item.get('tem_2'))
        res['s3'].append(item.get('tem_3'))
        res['time'].append(item.get('time').timestamp())
        res['cleand'].append(item.get('clean'))

    res['min'] = int(min(res['s1']+res['s2']+res['s3']+res['cleand'])) - 2
    res['max'] = int(max(res['s1']+res['s2']+res['s3']+res['cleand'])) + 2
    return res
