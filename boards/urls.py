from django.urls import path
from . import views

app_name = 'boards'

urlpatterns = [
    path('',views.PostList.as_view(), name='post_list'),
    path('detail/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('comment/<int:pk>/', views.CommentCreate.as_view(),name='comment_create'),
    path('create/', views.PostCreate.as_view(), name='post_create'),
    path('delete/<int:pk>/', views.PostDelete.as_view(), name='comment_delete'),
    path('update/<int:pk>/', views.CommentUpdate.as_view(), name='comment_update'),
    path('good/<int:pk>/<int:pk>/', views.goodfunc, name='comment_good'),
]
