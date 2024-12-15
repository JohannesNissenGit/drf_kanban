import json

from django.db import models


# Create your models here.

# region users
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"


# endregion

# region tasks
class Task(models.Model):
    class Status(models.TextChoices):
        TODO = 'todo',
        IN_PROGRESS = 'in_progress',
        FEEDBACK = 'feedback',
        DONE = 'done',

    class Priority(models.TextChoices):
        LOW = 'low',
        MED = 'med',
        HIGH = 'high',
        URGENT = 'urgent',

    class Category(models.TextChoices):
        USER_STORY = 'user_story',
        TECH_STACK = 'tech_stack',
        SUPPORT = 'support',
        INFRASTRUCTURE = 'infrastructure',
        OTHERS = 'others',

    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(
        max_length=255,
        choices=Category.choices,
        default=Category.USER_STORY,
    )
    status = models.CharField(
        max_length=255,
        choices=Status.choices,
        default=Status.TODO,
    )
    priority = models.CharField(
        max_length=255,
        choices=Priority.choices,
        default=Priority.MED,
    )
    users = models.ManyToManyField(User, related_name='tasks', blank=True)
    subtasks = models.JSONField(default=None, blank=True, null=True)

    # the following functions convert the json from JSONField into a list and back when getting and retrieving the subtasks
    def set_subtasks(self, x):
        self.subtasks = json.dumps(x)

    def get_subtasks(self):
        return json.loads(self.subtasks)

    def __str__(self):
        return f"{self.title} ({self.Status})"
# endregion
