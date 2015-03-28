from django.conf.urls import patterns, url

from ahp import views

urlpatterns = patterns('',
    url(r'^common_hierarchy/$', views.common_hierarchy, name='common_hierarchy'),
    url(r'^level/$', views.level, name='level'),
    url(r'^node/$', views.node, name='node'),
    url(r'^groups_list/$', views.groups_list, name='groups_list'),
    url(r'^group/$', views.group, name='group'),
    url(r'^group_nodes_list/$', views.group_nodes_list, name='group_nodes_list'),
    url(r'^group_nodes/$', views.group_nodes, name='group_nodes'),
    url(r'^question/$', views.question, name='question'),
    url(r'^group_question_list/$', views.group_question_list, name='group_question_list'),
    url(r'^users_list/$', views.users_list, name='users_list'),
    url(r'^user/$', views.user, name='user'),

    url(r'^$', views.index, name='index'),
    url(r'^(?P<user_id>\d+)/$', views.user_hierarchy, name='user_hierarchy'),
)