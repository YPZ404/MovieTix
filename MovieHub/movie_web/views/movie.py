from platform import release
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from datetime import datetime
from my_admin.models import Movie, Room, Release
from my_staff.models import Seat
from django.db.models import Q
from django.core import serializers
import json
# Create your views here.

# browse movie information
def index(request, pIndex=1):
    model = Movie.objects
    movieList = model.all()
    keyWord = request.GET.get("keyword", None)
    condition = []

    # keyword research
    if keyWord:
        movieList = movieList.filter(Q(movie_name__icontains=keyWord) | Q(type__icontains=keyWord)| Q(cast__icontains=keyWord))
        condition.append('keyword=' + keyWord)

    # In page by 10 record
    pIndex = int(pIndex)
    page = Paginator(movieList, 5)
    maxPages = page.num_pages
    if pIndex > maxPages:
        pIndex = maxPages
    if pIndex < 1:
        pIndex = 1
    movieList2 = page.page(pIndex)  # acquire current page info
    pageNum = page.page_range  # acquire num of page
    context = {"movieList": movieList2, 'pageNum': pageNum, 'pIndex': pIndex, 'maxPages': maxPages,
               'condition': condition}
    for st in movieList:
        print(st)
    return render(request, 'movie_web/movie/index.html', context)

def releaseList(request, pIndex=1):
    model = Release.objects
    releaseList = model.all()
    id = request.POST.get("movie_id", None)
    print(id)
    condition = []

    # keyword research
    if id:
        releaseList = releaseList.filter(movie_id=id)
        condition.append('movie_id=' + id)

    # In page by 10 record
    pIndex = int(pIndex)
    page = Paginator(releaseList, 5)
    maxPages = page.num_pages
    if pIndex > maxPages:
        pIndex = maxPages
    if pIndex < 1:
        pIndex = 1
    releaseList2 = page.page(pIndex)  # acquire current page info
    pageNum = page.page_range  # acquire num of page
    print(pageNum)
    context = {"releaseList": [], 
    'pageNum': list(pageNum), 
    'pIndex': int(pIndex), 
    'maxPages': int(maxPages),
    'condition': condition}
    for st in releaseList:
        print(st)
    json_data = serializers.serialize('json', releaseList2) # 将查询结果进行json序列化
    context['releaseList'] = json_data
    return HttpResponse(json.dumps(context), content_type="application/json")

# load movie booking page
def loadBooking(request, release_id):
    rIndex = int(release_id)
    try:
        # Selected movie to book
        release_ob = Release.objects.get(release_id = rIndex)
        movie_id = release_ob.movie_id
        movie_ob = Movie.objects.get(movie_id = movie_id)
        movie_name = movie_ob.movie_name
        room_id = release_ob.room_id
        room_ob = Room.objects.get(room_id = room_id)
        row_size = room_ob.row_size
        column_size = room_ob.column_size
        price = release_ob.price
        release_time = release_ob.release_time

        seat_obs = Seat.objects.filter(release_id = release_id)
        rows = range(1,row_size+1)
        columns = range(1,column_size+1)
        seat_list = []
        for row in rows:
            row_seat_obs = seat_obs.filter(row_id = row)
            row_seats = []
            for column in columns:
                seat_ob = row_seat_obs.get(column_id = column)
                seat = seat_ob.toDict()
                row_seats.append(seat)
            seat_list.append(row_seats)


        context = {'movie_name':movie_name, 'movie_id':movie_id, 'release_id':release_id, 'room_id':room_id,
        'seat_list':seat_list, 'price':price, 'release_time':release_time}

        # context = {'movie_name':movie_name, 'movie_id':movie_id, 'release_id':release_id, 'room_id':room_id,
        #  'rows':range(0,row_size), 'columns':range(0,column_size), 'price':price, 'release_time':release_time}
        return render(request, 'movie_web/movie/ticketBooking.html', context)
    except Exception as err:
        print(err)
        context = {'info': 'Cannot book the movie'}
    return render(request, 'movie_web/movie/ticketBooking.html', context)