from django.contrib import admin
from django.urls import path, include
from homepage.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('erp/', include('erp.urls')),
    path('login/', include('login.urls')),
    path('admin/', admin.site.urls),
]