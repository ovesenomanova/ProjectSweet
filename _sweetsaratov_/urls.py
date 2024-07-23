from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('main.urls')),
    path('catalog/', include('catalog.urls')),
    path('messages/', include('messages.urls')),
    path('payment/', include('payment.urls')),
    path('users/', include('users.urls'))

]
