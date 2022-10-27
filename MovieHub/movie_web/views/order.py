from platform import release
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator
from datetime import datetime
from my_admin.models import Order
from my_admin.models import Release
from django.db.models import Q
from django.core import serializers
from my_staff.models import Seat
import json

def index(request, pIndex=1):
    model = Order.objects
    orderList = model.all()
    condition = []
    # In page by 10 record
    pIndex = int(pIndex)
    page = Paginator(orderList, 10)
    maxPages = page.num_pages
    if pIndex > maxPages:
        pIndex = maxPages
    if pIndex < 1:
        pIndex = 1
    orderList2 = page.page(pIndex)  # acquire current page info
    pageNum = page.page_range  # acquire num of page
    context = {"orderList": orderList2, 'pageNum': pageNum, 'pIndex': pIndex, 'maxPages': maxPages,
               'condition': condition}
    for st in orderList:
        print(st)
    return render(request, 'movie_web/order/index.html', context)

def cancel(request):
    model = Order.objects
    orderList = model.all()
    id = request.POST.get("order_id", None)
    print(id)
    orderList = orderList.filter(order_id=id)
    if(len(orderList)!=1):
        return JsonResponse({'info':'cancel failed!'})
    order = orderList[0]
    order.is_cancel = 1
    order.save()
    seat_content = order.seat_content
    seats = seat_content.split(" ")
    for seat in seats:  
        print(seat)
        row = seat[4]
        column = seat[6]
        seatList = Seat.objects.all().filter(Q(row_id=row) & Q(column_id=column)).delete()
        if(len(seatList)!=1):
            return JsonResponse({'info':'cancel failed!'})
        seatList[0].is_available = 0
        seatList[0].save()
    return JsonResponse({'info':'Successfully Canceled!'})