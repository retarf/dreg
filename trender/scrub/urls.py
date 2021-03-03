from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import api
from . import views

router = DefaultRouter()
router.register('website', api.WebsiteView)


app_name = 'scrub'
urlpatterns = [
    path('pull', api.PullDataView.as_view(), name='pull'),
    path('website/', include(router.urls)),
    path('company/', views.CompanyView.as_view(), name='company'),
    path('data/', views.DataView.as_view(), name='data'),
]
