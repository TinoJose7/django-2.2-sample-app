from django.urls import path

from polls.views import IndexView, DetailView, ResultsView
from . import views

app_name = 'polls'

urlpatterns = [
    # ex: /polls/
    # path('', views.index, name='index'),
    path('', IndexView.as_view(), name='index'),
    # ex: /polls/5/
    # path('<int:question_id>/', detail, name='detail'),
    path('<int:pk>/', DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    # path('<int:question_id>/results/', results, name='results'),
    path('<int:pk>/results/', ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]