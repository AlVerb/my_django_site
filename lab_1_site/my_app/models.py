from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200)                   #заголовок статьи.
    text = models.TextField()                                  #текст статьи
    created_date = models.DateTimeField(
        default=timezone.now)                                  #дата создания
    file = models.FileField(upload_to="uploads/", null=True)   #Вложение


def chTitle(self, new_title):
    self.title = new_title
    self.save()

def chText(self, new_text):
    self.title = new_text
    self.save()

def __str__(self):
    return self.title

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)
