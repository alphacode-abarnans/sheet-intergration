from django.urls import path
from . import views

urlpatterns = [
    path('', views.google_sheet_view, name='google_sheet_view'),
]
