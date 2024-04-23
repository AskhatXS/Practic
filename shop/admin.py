from django.contrib import admin
from .models import Product, ProductImage, Comment, Rating, Editor


admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Comment)
admin.site.register(Rating)
admin.site.register(Editor)