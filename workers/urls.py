from django.conf.urls import url
from . import views


urlpatterns =[

	url(r'^$',views.show, name='show'),
	url(r'^(?P<worker_id>[0-9]+)', views.details, name='details'),
	
	
]

