from django.db import models

# Create your models here.
class Product(models.Model):
     Product_id = models.AutoField
     Product_name = models.CharField(max_length=69)
     Category = models.CharField(max_length=69, default="")
     SubCategory = models.CharField(max_length=69, default="")
     Price = models.IntegerField(default="0")
     Descriptions = models.CharField(max_length=333, default="")
     Publish_date = models.DateField("Publish Date", default="")
     Image = models.ImageField(upload_to="shop/Image", default="")
     def __str__(self):
          return self.product_name
