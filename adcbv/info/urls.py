from django.conf.urls import url
from info import views

app_name = 'info'

urlpatterns = [
        url(r'^$', views.SchoolListView.as_view(), name='list'),
        url(r'^(?P<pk>[-\w]+)/$', views.SchoolDetailView.as_view() , name='detal'),
]
