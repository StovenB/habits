from django.db import models


class Habit(models.Model):
    habit_text = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date started')
    task_completed = models.IntegerField(default=0)

    def __str__(self):
        return self.habit_text
