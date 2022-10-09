from django.urls import path

from movie_web.views import index

urlpatterns = [
    # movie web home page
    path('', index.index, name="index"),

]