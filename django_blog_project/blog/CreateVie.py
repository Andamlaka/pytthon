from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_form.html'  # Template for the form
    fields = ['title', 'content']  # Fields to be included in the form
    success_url = reverse_lazy('blog:list')  # Redirect to the post list after creation

    def form_valid(self, form):
        form.instance.author = self.request.user  # Set the author to the logged-in user
        return super().form_valid(form)
