import random

from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from my_admin.models import Movie
from django.core.paginator import Paginator
from datetime import datetime
import hashlib
import string

def index(request):
    return render(request, 'my_staff/release/index.html')

def release(requset):
    return render(requset, 'my_staff/release/release.html')
