from django.urls import path
from . import views

app_name = 'boards'

urlpatterns = [
    path('',views.PostList.as_view(), name='post_list'),
    path('detail/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('comment/<int:pk>/', views.CommentCreate.as_view(),name='comment_create'),
    path('create/', views.PostCreate.as_view(), name='post_create'),

]
