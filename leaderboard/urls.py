from django.conf.urls import url
from . import views

app_name = 'leaderboard'



urlpatterns = [
    # /brand/
    url(r'^$', views.index, name='index'),

    # /brand/squad12v12/
    url(r'^squad12v12/$', views.leaderboard_12v12, name='leaderboard-12v12'),

    # /brand/squad12v12/<pk>
    url(r'^squad12v12/(?P<pk>[0-9]+)/$', views.detail_12v12, name='detail-12v12'),

    # /brand/squad/12v12teams/add
    #url(r'^squad/12v12teams/add/$', views.Team12v12Create.as_view(), name='team-12v12-add'),
    url(r'^squad/12v12teams/add/$', views.Team12v12Create, name='team-12v12-add'),

    # /brand/squad/12v12teams/<pk>
    url(r'^squad/12v12teams/(?P<pk>[0-9]+)/$', views.Team12v12Update.as_view(), name='team-12v12-update'),

    # /brand/squad/12v12teams/<pk>/delete
    url(r'^squad/12v12teams/(?P<pk>[0-9]+)/delete/$', views.Team12v12Delete.as_view(), name='team-12v12-delete'),

    # User registration form
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
]