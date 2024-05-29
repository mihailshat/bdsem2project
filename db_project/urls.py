from django.contrib import admin
from django.urls import path, include    # добавьте эту строку

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('courses.urls')),   # добавьте эту строку
]
