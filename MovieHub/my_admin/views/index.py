from django.shortcuts import render, redirect
from django.urls import reverse

from my_admin.models import Staff
# Create your views here.
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'my_admin/index/index.html')


def loadLogin(request):
    return render(request, 'my_admin/index/loadLogin.html')


def login(request):
    try:
        staffId = request.POST["staffId"]
        password = request.POST["password"]
        ob = Staff.objects.get(staff_id=staffId)

        if password == ob.password and ob.level == 2:
            request.session['adminuser'] = ob.toDict()
            return redirect(reverse('admin_index'))
        elif password == ob.password and ob.level != 2:
            context = {'info': 'no permission'}
        else:
            context = {'info': 'password is incorrect'}
    except Exception as err:
        print(err)
        context = {'info': 'StaffId is invalid '}

    return render(request, "my_admin/index/loadLogin.html", context)


def logout(request):
    del request.session['adminuser']
    return redirect(reverse('admin_load_login'))
