from django.db import models




# class UserModel(models.Model):
#     email = models.EmailField()
#     password = models.CharField(max_length=255)

class UserModel(models.Model):
    class Role(models.TextChoices):  # Ensures role consistency
        ADMIN = "Admin", "Admin"
        FARMER = "Farmer", "Farmer"
        CONSUMER = "Consumer", "Consumer"

    username = models.CharField(max_length=30)
    email = models.EmailField(db_index=True)
    password = models.CharField(max_length=30)
    role = models.CharField(max_length=10, choices=Role.choices, default=Role.CONSUMER)
    address = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.username} ({self.role})"

    
class FarmDetailsModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, limit_choices_to={'role': 'Farmer'}, related_name="farm")
    farm_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.farm_name} - Owned by {self.user.username}"


class ProductsModel(models.Model):
    farmer_id = models.ForeignKey(FarmDetailsModel, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    quantity_available = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Add an Image url field
    
    
class OrdersModel(models.Model):
    consumer_id = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    order_status = models.CharField(max_length=255)
    total_order_price = models.DecimalField(max_digits=20, decimal_places=4)
    shipping_address = models.CharField(max_length=255)
    order_date = models.DateTimeField(auto_now=True)
    delivery_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
class OrderItemsModel(models.Model):
    order_id = models.ForeignKey(OrdersModel, on_delete=models.CASCADE)
    product_id = models.ForeignKey(ProductsModel, on_delete=models.CASCADE)
    quantity_purchased = models.IntegerField()
    price_of_purchased = models.DecimalField(max_digits=20, decimal_places=4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
class ReviewsModel(models.Model):
    consumer_id = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    farmer_id = models.ForeignKey(FarmDetailsModel, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
class TransactionModel(models.Model):
    order_id = models.ForeignKey(OrdersModel, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=20, decimal_places=4)
    payment_method = models.CharField(max_length=255)
    payment_status = models.CharField(max_length=255)
    transaction_date = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    