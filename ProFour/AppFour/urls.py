from django.conf.urls import url
from AppFour import views
from django.urls import path
urlpatterns=[
url(r'^$',views.index,name='index')
]
