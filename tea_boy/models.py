from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):

    name = models.CharField(
        max_length = 64, 
        null = False, 
        blank = False, 
        unique = True
        )
    description = models.CharField(
        max_length = 128, 
        null = True, 
        blank = True
        )
    image = models.ImageField(null = True, blank = True)
    is_active = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name


class Order(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    notes = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return "1 %s - for %s %s" % (self.item.name, self.user.first_name, self.user.last_name)