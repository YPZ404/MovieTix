from django.urls import path

from my_admin.views import index
from my_admin.views import staff

urlpatterns = [
    # admin home page
    path('', index.index, name="admin_index"),

    # login logout
    path('loadLogin', index.loadLogin, name="admin_load_login"),
    path('login', index.login, name="admin_login"),
    path('logout', index.logout, name="admin_logout"),

    # staff information management
    path('staff/<int:pIndex>', staff.index, name="admin_staff_index"),
    path('staff/add', staff.add, name="admin_staff_add"),
    path('staff/insert', staff.insert, name="admin_staff_insert"),
    path('staff/delete/<int:staffId>', staff.delete, name="admin_staff_delete"),
    path('staff/edit/<int:staffId>', staff.edit, name="admin_staff_edit"),
    path('staff/update/', staff.update, name="admin_staff_update"),

]
