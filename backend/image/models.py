from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
    file_content = models.FileField(upload_to='media/')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="images")
    filter_type = models.Charfield(max_length=30, default="normal")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name