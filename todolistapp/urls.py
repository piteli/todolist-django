from django.conf.urls import url
from . import views

app_name = 'users'

urlpatterns = [

    # /users/signup:url to take the input from the user
    url(r'^todolist/$', views.todolist, name='todolist'),
    #/users/showdata:url to display the list of users stored on the database
    url(r'^showdata/$', views.showdata, name='showdata'),

    url(r'^delete/(?P<id>\d+)/$',views.delete),

    url(r'^subtodolist/(?P<id>\d+)/$',views.subtodolist, name="subtodolist"),

    url(r'^hello/$', views.hello),


]
