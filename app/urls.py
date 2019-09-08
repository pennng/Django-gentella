from django.urls import path, re_path
from app import views

urlpatterns = [
    # Matches any html file - to be used for gentella
    # Avoid using your .html in your resources.
    # Or create a separate django app.
    re_path(r'^.*\.html', views.gentella_html, name='index'),

    # The home page
    path('', views.index, name='index'),
    path('outliers', views.outliers, name='outliers'),
    path('data_fresh', views.data_fresh, name="data_fresh"),
    path('data_fresh\\', views.data_fresh, name="data_fresh"),
    path('data_fresh/', views.data_fresh, name="data_fresh"),
    path('data_fresh_tem_table', views.data_table_tem_fresh_with_pred, name='data_table_tem_fresh'),
    path('data_live_tem', views.live_tem, name='data_live_tem'),
]

