from django.contrib import admin
from django.urls import path, include
from .views import TitleViewRedirect


urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('apps.main.urls')),
    path('catalog/', include('apps.catalog.urls')),
    path('forum/', include('apps.forum.urls')),
    path('payment/', include('apps.payment.urls')),
    path('users/', include('apps.users.urls')),
    path('', TitleViewRedirect.as_view)

]
