from django.shortcuts import render
from django.db.models import F,Q

# Create your views here.
def about_views(request):
    if request.method == 'GET':
       return render(request,'about.html')