from django.conf.urls import url
from . import views         #from . import views in current directory

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process_money/(?P<loc>\w+)', views.process),      #anything that comes after \ is grabbed, referred to by <> variable name
    url(r'^reset$',views.reset)
]
