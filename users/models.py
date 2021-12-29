from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    ROLE_CHOICES = (
        ('c', 'client'),
        ('s', 'seller'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    image = models.ImageField(default='default-profile.png', upload_to='profile_pics/')
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default="c")
    country = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    @property
    def get_all_gigs(self):
        try:
            return self.gigs.all()
        except:
            return None
  
    def register(self):
        self.save()
  
    @staticmethod
    def get_profile_by_email(email):
        try:
            return Profile.objects.get(user__email=email)
        except:
            return False
  
    def isExists(self):
        if Profile.objects.filter(user__email=self.email):
            return True
  
        return False

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def get_image_url(self):
        try:
            return self.image.url
        except:
            return ''


@receiver(post_save, sender=User)
def create_profile(sender, created, instance, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()
