from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), # Yeh aapka Warden dashboard ka link hai
    path('', include('complaints.urls')), # Yeh aapke naye student home page ka link hai
]