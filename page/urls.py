from django.conf.urls import url
from django.urls import path
from page import views

urlpatterns = [
	url(r'^$', views.HomePageView.as_view()),

	#path('hostname/', views.my_view1,name='my_view_name1'),
	path('pacakageinstall/', views.take_view,name='take_view'),
]
