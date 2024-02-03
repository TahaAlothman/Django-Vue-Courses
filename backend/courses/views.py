from django.shortcuts import render
from rest_framework import generics
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend



from .serializers import CategorySerializers, CourseSerializers
from .models import Course, Category


class CourseListFilterAPI(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['price','category']



class CategoryListAPI(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
        




