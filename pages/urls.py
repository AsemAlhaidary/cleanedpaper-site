from django.urls import path
from pages.views import *

app_name = 'pages'

urlpatterns = [
    path("", HomeView.as_view(), name='home'),
    path("contact/", ContactView.as_view(), name='contact'),
    path("blog/", BlogView.as_view(), name='blog'),
]
