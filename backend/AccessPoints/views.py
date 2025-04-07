from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    """
    Render the index page.
    """
    return render(request,'AccessPoints/access_points_page.html')