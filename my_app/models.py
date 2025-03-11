from django.db import models

# Create your models here.
class User_table(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)

    class Meta:
        db_table = 'user_table'

class Products_table(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')

    class Meta:
        db_table = 'products_table'

class Cart_table(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User_table, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products_table, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        db_table = 'cart_table'

    @property
    def product_total(self):
        return self.product_id.price * self.quantity
