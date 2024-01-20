from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test_api_view),
    path('',views.product_list_api_viem),
    path('<int:id>/)',views.product_detail_api_view),
]