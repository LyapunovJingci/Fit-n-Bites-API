
from rest_framework import generics, status
from .models import food
from .serializers import FoodSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework_api_key.permissions import HasAPIKey

class FoodList(generics.ListAPIView):
    '''
        Return a list of food details
    '''
    serializer_class = FoodSerializer
    pagination_class = PageNumberPagination 
    #permission_classes = [HasAPIKey]
    def get_queryset(self):
        queryset = food.objects.all()
        keyword = self.request.query_params.get('keyword', None)
        max_query = self.request.query_params.get('max', None)
        min_query = self.request.query_params.get('min', None)
        if keyword is not None:
            queryset = queryset.filter(Main_food_description__icontains=keyword)
        if max_query is not None:
            queryset = queryset.filter(Energy__lte=max_query)
        if min_query is not None:
            queryset = queryset.filter(Energy__gte=min_query)
        
        return queryset

class FoodDetail(generics.RetrieveAPIView):
    permission_classes = [HasAPIKey]
    queryset = food.objects.all()
    serializer_class = FoodSerializer

class AlcoholFreeList(generics.ListAPIView):
    #queryset = food.objects.all().filter(Alcohol__float=0)
    serializer_class = FoodSerializer
    pagination_class = PageNumberPagination
    permission_classes = [HasAPIKey]
    def get_queryset(self):
        queryset = food.objects.all().filter(Alcohol=0)
        keyword = self.request.query_params.get('keyword', None)
        max_query = self.request.query_params.get('max', None)
        min_query = self.request.query_params.get('min', None)
        if keyword is not None:
            queryset = queryset.filter(Main_food_description__icontains=keyword)
        if max_query is not None:
            queryset = queryset.filter(Energy__lte=max_query)
        if min_query is not None:
            queryset = queryset.filter(Energy__gte=min_query)
        
        return queryset

class CaffeineFreeList(generics.ListAPIView):
    #queryset = food.objects.all()
    serializer_class = FoodSerializer
    pagination_class = PageNumberPagination
    permission_classes = [HasAPIKey]
    def get_queryset(self):
        queryset = food.objects.all().filter(Caffeine=0)
        keyword = self.request.query_params.get('keyword', None)
        max_query = self.request.query_params.get('max', None)
        min_query = self.request.query_params.get('min', None)
        if keyword is not None:
            queryset = queryset.filter(Main_food_description__icontains=keyword)
        if max_query is not None:
            queryset = queryset.filter(Energy__lte=max_query)
        if min_query is not None:
            queryset = queryset.filter(Energy__gte=min_query)
        
        return queryset