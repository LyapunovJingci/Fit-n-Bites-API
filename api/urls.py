from django.urls import path

from .views import FoodDetail, FoodList, AlcoholFreeList, CaffeineFreeList


urlpatterns = [
    path('foods/', FoodList.as_view()),
    path('food/<int:pk>/', FoodDetail.as_view()),
    path('foods/alcoholfree/', AlcoholFreeList.as_view()),
    path('foods/caffeinefree/', CaffeineFreeList.as_view()),

]