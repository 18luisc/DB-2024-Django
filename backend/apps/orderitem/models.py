from django.db import models

class Orderitem(models.Model): 
    order_item_id = models.IntegerField(primary_key=True)
    order = models.ForeignKey("order.Order", on_delete=models.CASCADE, related_name="orderitems")
    product = models.ForeignKey("product.Product", on_delete=models.CASCADE, related_name="orderitems2")
    quantity = models.IntegerField(null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True, blank=True)

    class Meta:
        db_table = "order_items"
        
    def __str__(self):
        return self.order_item_id
