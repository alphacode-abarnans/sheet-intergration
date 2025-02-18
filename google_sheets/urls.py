from django.urls import path
from . import views

urlpatterns = [
    path("", views.google_sheet_view, name="google_sheet_view"),
    path("add/", views.add_row, name="add_row"),
    path("edit/<int:row_number>/", views.edit_row, name="edit_row"),
    path("delete/<int:row_number>/", views.delete_row, name="delete_row"),
]
