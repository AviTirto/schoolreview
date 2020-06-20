from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from model_utils.models import TimeStampedModel

class Profile(models.Model):
    GENDER_FIELD = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length = 1, choices = GENDER_FIELD)
    address = models.CharField(max_length = 30)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

class School(models.Model):
    name = models.CharField(max_length = 50)
    description = models.TextField(max_length = 2000)
    address = models.CharField(max_length = 100)
    city = models.CharField(max_length = 50)
    latitude = models.DecimalField(decimal_places = 3, max_digits = 5)
    longitude = models.DecimalField(decimal_places = 3, max_digits = 5)
    public = models.BooleanField()
    students = models.IntegerField()
    rating = models.DecimalField(decimal_places = 3, max_digits = 5)
    image = models.ImageField(upload_to='images/')

class Comment(models.Model):
    content = models.TextField()
    rating = models.IntegerField()
    school = models.ForeignKey(School, on_delete = models.CASCADE, related_name = "comments")
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name="comments")
    email = models.EmailField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
