from django.contrib import admin
from .models import UserModel, FarmDetailsModel, ProductsModel, OrdersModel, OrderItemsModel, ReviewsModel, TransactionModel

# Register your models here.

admin.site.register(UserModel)
admin.site.register(FarmDetailsModel)
admin.site.register(ProductsModel)
admin.site.register(OrdersModel)
admin.site.register(OrderItemsModel)
admin.site.register(ReviewsModel)
admin.site.register(TransactionModel)
