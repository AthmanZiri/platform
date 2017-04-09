from django.conf.urls import url
from .views import milestone_list, milestone_create

urlpatterns = [
	url(r'^$', milestone_list, name='milestone_list'),

	url(r'^create/', milestone_create, name='milestone_create')
]