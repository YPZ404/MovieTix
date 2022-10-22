from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from datetime import datetime
from my_admin.models import Movie
from my_admin.models import Release
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