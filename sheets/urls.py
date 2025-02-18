from django.contrib import admin
from django.urls import path, include
from google_sheets import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.google_sheet_view, name='google_sheet_view'),
    path('google-sheets/', include('google_sheets.urls')),
]
