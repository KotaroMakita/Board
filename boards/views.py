from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic
from .forms import CommentCreateForm, PostCreateForm
from .models import Post, Comment
from django import forms



# Create your views here.


class PostList(generic.ListView):
    model = Post
    # ordering = '-created_at'
    paginate_by = 10


class PostDetail(generic.DetailView):
    model = Post


class CommentCreate(generic.CreateView):
    model = Comment
    form_class = CommentCreateForm

    def form_valid(self, form):
        post_pk = self.kwargs['pk']
        post = get_object_or_404(Post, pk=post_pk)
        comment = form.save(commit=False)
        comment.target = post
        comment.save()
        return redirect('boards:post_detail', pk=post_pk)


class PostCreate(generic.CreateView):
    model = Post
    form_class = PostCreateForm
    success_url = reverse_lazy('boards:post_list')
