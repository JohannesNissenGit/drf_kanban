from django.urls import path, include
from rest_framework import routers

from kanban_app.api.views import UsersViewSet, TasksViewSet, SummaryView, TaskOfUserView, UserOfTaskView

router = routers.SimpleRouter()
router.register(r'users', UsersViewSet, basename='user')
router.register(r'tasks', TasksViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls)),
    path("users/<int:pk>/tasks/", TaskOfUserView.as_view(), name='tasks_of_user'),
    path("tasks/<int:pk>/users/", UserOfTaskView.as_view(), name='users_of_task'),
    path('summary/', SummaryView.as_view(), name='summary'),
]