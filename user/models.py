from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class MyApp(models.Model):
    id = models.AutoField(primary_key=True)  # Auto-incrementing primary key
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # ForeignKey to the User model
    app_name = models.CharField(max_length=100)  # App name field
    points = models.IntegerField(default=1)  # Points field
    img = models.ImageField(upload_to='img')  # Image field
    created_at = models.DateTimeField(default=timezone.now, editable=False)  # Timestamp field

    def __str__(self):
        return f"{self.app_name} ({self.user.username})"
