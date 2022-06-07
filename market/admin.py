from django.contrib import admin
from .models import Ratings_and_Review, Rice_list_details, Purchase_cart_detail


admin.site.register(Purchase_cart_detail)
admin.site.register(Rice_list_details)
admin.site.register(Ratings_and_Review)

