from django.db import models
#from .models import Manufacturer

class Product(models.Model): 
    product_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    manufacturer = models.ForeignKey("manufacturer.Manufacturer", on_delete=models.CASCADE, related_name="products")
    
    class Meta:
        db_table = "product"
        
    def __str__(self):
        return self.name
