from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = format_suffix_patterns(
    [
        # TOKEN AUTHENTIFICATION
        url(
            r'^token-auth$',
            views.ObtainAuthToken.as_view(),
            name='token_api'
        ),
        # PROJECTS
        url(
            r'^projects$',
            views.ProjectListCreate.as_view(),
            name='projects'
        ),
        url(
            r'^projects/(?P<pk>\d+)$',
            views.ProjectRetrieveUpdateDestroy.as_view(),
            name='projects_detail'
        ),
        url(
            r'^projects/(?P<pk>\d+)/access$',
            views.ProjectAccessList.as_view(),
            name='projects_access_list'
        ),
        url(
            r'^projects/(?P<pk>\d+)/tasks$',
            views.ProjectTaskList.as_view(),
            name='projects_tasks_list'
        ),
        # ACCESS
        url(
            r'^access$',
            views.AccessListCreate.as_view(),
            name='access'
        ),
        url(
            r'^access/(?P<pk>\d+)$',
            views.AccessRetrieveUpdateDestroy.as_view(),
            name='access_detail'
        ),
        # TASKS
        url(
            r'^tasks$',
            views.TaskListCreate.as_view(),
            name='tasks'
        ),
        url(
            r'^tasks/(?P<pk>\d+)$',
            views.TaskRetrieveUpdateDestroy.as_view(),
            name='tasks_detail'
        ),
        # Label
        url(
            r'^labels$',
            views.LabelListCreate.as_view(),
            name='labels'
        ),
        url(
            r'^labels/(?P<pk>\d+)$',
            views.LabelRetrieveUpdateDestroy.as_view(),
            name='labels_detail'
        ),
        # File
        url(
            r'^files$',
            views.FileListCreate.as_view(),
            name='files'
        ),
        url(
            r'^files/(?P<pk>\d+)$',
            views.FileRetrieveUpdateDestroy.as_view(),
            name='files_detail'
        ),
        # Comment
        url(
            r'^comments$',
            views.CommentListCreate.as_view(),
            name='comments'
        ),
        url(
            r'^comments/(?P<pk>\d+)$',
            views.CommentRetrieveUpdateDestroy.as_view(),
            name='comments_detail'
        ),
        # Kanboard
        url(
            r'^kanboards$',
            views.KanboardListCreate.as_view(),
            name='kanboards'
        ),
        url(
            r'^kanboards/(?P<pk>\d+)$',
            views.KanboardRetrieveUpdateDestroy.as_view(),
            name='kanboards_detail'
        ),
        # DOCUMENTATION SWAGGER
        url(
            r'^documentation/',
            include('rest_framework_docs.urls')
        ),
     ]
)
