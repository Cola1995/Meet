from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser


class UserInfo(AbstractUser):
    tel = models.CharField(max_length=32)

class Room(models.Model):
    """
    会议室表
    """
    caption = models.CharField(max_length=32)
    num = models.IntegerField()  # 容纳人数
    def __str__(self):
        return self.caption


class Book(models.Model):
    """
    会议室预定信息

    """
    user = models.ForeignKey('UserInfo')
    room = models.ForeignKey('Room')
    date = models.DateField()
    time_choices = (
        (1, '8:00'),
        (2, '9:00'),
        (3, '10:00'),
        (4, '11:00'),
        (5, '12:00'),
        (6, '13:00'),
        (7, '14:00'),
        (8, '15:00'),
        (9, '16:00'),
        (10, '17:00'),
        (11, '18:00'),
        (12, '19:00'),
        (13, '20:00'),
    )


    time_id = models.IntegerField(choices=time_choices)

    class Meta:
        unique_together = (
            ('room','date','time_id'),
        )


    def __str__(self):
        return str(self.user)+"预定了"+str(self.room)
