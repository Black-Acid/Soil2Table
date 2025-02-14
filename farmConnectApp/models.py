from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.models import Token 

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError("Please add your email")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password=None, username=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if username is None:
            username = "admin"  # Set a default if not provided

        return self.create_user(email=email, username=username, password=password, **extra_fields)


ROLES = [
    ("Admin", "Admin" ), 
    ("Farmer", "Farmer"),
    ("Consumer", "Consumer")
]

class UserModel(AbstractBaseUser, PermissionsMixin):
    # class Role(models.TextChoices):  # Ensures role consistency
    #     ADMIN = "Admin", "Admin"
    #     FARMER = "Farmer", "Farmer"
    #     CONSUMER = "Consumer", "Consumer"


    username = models.CharField(max_length=30)
    email = models.EmailField(
        unique=True)
    role = models.CharField(max_length=10, choices=ROLES, default="Consumer")
    address = models.CharField(max_length=255, blank=True)
    is_staff = models.BooleanField(default=False)  # Add this field
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = "email"

    def __str__(self):
        return f"{self.username} ({self.role})"
    
    
    def save(self, *args, **kwargs):
        # Ensure the password is hashed before saving
        if self.pk is None or not self.password.startswith('pbkdf2_sha256$'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
    
        if not hasattr(self, 'auth_token'):  # Prevents duplicate tokens
                Token.objects.create(user=self)
    
    # def save(self, *args, **kwargs):
    #     # Hash the password only if it's not already hashed
    #     if not self.password.startswith('pbkdf2_sha256$'):
    #         self.password = make_password(self.password)
    #     super().save(*args, **kwargs)

    
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
    