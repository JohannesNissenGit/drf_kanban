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
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    priority = models.CharField(max_length=255)
    users = models.ManyToManyField(User, related_name='tasks')

    def __str__(self):
        return f"{self.title} ({self.status})"

# class Task(models.Model):
#     class Status(models.TextChoices):
#         TODO = 'todo',
#         IN_PROGRESS = 'in_progress',
#         FEEDBACK = 'feedback',
#         DONE = 'done',
#
#     class Priority(models.TextChoices):
#         LOW = 'low',
#         MED = 'med',
#         HIGH = 'high',
#         URGENT = 'urgent',
#
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     category = models.CharField(max_length=255)
#     status = models.CharField(
#         max_length=255,
#         choices=Status.choices,
#         default=Status.TODO,
#     )
#     priority = models.CharField(
#         max_length=255,
#         choices=Priority.choices,
#         default=Priority.MED,
#     )
#     users = models.ManyToManyField(User, related_name='tasks')
#
#     def __str__(self):
#         return f"{self.title} ({self.Status})"

# endregion