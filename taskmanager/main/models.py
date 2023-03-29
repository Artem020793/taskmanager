from django.db import models

class Task(models.Model):
    title = models.CharField('Name', max_length=50)
    task = models.TextField('Text', max_length=255)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
