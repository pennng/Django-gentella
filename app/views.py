from django.http import HttpResponse, JsonResponse
from django.template import loader

from app import models
import time


def test_index(request):
    context = models.get_current_info()
    template = loader.get_template('app/test.html')
    return HttpResponse(template.render(context, request))


def index(request):
    context = models.get_current_info()
    template = loader.get_template('app/index.html')
    return HttpResponse(template.render(context, request))


def data_fresh(request):
    context = models.get_current_info()
    return JsonResponse(context)


def data_table_tem_fresh(request):
    n = 100
    date_time, value = models.get_recent_n_records(n)
    context = {
        'date': date_time,
        'value': value,
    }
    return JsonResponse(context)


def data_table_tem_fresh_with_pred(request):
    n = 100
    n = int(request.GET.get("pred_szie"))
    m = 20
    date_time, value, pred_date_time, pred_value, pred_m_date, pred_m_value = models.get_pred_and_record(n, m)
    context = {
        'date': date_time,
        'value': value,
        'pred_date': pred_date_time,
        'pred_value': pred_value,
        # 'pred_m_date': pred_m_date,
        # 'pred_m_value': pred_m_value,
        'min': int(min(value+pred_value+pred_m_value) - 2),
        'max': int(max(value+pred_value+pred_m_value) + 2)
    }
    return JsonResponse(context)


def outliers(request):
    context = models.get_outliers_info()
    return JsonResponse(context)


def live_tem(request):
    n = 600
    context = models.get_live_data(n)
    return JsonResponse(context)


def gentella_html(request):
    context = {}
    # The template to be loaded as per gentelella.
    # All resource paths for gentelella end in .html.

    # Pick out the html file name from the url. And load that template.
    load_template = request.path.split('/')[-1]
    template = loader.get_template('app/' + load_template)
    return HttpResponse(template.render(context, request))
