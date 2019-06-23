from django.db import models

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
    is_active = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


    def __str__(self):
        return self.name
