from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('apps.main.urls')),
    path('catalog/', include('apps.catalog.urls')),
    path('msg/', include('apps.msg.urls')),
    path('payment/', include('apps.payment.urls')),
    path('users/', include('apps.users.urls'))

]
