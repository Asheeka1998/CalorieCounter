from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets

from .models import Foods, Activities
from .serializers import FoodsSerializer, ActivitiesSerializer
from ..User.views import AddActivityByUser, AddItemByUser


# Create your views here.
# create a viewset
class FoodsViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = Foods.objects.all()

    # specify serializer to be used
    serializer_class = FoodsSerializer


# create a viewset
class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activities.objects.all()
    # define queryset
    serializer_class = ActivitiesSerializer


def ReviewNewActivity(request):
    Activity = AddActivityByUser.objects.all()
    return HttpResponse({'Activity': Activity})


def ReviewNewItem(request):
    Item = AddItemByUser.objects.all()
    return HttpResponse({'Item': Item})


def ActivityApprove(request, id):
    obj = AddActivityByUser.objects.get(id=id)
    obj.Status = 1
    obj.save()
    return HttpResponse("New Activity Approved")


def ItemApprove(request, id):
    obj = AddItemByUser.objects.all()
    obj.Status = 1
    obj.save()
    return HttpResponse("New Item Approved")
