from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic
from .forms import CommentCreateForm, PostCreateForm
from .models import Post, Comment
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
# from django.contrib.auth.decorators import login_required




# Create your views here.

# @login_required
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
        comment.writer = User.objects.get(pk=self.request.user.pk)
        comment.save()
        return redirect('boards:post_detail', pk=post_pk)


class PostCreate(generic.CreateView):
    model = Post
    form_class = PostCreateForm
    success_url = reverse_lazy('boards:post_list')


class PostDelete(generic.DeleteView):
    model = Comment
    success_url = reverse_lazy('boards:post_list')


class CommentUpdate(generic.UpdateView):
    model = Comment
    form_class = CommentCreateForm
    success_url = reverse_lazy('boards:post_list')

def goodfunc(request, pk_title, pk_comment):
    object = get_object_or_404(Comment, pk=pk_comment)
    object.good = object.good + 1
    object.save()
    return redirect('boards:post_detail', pk=pk_title)

def logoutfunc(request):
    logout(request)
    return redirect('home')


class UserProfileView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'boards/profile.html'
    def get_queryset(self):
        return User.objects.get(id=self.request.user.id)


