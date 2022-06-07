from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Rice_list_details(models.Model):
    rice_name = models.CharField(max_length=50)
    import_from = models.CharField(max_length=70)
    about = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(blank=True)
    rating = models.ForeignKey('Ratings_and_Review', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.rice_name)

class Ratings_and_Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rice_name = models.ForeignKey(Rice_list_details, on_delete=models.CASCADE)
    image = models.ImageField(blank=True)
    review = models.CharField(max_length=150)
    ratings = models.FloatField()

    def __str__(self):
        return str(self.user)

class Purchase_cart_detail(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    rice_selected = models.ManyToManyField(Rice_list_details)
    quantity = models.IntegerField()

    def __str__(self):
        return str(self.user_name)