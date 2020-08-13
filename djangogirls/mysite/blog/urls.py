from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'), # views.post_list= 이름을 붙인 것으로 뷰를 식별
]
#누군가 이 주소로 들어왔을 때 views.post_list를 보여주라!