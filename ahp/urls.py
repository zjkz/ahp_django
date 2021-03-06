from django.conf.urls import patterns, url

from ahp import views

from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    url(r'^common_hierarchy/$', login_required(views.common_hierarchy), name='common_hierarchy'),
    url(r'^level/$', login_required(views.level), name='level'),
    url(r'^node/$', login_required(views.node), name='node'),
    url(r'^groups_list/$', login_required(views.groups_list), name='groups_list'),
    url(r'^group/$', login_required(views.group), name='group'),
    url(r'^group_nodes_list/$', login_required(views.group_nodes_list), name='group_nodes_list'),
    url(r'^group_nodes/$', login_required(views.group_nodes), name='group_nodes'),
    url(r'^chosen_group_nodes/$', login_required(views.chosen_group_nodes), name='chosen_group_nodes'),
    url(r'^question/$', login_required(views.question), name='question'),
    url(r'^group_question_list/$', login_required(views.group_question_list), name='group_question_list'),
    url(r'^users_list/$', login_required(views.users_list), name='users_list'),
    url(r'^user/$', login_required(views.user), name='user'),
    url(r'^questions/$', login_required(views.questions), name='questions'),
    url(r'^email/$', login_required(views.email), name='email'),
    url(r'^chosen_group_nodes_for_comparison/$', login_required(views.chosen_group_nodes_for_comparison), name='chosen_group_nodes_for_comparison'),
    url(r'^user_confidence_list/$', login_required(views.user_confidence_list), name='user_confidence_list'),
    url(r'^global_priority/$', login_required(views.global_priority_calculation), name='global_priority_calculation'),
    url(r'^alt_type/$', login_required(views.alt_type), name='alt_type'),
    url(r'^save_absolute_value/$', login_required(views.save_absolute_value), name='save_absolute_value'),

    url(r'^popup/$', login_required(views.popup), name='popup'),
    url(r'^group_questions.html/$', login_required(views.group_questions), name='group_questions'),
    url(r'^hierarchy.html/$', login_required(views.hierarchy), name='hierarchy'),
    url(r'^group_template.html/$', login_required(views.group_template), name='group_template'),
    url(r'^votes.html/$', login_required(views.votes), name='votes'),
    url(r'^priority.html/$', login_required(views.priority), name='priority'),

    url(r'^hierarchy_graph/$', login_required(views.hierarchy_graph), name='hierarchy_graph'),
    url(r'^groups_votes/$', login_required(views.groups_votes), name='groups_votes'),
    url(r'^users_answer_hierarchy/$', login_required(views.users_answer_hierarchy), name='users_answer_hierarchy'),
    url(r'^users_answer_comparison/$', login_required(views.users_answer_comparison), name='users_answer_comparison'),


    #url(r'^projects/$', login_required(views.projects), name='projects'),
    url(r'^projects/$', login_required(views.projects), name='projects'),
    url(r'^$', login_required(views.main), name='main'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'ahp/login.html'}),

    url(r'^hierarchy/(?P<hash_user_id>\w+)/$', views.form_for_participant, name='form_for_participant'),
    url(r'^comparison/(?P<hash_user_id>\w+)/$', views.form_for_comparison, name='form_for_comparison'),
)

