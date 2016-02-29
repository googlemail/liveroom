from django.shortcuts import render,get_object_or_404
from .models import Question,Choice,User
from django.views import generic
def Index(request):
    hello = 'this is yi ge tou piao app'
    return render(request,'polls/index.html',{'hello':hello})
class Indexview(generic.ListView):
    model = Question
    template_name = 'polls/index.html'
    context_object_name = 'question'
class Choiceview(generic.DetailView):
    model = Question
    template_name = 'polls/choice.html'
    context_object_name = 'question'
def vote(request,pk):
    question = get_object_or_404(Question,pk = pk)
    choice = question.choice_set.get(pk = request.POST['vote'])
    choice.vote += 1
    choice.save()
    return render(request,'polls/vote.html',{'question':question})


# Create your views here.
