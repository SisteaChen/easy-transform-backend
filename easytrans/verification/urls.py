from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^smscode/(?P<mobile>1[3-9]\d{9})/$', views.SMSCodeView.as_view()),
]
