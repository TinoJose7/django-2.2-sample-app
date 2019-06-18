from django.views import generic
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
# from django.shortcuts import render

# @login_required
# @permission_required('polls.can_vote')
# def index_view(request):
#     return render(request, 'admin/home.html', {})

class DashboardView(LoginRequiredMixin, TemplateView):
    # permission_required = 'polls.can_vote'
    login_url = '/login/'
    template_name = "admin/home.html"