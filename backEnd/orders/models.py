from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User= get_user_model()

class Orders(models.Model):

    SIZES = (
        ('SMALL', 'small'),
        ('MEDIUM', 'medium'),
        ('LARGE', 'large'),
        ('EXTRA_LARGE', 'extralarge')
    )

    STATUS=(
        ('PENDING', 'pending'),
        ('IN_TRANSIT', 'intransit'),
        ('DELIVERED', 'delivered')
    )

    customer= models.ForeignKey(User, on_delete=models.CASCADE)
    size= models.CharField(max_length=20, choices=SIZES, default=SIZES[0][0])
    status= models.CharField(max_length=20, choices=STATUS, default=STATUS[0][0])
    quantity= models.IntegerField()
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    def __str__(self):
        return f" <Orders{self.size} by {self.customer.id}> "
