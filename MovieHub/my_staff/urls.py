from django.urls import path

from my_staff.views import index
from my_staff.views import staff
from my_staff.views import room
from my_staff.views import movie
from my_staff.views import release

urlpatterns = [
    # staff home page
    path('', index.index, name="staff_index"),

    # login logout
    path('loadLogin', index.loadLogin, name="staff_load_login"),
    path('login', index.login, name="staff_login"),
    path('logout', index.logout, name="staff_logout"),
    path('verify', index.verify, name="staff_verify"),

    # staff information management
    path('staff/<int:pIndex>', staff.index, name="staff_staff_index"),
    path('staff/add', staff.add, name="staff_staff_add"),
    path('staff/insert', staff.insert, name="staff_staff_insert"),
    path('staff/delete/<int:staffId>', staff.delete, name="staff_staff_delete"),
    path('staff/edit/<int:staffId>', staff.edit, name="staff_staff_edit"),
    path('staff/update/', staff.update, name="staff_staff_update"),

    # room management
    path('room/<int:pIndex>', room.index, name="staff_room_index"),
    path('room/add', room.add, name="staff_room_add"),
    path('room/insert', room.insert, name="staff_room_insert"),
    path('room/edit/<int:roomId>', room.edit, name="staff_room_edit"),
    path('room/update/', room.update, name="staff_room_update"),

    # movie info management
    path('movie/<int:pIndex>', movie.index, name="staff_movie_index"),
    path('movie/add', movie.add, name="staff_movie_add"),
    path('movie/insert', movie.insert, name="staff_movie_insert"),
    path('movie/edit/<int:movieId>', movie.edit, name="staff_movie_edit"),
    path('movie/update/', movie.update, name="staff_movie_update"),

    #release movie management
    path('release/', release.index, name="staff_release_index"),
    path('release/release', release.release, name="staff_release_release"),

]
