from django.db import models




class CustUser(models.Model):
    username = models.CharField(max_length=100, unique=True, null=False)

    def save(self, *args, **kwargs):
        created = not self.pk
        super().save(*args, **kwargs)
        if created:
            Task.objects.create(
            title = 'Welcome to Taks Tracker',
            description = 'You can create new task, edit or delete existing ones !',
            status = 'completed',
            due_date = '1999-01-01', user=self
        )


class Task(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('in progress', 'In Progress'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    due_date = models.DateField()
    user = models.ForeignKey(CustUser, null=True, on_delete=models.CASCADE,)

    # Add a foreign key to the User model

    @classmethod
    def get_default_pk(cls):
        task, created = cls.objects.get_or_create(
            title = 'Welcome to Taks Tracker',
            description = 'You can create new task, edit or delete existing ones !',
            status = 'completed',
            due_date = '1999-01-01',
        )
        return task.pk

    def __str__(self):
        return self.title
    
