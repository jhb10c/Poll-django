from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from poll.models import Question, Choice
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic


# Create your views here.

class IndexView(generic.ListView):
    template_name = 'poll/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

'''
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    return render(request,'poll/index.html',{'latest_question_list':latest_question_list})
    #With render we do not need loader to get the template.
    #And we do not need HttpResponse to load the page.


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('poll\index.html')
    context = {'latest_question_list':latest_question_list}
    return HttpResponse(template.render(context, request))
    #With render we do not need loader to get the template.
    #And we do not need HttpResponse to load the page.
'''
'''
def results(request, question_id):
    response = "You're looking at the results of question {}."
    return HttpResponse(response.format(question_id))
'''
class DetailView(generic.DetailView):
    model = Question
    template_name = 'poll/detail.html'

'''
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'poll/detail.html', {'question':question})


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    
    return render(request, 'poll/detail.html',{'question':question})
'''

'''def vote(request, question_id):
    return HttpResponse("You're voting on question {}".format(question_id))'''

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'poll/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('poll:results', args=(question.id,)))
'''
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'poll/results.html', {'question': question})
'''
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'poll/results.html'

