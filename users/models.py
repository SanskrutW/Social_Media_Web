from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


from PIL import Image
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill,Transpose
from taggit.managers import TaggableManager


WING = [
    
    ('INFORMATION TECHNOLOGY','INFORMATION TECHNOLOGY',),
    ('COMPUTER SCIENCE', 'COMPUTER SCIENCE'),
    ('CIVIL ENGINEERING','CIVIL ENGINEERING'),
    ('TEXTILE ENGINEERING','TEXTILE ENGINEERING'),
    ('TRAVEL`S AND TOURISM', 'TRAVEL`S AND TOURISM'),
    ('PACKAGING ENGINEERING','PACKAGING ENGINEERING'),
    ('MECHANICAL ENGINEERING','MECHANICAL ENGINEERING'),
    ('ELECTRICAL ENGINEERING','ELECTRICAL ENGINEERING'),
    ('AUTOMOBILE ENGINEERING','AUTOMOBILE ENGINEERING'),
    ('METALLURGICAL ENGINEERING','METALLURGICAL ENGINEERING'),
    ('MINING AND MINE SURVEYING', 'MINING AND MINE SURVEYING'),
    ('ELECTRONICS AND TELECOMMUNICATION','ELECTRONICS AND TELECOMMUNICATION'),

    
]

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=25,blank=True)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    image_thumbnail_user = ImageSpecField(source='image',
                                      processors=[Transpose(),ResizeToFill(170, 170)],
                                      format='JPEG',
                                      options={'quality': 100})

    description = models.CharField(max_length=100, blank=True)
    follows = models.ManyToManyField(User,related_name="follows",blank=True)
    followers = models.ManyToManyField(User,related_name="followers",blank=True)
    camps = TaggableManager(blank=True)
    wing = models.CharField(max_length=40,choices=WING,blank=True)
    def __str__(self):
        return f"{self.user.username}'s Profile"



REASON = [
    
    ('SPAM','SPAM'),
    ('INAPPROPRIATE','INAPPROPRIATE'),
    
]


class UserReport(models.Model):
    reported_user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='reported_user')
    reason = models.CharField(max_length=50,choices=REASON)
    reporting_user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='reporting_user')
    date_reported = models.DateTimeField(default=timezone.now) 

    def __str__(self):
        return self.reported_user.username