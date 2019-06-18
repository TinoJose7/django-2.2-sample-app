from django.shortcuts import render
from django.views import generic
# from .models import User
from django.contrib.auth.models import User
from django.urls import reverse
from django.db import transaction
from django.http import HttpResponseRedirect
from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404
from django.http import Http404

# Create your views here.
class IndexView(
    generic.ListView):
    template_name = 'users/index.html'
    login_url = '/login/'
    context_object_name = 'latest_user_list'

    def get_queryset(self):
        """ Return the last fice users. """
        return User.objects.order_by('-date_joined')[:5]


class CreateView(
    generic.edit.CreateView):
    template_name = 'users/create.html'
    model = User
    success_message = 'New new user has been created.'

    fields = ['first_name', 'last_name', 'username', 'email', 'password']

    def form_valid(self, form):
        password = make_password(form.cleaned_data.get('password'))
        form.instance.password = password
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('users:index')


class UpdateView(
    generic.edit.UpdateView):
    template_name = 'users/edit.html'
    model = User
    fields = ['first_name', 'last_name', 'username', 'email']

    def get_object(self, *args, **kwargs):
        user = get_object_or_404(User, pk=self.kwargs['pk'])
        return user
    
    def get_success_url(self):
        return reverse('users:index')
        # return reverse('users:edit', kwargs={'pk': self.object.pk})


class DetailView(
    generic.DetailView):
    template_name = 'users/show.html'
    model = User


class DeleteView(
    generic.DeleteView):
    # template_name = ''
    model = User
    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        user = get_object_or_404(User, pk=self.kwargs['pk'])
        # obj = super(DeleteView, self).get_object()
        # if not obj.owner == self.request.user:
        #     raise Http404
        return user

    def get_success_url(self):
        return reverse('users:index')

    