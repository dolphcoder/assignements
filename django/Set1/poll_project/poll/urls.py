from django.urls import path
from .views import *

urlpatterns = [
    path('', PollListView.as_view(), name='home'),
    path('create', PollCreateView.as_view(), name='create'),
    path('vote/<int:pk>', VoteView.as_view(), name='vote'),
    path('result/<int:pk>', ResultsView.as_view(), name='results'),
]