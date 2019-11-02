from django.conf.urls import url
from .import views 

urlpatterns = [
	url('us_stocks', views.index,name="us_stocks"),
	url('india_stocks', views.index1,name="india_stocks"),
	url('crypto_stocks', views.index2,name="crypto_stocks"),
	url('stocks/', views.stocks),
    ]