from django.shortcuts import get_object_or_404
from django.urls.base import reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from market.models import Post
from market.forms import PostForm
from django.utils import timezone
from django.urls import reverse_lazy

# Create your views here.
# CBV(Class Based View) 사용하기

class PostList(ListView):
    paginate_by = 6
    def get_queryset(self):
        return Post.objects.order_by('-create_date')

class PostCreate(CreateView):
    form_class = PostForm
    template_name = 'market/post_create.html'
    success_url = reverse_lazy('market:postdetail')

    def form_valid(self, form):
        post = form.save(False)
        post.create_date = timezone.now()
        post.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('market:postdetail', kwargs={'pk':self.object.pk})

class PostDetail(DetailView):
    model = Post

class PostUpdate(UpdateView):
    form_class = PostForm
    template_name = 'market/post_update.html'
    success_url = reverse_lazy('market:postdetail')

    def get_object(self):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        post.modify_date = timezone.now()
        post.save()
        return post

    def get_success_url(self):
        return reverse_lazy('market:postdetail', kwargs={'pk':self.object.pk})


class PostDelete(DeleteView):
    model = Post
    success_url = '/'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)