import random

from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from my_admin.models import Movie
from my_admin.models import Release
from my_admin.models import Room
from django.core.paginator import Paginator
from datetime import datetime
import hashlib
import string
from my_staff.models import Seat

# browse staff information
def index(request, pIndex=1):
    model = Movie.objects
    movieList = model.all()
    keyWord = request.GET.get("keyword", None)
    condition = []

    # keyword research
    if keyWord:
        movieList = movieList.filter(Q(movie_name__contains=keyWord) | Q(cast__contains=keyWord) |
                                     Q(introduction__contains=keyWord) | Q(type__contains=keyWord))
        condition.append('keyword=' + keyWord)

    # In page by 10 record
    pIndex = int(pIndex)
    page = Paginator(movieList, 10)
    maxPages = page.num_pages
    if pIndex > maxPages:
        pIndex = maxPages
    if pIndex < 1:
        pIndex = 1
    movieList2 = page.page(pIndex)  # acquire current page info
    pageNum = page.page_range  # acquire num of page
    context = {"movieList": movieList2, 'pageNum': pageNum, 'pIndex': pIndex, 'maxPages': maxPages,
               'condition': condition}
    for movie in movieList:
        print(movie.toDict())
    return render(request, 'my_staff/release/index.html', context)

# insert new staff action
def insert(request):
    try:
        ob = Release()
        roomId = request.POST['roomId']
        Room.objects.get(room_id=roomId)
        rowSize =  Room.objects.get(room_id=roomId).row_size
        columnSize = Room.objects.get(room_id=roomId).column_size
        while True:
            release_id = random.randint(10000000, 99999999)
            try:
                release = Movie.objects.get(release_id=release_id)
            except Exception as err:
                ob.release_id = release_id
                break
            else:
                continue

        for a in range(1, rowSize+1):
            for b in range(1, columnSize+1):
                oa = Seat()
                oa.release_id = release_id
                oa.room_id = request.POST['roomId']
                oa.row_id = a
                oa.column_id = b
                oa.is_available = 0
                oa.save()

        ob.movie_id = request.POST['movieId']
        ob.room_id = request.POST['roomId']
        ob.price = request.POST['price']
        ob.is_delete = 0
        ob.release_time = request.POST['releaseTime']
        ob.create_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.update_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        context = {'info': "Release new movie successfully, release_id is %s" % ob.release_id}
        ob.save()
    except Exception as err:
        print(err)
        context = {'info': "Room ID dose not exist, releasing new movie fails"}
    return render(request, 'my_staff/info.html', context)


# load employee information edit form
def edit(request, movieId=0):
    try:
        ob = Movie.objects.get(movie_id=movieId)
        context = {'movie': ob}
        return render(request, 'my_staff/release/edit.html', context)
    except Exception as err:
        print(err)
        context = {'info': 'Cannot find the information of edited movie'}
    return render(request, 'my_staff/info.html', context)


# update staff information action
def update(request):
    try:
        movieId = request.POST["movieId"]
        ob = Release.objects.get(movie_id=movieId)
        ob.release_time = request.POST['releaseTime']
        ob.update_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.create_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info': "Update Successfully"}
        return render(request, 'my_staff/info.html', context)
    except Exception as err:
        print(err)
        context = {'info': 'Update Failed'}
    return render(request, 'my_staff/info.html', context)

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False
