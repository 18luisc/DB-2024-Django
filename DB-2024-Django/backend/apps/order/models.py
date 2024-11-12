from django.db import models

class Order(models.Model): 
    order_id = models.IntegerField(primary_key=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True, blank=True)
    order_date = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey("clients.Customer", on_delete=models.CASCADE, related_name="orders")
    
    class Meta:
        db_table = "order"
        
    def __str__(self):
        return f"{self.order_id}"
