from django.urls import path
from . import views
urlpatterns = [


path('regapi',views.register,name="reg"),
path('logapi',views.login,name="log"),
path('innerapi',views.inner,name= "inner"),
path('listapi',views.list,name= "list"),
path('createapi',views.create,name= "create"),
path('updateapi/<int:pk>',views.update,name= "update"),
path('deleteapi/<int:pk>',views.delete,name= "delete"),
path('searchapi',views.search,name= "search"),
path('outapi',views.logout,name= "out"),

]