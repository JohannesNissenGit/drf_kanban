# Generated by Django 5.1.4 on 2024-12-15 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("kanban_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="subtasks",
            field=models.JSONField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name="task",
            name="category",
            field=models.CharField(
                choices=[
                    ("user_story", "User Story"),
                    ("tech_stack", "Tech Stack"),
                    ("support", "Support"),
                    ("infrastructure", "Infrastructure"),
                    ("others", "Others"),
                ],
                default="user_story",
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="task",
            name="priority",
            field=models.CharField(
                choices=[
                    ("low", "Low"),
                    ("med", "Med"),
                    ("high", "High"),
                    ("urgent", "Urgent"),
                ],
                default="med",
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="task",
            name="status",
            field=models.CharField(
                choices=[
                    ("todo", "Todo"),
                    ("in_progress", "In Progress"),
                    ("feedback", "Feedback"),
                    ("done", "Done"),
                ],
                default="todo",
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="task",
            name="users",
            field=models.ManyToManyField(
                blank=True, related_name="tasks", to="kanban_app.user"
            ),
        ),
    ]