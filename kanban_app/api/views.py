from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response

from kanban_app.api.serializers import TaskSerializer, UserSerializer
from kanban_app.models import Task, User


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TasksViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskOfUserView(generics.ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        user_id = self.kwargs['pk']
        return Task.objects.filter(users__id=user_id)


class UserOfTaskView(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        task_id = self.kwargs['pk']
        return User.objects.filter(tasks__id=task_id)


class SummaryView(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()

    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        tasks = Task.objects.all()
        done_tasks = Task.objects.filter(status='done')
        todo_tasks = Task.objects.filter(status='todo')
        in_progress_tasks = Task.objects.filter(status='in_progress')
        feedback_tasks = Task.objects.filter(status='feedback')
        urgent_priority_tasks = Task.objects.filter(priority='urgent')

        return Response({
            'total_users': users.count(),
            'total_tasks': tasks.count(),
            'total_done_tasks': done_tasks.count(),
            'total_todo_tasks': todo_tasks.count(),
            'total_in_progress_tasks': in_progress_tasks.count(),
            'total_feedback_tasks': feedback_tasks.count(),
            'total_urgent_priority_tasks': urgent_priority_tasks.count()
        })
