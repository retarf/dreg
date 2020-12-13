from django.urls import path

from . import api

urlpatterns = [
    path('pull', api.PullDataView.as_view(), name='pull'),
]
