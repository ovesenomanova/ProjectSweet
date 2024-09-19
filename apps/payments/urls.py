from django.urls import path
from . import views

urlpatterns = [
    path('', views.PaymentListView.as_view(), name='payment'),
    path('info.payment/', views.InfoPayment.as_view(), name='info_payment')
]