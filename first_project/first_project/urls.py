# first_project/urls.py
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView, TemplateView
from book_store.views import SignUpView
urlpatterns = [
    path("books/", include("book_store.urls")),  # This includes the urls from your app under /books/
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='books/', permanent=True)),  # Redirect from root to /books/
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', TemplateView.as_view(template_name='profile.html'), name='profile'),
    path("signup/", SignUpView.as_view(), name="templates/registration/signup"),
    
]