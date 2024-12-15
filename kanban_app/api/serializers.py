from rest_framework import serializers

from kanban_app.models import User, Task


class UserSerializer(serializers.ModelSerializer):

    tasks = serializers.StringRelatedField(many=True, read_only=True, source='task-detail')

    class Meta:
        model = User
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField(many=True, read_only=True, source='user-detail')

    class Meta:
        model = Task
        fields = '__all__'

class TaskOfUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        exclude = ['user']

class UserOfTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['tasks']