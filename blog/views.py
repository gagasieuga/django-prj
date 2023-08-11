from django.shortcuts import render, get_object_or_404
from .models import Blog, Comment
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
# Create your views here.
# def list(request):
#     Data = {'Blogs': Blog.objects.all().order_by('-date')} # -date means descending order, while date means ascending order
#     return render(request, 'blog/list.html', Data)
class BlogListView(ListView):
    queryset = Blog.objects.all().order_by('-date')
    template_name = 'blog/list.html'
    context_object_name = 'Blogs'
def post(request, id):
    post = get_object_or_404(Blog, id=id)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST, author=request.user, blog=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    # Post = {'Post': Blog.objects.get(id=id)}
    return render(request, 'blog/post.html', {'Post': post, 'form': form})
# class BlogDetailView(DetailView):
#     model = Blog # model = Blog is same as queryset = Blog.objects.all(), which is imported from .models import Blog
#     template_name = 'blog/post.html'