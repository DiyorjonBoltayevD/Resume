from django.urls import path

from resumeapp.views import *

urlpatterns = [
    path('', home, name='home'),

]
