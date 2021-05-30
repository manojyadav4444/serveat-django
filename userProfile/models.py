from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.core.validators import MaxValueValidator
# Create your models here.

class Profile(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="profile_pics", default="default.png", null=True, blank=True)
    number_of_ratings = models.IntegerField(default=0)
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0)
    address_1 = models.CharField(max_length=50)
    address_2 = models.CharField(max_length=30)
    pin_code = models.IntegerField(validators=[MaxValueValidator(999999)])

    def __str__(self):
        return f"{self.user}'s profile"

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if(img.height > 300 or img.width > 300) :
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
