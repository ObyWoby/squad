from django.conf.urls import url
from . import views

app_name = 'leaderboard'

#I think that the update and delete generic view functions didn't work because my url structure is different to
# the tutorial. I need to rethink the current structure and redesign it silimar to the tuturial, and in such a
# way as enable the site to expand easily to include the other leaderboards as well as SkrimZ (think about the url
# for the index page etc). Perhaps rename leaderboards to a brand name? Maybe temporarily enter 'brand'?


urlpatterns = [
    # /brand/
    # /leaderboards/
    url(r'^$', views.index, name='index'),

    # /brand/squad12v12/
    url(r'^squad12v12/$', views.leaderboard_12v12, name='leaderboard-12v12'),
    # /leaderboards/12v12/
    # url(r'^12v12/$', views.leaderboard_12v12, name='leaderboard-12v12'),

    # /brand/squad12v12/<pk>
    url(r'^squad12v12/(?P<pk>[0-9]+)/$', views.detail_12v12, name='detail-12v12'),
    # /leaderboards/12v12/1
    # url(r'^12v12/(?P<team12v12_id>[0-9]+)/$', views.detail_12v12, name='detail-12v12'),

    # /brand/squad/12v12teams/add
    #url(r'^squad/12v12teams/add/$', views.Team12v12Create.as_view(), name='team-12v12-add'),
    url(r'^squad/12v12teams/add/$', views.Team12v12Create, name='team-12v12-add'),
    # /leaderboards/12v12/add
    # url(r'^12v12/add/$', views.Team12v12Create.as_view(), name='team-12v12-add'),

    # /brand/squad/12v12teams/<pk>
    url(r'^squad/12v12teams/(?P<pk>[0-9]+)/$', views.Team12v12Update.as_view(), name='team-12v12-update'),
    # /leaderboards/12v12/PK/update
    # url(r'^12v12/(?P<team12v12_id>[0-9]+)/update/$', views.Team12v12Update.as_view(), name='team-12v12-update'),

    # /brand/squad/12v12teams/<pk>/delete
    url(r'^squad/12v12teams/(?P<pk>[0-9]+)/delete/$', views.Team12v12Delete.as_view(), name='team-12v12-delete'),
    # /leaderboards/12v12/PK/delete
    # url(r'^12v12/(?P<team12v12_id>[0-9]+)/delete/$', views.Team12v12Delete.as_view(), name='team-12v12-delete'),

    # User registration form
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
]