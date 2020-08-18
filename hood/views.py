from django.shortcuts import render
from .models import NeighbourHood,Post
from django.contrib.auth import login, authenticate
# Create your views here.

@login_required(login_url='login')
def index(equest):
  return render(request, 'index.html')
