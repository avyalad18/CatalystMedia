from django.urls import path
from .views import InventoryView,UploadView

urlpatterns = [
    path('getbooks', InventoryView.as_view()),  
    path('addbook',InventoryView.as_view()),
    path('upload',UploadView.as_view()),
    path('updatebook/<int:id>',InventoryView.as_view()),
    path('deletebook/<int:id>',InventoryView.as_view()),
]
