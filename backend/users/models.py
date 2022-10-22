from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pfp_url = models.CharField(max_length=500,
                               default="https://variety.com/wp-content/uploads/2021/07/Rick-Astley-Never-Gonna-Give-You-Up.png?w=681&h=383&crop=1")  # Rick Astley image as default

    runs = models.IntegerField(default=0)
    balls = models.IntegerField(default=0)
    matches = models.IntegerField(default=0)
    innings = models.IntegerField(default=0)
    batting_innings = models.IntegerField(default=0)
    bowling_innings = models.IntegerField(default=0)
    wickets = models.IntegerField(default=0)
    overs = models.IntegerField(default=0)
    bowling_runs = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.username}: {self.runs} ({self.balls})'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance: User, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance: User, **kwargs):
    instance.profile.save()
