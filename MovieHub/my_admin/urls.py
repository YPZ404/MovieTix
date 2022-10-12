from django.urls import path

from my_admin.views import index
from my_admin.views import staff
from my_admin.views import room
from my_admin.views import movie

urlpatterns = [
    # admin home page
    path('', index.index, name="admin_index"),

    # login logout
    path('loadLogin', index.loadLogin, name="admin_load_login"),
    path('login', index.login, name="admin_login"),
    path('logout', index.logout, name="admin_logout"),
    path('verify', index.verify, name="admin_verify"),

    # staff information management
    path('staff/<int:pIndex>', staff.index, name="admin_staff_index"),
    path('staff/add', staff.add, name="admin_staff_add"),
    path('staff/insert', staff.insert, name="admin_staff_insert"),
    path('staff/delete/<int:staffId>', staff.delete, name="admin_staff_delete"),
    path('staff/edit/<int:staffId>', staff.edit, name="admin_staff_edit"),
    path('staff/update/', staff.update, name="admin_staff_update"),

    # room management
    path('room/<int:pIndex>', room.index, name="admin_room_index"),
    path('room/add', room.add, name="admin_room_add"),
    path('room/insert', room.insert, name="admin_room_insert"),
    path('room/edit/<int:roomId>', room.edit, name="admin_room_edit"),
    path('room/update/', room.update, name="admin_room_update"),

    # movie info management
    path('movie/<int:pIndex>', movie.index, name="admin_movie_index"),
    path('movie/add', movie.add, name="admin_movie_add"),
    path('movie/insert', movie.insert, name="admin_movie_insert"),
    path('movie/edit/<int:movieId>', movie.edit, name="admin_movie_edit"),
    path('movie/update/', movie.update, name="admin_movie_update"),
]
