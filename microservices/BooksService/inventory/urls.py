from django.urls import path
from .views import InventoryView,UploadView

urlpatterns = [
    path('getbooks',InventoryView.as_view(),name='getbooks'),   
    path('addbook',InventoryView.as_view(),name='addbook'),
    # path('upload',UploadView.as_view()),     
    path('updatebook/<int:id>',InventoryView.as_view(),name='updatebook'),
    path('deletebook/<int:id>',InventoryView.as_view(),name='deletebook'),
]
