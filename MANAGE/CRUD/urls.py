from django.urls import path
from . import views
urlpatterns = [

path('',views.HOMEPAGE,name= "home"),
path('home',views.HOMEPAGE,name= "home"),
path('reg',views.register,name="reg"),
path('log',views.login,name="log"),
path('inner',views.inner,name= "inner"),
path('out',views.logout,name= "out"),
path('create',views.create,name= "create"),
path('update/<int:pk>',views.update,name= "update"),
path('delete/<int:pk>',views.delete,name= "delete"),
path('search',views.search,name= "search"),

]