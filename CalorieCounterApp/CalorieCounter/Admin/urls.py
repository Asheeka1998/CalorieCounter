# basic URL Configurations
from django.urls import include, path
# import routers
from rest_framework import routers

# import everything from views
from .views import *

# define the router
router = routers.DefaultRouter()

# define the router path and viewset to be used
router.register(r'AddFoods', FoodsViewSet)
router.register(r'AddActivity', ActivityViewSet)

# specify URL Path for rest_framework
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('item_approve/<id>', ItemApprove),
    path('activity_approve/<id>', ActivityApprove),
    path('review_new_activity', ReviewNewActivity),
    path('review_new_item', ReviewNewItem)

]