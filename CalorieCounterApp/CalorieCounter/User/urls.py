# basic URL Configurations
from django.urls import include, path

# import everything from views
from .views import *

# specify URL Path for rest_framework
urlpatterns = [
    path('Signup/', RegisterPage),
    path('Login/', LoginPage),
    path('Logout/', LogOutPage),
    path('RecordFood/', select_food),
    path('RecordActivity/', select_activity),
    path('view_reports/<date1>', select_activity),
    path('view_reports/<date1>/<date2>', select_activity)
]