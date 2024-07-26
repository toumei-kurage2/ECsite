from django.contrib import admin
from .models import (
    Products,ProductPictures,ProductTypes,
    Manufacturers,Address
)

admin.site.register(
    [Products,ProductPictures,ProductTypes,Manufacturers,Address]
)
