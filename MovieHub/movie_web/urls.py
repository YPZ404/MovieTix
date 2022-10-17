from django.urls import path
from movie_web.views import customer
from movie_web.views import index

urlpatterns = [
    # movie web home page
    path('', index.index, name="welcome"),

    # register, login, and logout
    path('register', index.register, name = "customer_register"),
    path('doRegister', index.doRegister, name = "customer_do_register"),
    path('loadLogin', index.loadLogin, name="customer_load_login"),
    path('login', index.login, name="customer_login"),
    path('logout', index.logout, name="customer_logout"),
    path('verify', index.verify, name="customer_verify"),
    path('home', index.home, name="customer_home"),

    # Profile management
    path('customer', customer.edit, name="customer_edit"),
    path('customer/update', customer.update, name="customer_update"),

]