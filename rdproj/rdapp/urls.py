from django.urls import path
from .views import UserViewList, UserViewCreate

urlpatterns = [
    path('userview/list/', UserViewList.as_view()),
    path('userview/create/', UserViewCreate.as_view())
]
