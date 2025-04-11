from django.shortcuts import render
from .models import Product  # this is your Product model
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
def product(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'