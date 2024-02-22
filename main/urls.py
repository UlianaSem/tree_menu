from django.urls import path

from main.apps import MainConfig
from main.views import MenuListView, MenuDetailView, get_item

app_name = MainConfig.name

urlpatterns = [
    path('menu/', MenuListView.as_view(), name='menu-list'),
    path('menu/<int:pk>/', MenuDetailView.as_view(), name='menu-detail'),
    path('get_item/<int:pk>/', get_item, name='get_item'),
]
