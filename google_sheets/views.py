from django.shortcuts import render
from .google_sheets import get_google_sheet_data

def google_sheet_view(request):
    data = get_google_sheet_data()
    return render(request, 'google_sheets/sheet_data.html', {'data': data})
