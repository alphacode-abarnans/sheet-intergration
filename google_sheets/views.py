from django.shortcuts import render, redirect
from .google_sheets import get_google_sheet_data, add_google_sheet_data, update_google_sheet_data, delete_google_sheet_data

def google_sheet_view(request):
    data = get_google_sheet_data()
    return render(request, "google_sheets/sheet_data.html", {"data": data})


def add_row(request):
    if request.method == "POST":
        new_data = [request.POST["col1"], request.POST["col2"], request.POST["col3"], request.POST["col4"]]
        add_google_sheet_data(new_data)
        return redirect("google_sheet_view")
    return render(request, "google_sheets/add_row.html")


def edit_row(request, row_number):
    if request.method == "POST":
        updated_data = [request.POST["col1"], request.POST["col2"], request.POST["col3"], request.POST["col4"]]
        update_google_sheet_data(row_number, updated_data)
        return redirect("google_sheet_view")
    return render(request, "google_sheets/edit_row.html", {"row_number": row_number})


def delete_row(request, row_number):
    delete_google_sheet_data(row_number)
    return redirect("google_sheet_view")

def dashboard_view(request):
    return redirect("google_sheets/dashboard.html")