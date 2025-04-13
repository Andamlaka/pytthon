from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post, Comment
from django.contrib.auth.forms import UserCreationForm
from .forms import CommentForm 
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.views.generic import DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context['form'] = CommentForm()
        context['comments'] = Comment.objects.filter(post=post)
        return context

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user  # Assign the logged-in user as the comment author
            comment.post = post  # Link the comment to the current post
            comment.save()
            return HttpResponseRedirect(reverse('post_detail', kwargs={'pk': post.pk}))
        else:
            return self.render_to_response({'form': form, 'post': post})
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class RegisterView(CreateView):
    template_name = 'registration/register.html'  # Your template for registration
    form_class = UserCreationForm  # Django's built-in user creation form
    success_url = reverse_lazy('login')  # Redirect to login page after successful registration

@login_required
def post_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        content = request.POST.get('content')
        comment = Comment.objects.create(post=post, author=request.user, content=content)
        return redirect('post_detail', pk=post.pk)
    return render(request, 'blog/post_comment.html', {'post': post})

# View to delete a comment
@login_required
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.user == comment.author:
        comment.delete()
        return redirect('post_detail', pk=comment.post.pk)
    return HttpResponseForbidden("You don't have permission to delete this comment.")

class CommentUpdateView(UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comment_edit.html'
    context_object_name = 'comment'

    def get_queryset(self):
        return Comment.objects.filter(author=self.request.user)  # Ensure the user can only edit their own comments

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.post.pk})
    
    class CommentDeleteView(DeleteView):
        model = Comment
        template_name = 'comment_confirm_delete.html'
        context_object_name = 'comment'

        def get_queryset(self):
            return Comment.objects.filter(author=self.request.user)  # Ensure the user can only delete their own comments

        def get_success_url(self):
            return reverse_lazy('post_detail', kwargs={'pk': self.object.post.pk})
        