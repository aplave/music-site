from django.conf.urls import patterns, url

from Profile import views

#If you want to change the URL of the polls detail view to something else, 
#perhaps to something like polls/specifics/12/ instead of doing it in the 
#template (or templates) you would change it in polls/urls.py:

urlpatterns = patterns('',
	#ex: /polls/
	url(r'^(?P<pk>\d+)/$',views.ProfileView,name='Profile'),
	url(r'^(?P<pk>\d+)/edit$', views.EditProfileView,name="EditProfile")
	)