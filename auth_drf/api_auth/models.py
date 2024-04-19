from django.db import models

class user_data(models.Model):
    name = models.CharField(("name"), max_length=50)
    
    def __str__(self) -> str:
        return self.name