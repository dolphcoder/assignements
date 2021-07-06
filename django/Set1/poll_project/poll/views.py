from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.http import HttpResponse
from .models import Poll

# Create your views here.
class PollListView(ListView):
    model = Poll
    context_object_name = 'polls'

# def home(request):
#     polls = Poll.objects.all()
#     context = {
#         'polls': polls
#     }
#     return render(request, 'poll/home.html', context)

class VoteView(UpdateView):
    model = Poll
    fields = ['question', 'option_one', 'option_two', 'option_three']
    template_name = 'poll/vote.html'

    def form_valid(self, form):
        selected_option = self.request.POST['poll']
        print(selected_option)
        if selected_option == 'option1':
            form.instance.option_one_count += 1
        elif selected_option == 'option2': 
            form.instance.option_two_count += 1
        else:
            form.instance.option_three_count += 1
        return super().form_valid(form)

# def vote(request, poll_id):
#     poll = Poll.objects.get(pk=poll_id)
#     if request.method == 'POST':
#         selected_option = request.POST['poll']
#         if selected_option == 'option1':
#             poll.option_one_count += 1
#         elif selected_option == 'option2':
#             poll.option_two_count += 1
#         elif selected_option == 'option3':
#             poll.option_three_count += 1
#         else:
#             return HttpResponse(400, 'Invalid Form')
#         poll.save()
#         return redirect('results', poll.id)
#     context = {
#         'poll': poll
#     }
#     return render(request, 'poll/vote.html', context)

class ResultsView(DetailView):
    context_object_name = 'poll'
    model = Poll

# def results(request, poll_id):
#     poll = Poll.objects.get(pk=poll_id)
#     context = {
#         'poll': poll
#     }
#     return render(request, 'poll/results.html', context)

class PollCreateView(CreateView):
    model = Poll
    fields = ['question', 'option_one', 'option_two', 'option_three']
    # success_url = '/'
    

# def create(request):
#     if request.method == 'GET':
#         form = CreatePollForm()
#     else:
#         form = CreatePollForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     context = {
#         'form': form
#     }
#     return render(request, 'poll/create.html', context)
