from django.urls import path, include
from . import views
from  django.views.generic import TemplateView

app_name = 'boards'

urlpatterns = [
    path('',views.PostList.as_view(), name='post_list'),
    path('detail/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('comment/<int:pk>/', views.CommentCreate.as_view(),name='comment_create'),
    path('create/', views.PostCreate.as_view(), name='post_create'),
    path('delete/<int:pk>/', views.PostDelete.as_view(), name='comment_delete'),
    path('update/<int:pk>/', views.CommentUpdate.as_view(), name='comment_update'),
    path('good/<int:pk_title>/<int:pk_comment>/', views.goodfunc, name='comment_good'),
    path('logout/', views.logoutfunc, name='logout')

]
