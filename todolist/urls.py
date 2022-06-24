from django.urls import path
from .views import Customeloginview, Deletetask, Tasklist,TaskDeatil,Cretetask,Updatetask,Customeloginview,registerpage
from django.contrib.auth.views import LogoutView

urlpatterns=[
    path('',Tasklist.as_view(),name="heompage"),
    path('detail/<int:pk>/',TaskDeatil.as_view(),name="detailpage"),
    
    path('create/',Cretetask.as_view(),name="create"),
    path('update/<int:pk>/',Updatetask.as_view(),name="update"),
    path('delete/<int:pk>/',Deletetask.as_view(),name="delete"),
    path('login/',Customeloginview.as_view(),name="loginpage"),
    path('logout/',LogoutView.as_view(next_page='loginpage'),name="logoutpage"),
    path('register/',registerpage.as_view(),name="registerpage"),

]
