from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import get_object_or_404, render
from .models import Post
from .forms import PostForm
from django.views.generic import View
from django.shortcuts import redirect


def post_new(request):

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            if request.FILES:
                post.image = request.FILES.get('image')
            post.save()
    else:
        form = PostForm()

    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
           # post.category = request.category
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def post_list(request):
    posts = Post.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


class IndexView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.order_by("-id")
        return render(request, 'blog/index.html', {
            'posts': posts,

        })


"""
class CategoryView(View):
    def get(self, request, *args, **kwargs):
        category_data = Category.objects.get(name=self.kwargs["category"])
        post_data = Post.objects.order_by("-id").filter(category=category_data)
        return render(request, "blog/base.html", {
            "post_data": post_data
        })
"""
