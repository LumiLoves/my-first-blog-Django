from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    # image = models.ImageField()


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


# __str__ : 기본 메서드. 더 상위에 있는 기본 메서드. toString()




