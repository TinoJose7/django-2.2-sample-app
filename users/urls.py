from django.urls import path
from users.views import IndexView, CreateView, UpdateView, DetailView, DeleteView
from django.contrib.auth.decorators import login_required

app_name = 'users'

urlpatterns = [
    path('', login_required(IndexView.as_view()), name='index'),
    path('create', login_required(CreateView.as_view()), name='create'),
    path('<int:pk>/edit', login_required(UpdateView.as_view()), name='edit'),
    path('<int:pk>', login_required(DetailView.as_view()), name='show'),
    path('<int:pk>/delete', login_required(DeleteView.as_view()), name='delete'),
]