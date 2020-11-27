from django.db import models
import uuid

class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50, null=True)
    age = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f'{self.name}, phone: {self.phone}, age: {self.age}'
