from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from .models import Question,Answer
from django.views.decorators.http import require_GET,require_POST
from .forms import *

@require_GET
def test(request):
    return HttpResponse('OK')

@require_GET
def index(request, *args, **kwargs):

    question_lists = Question.objects.new()
    paginator = Paginator(question_lists,10)
    page = request.GET.get('page')
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        questions = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        questions = paginator.page(paginator.num_pages)

    context = {'questions' : questions}
    return render(request, 'news.html', context)

<<<<<<< HEAD
=======
#@require_GET
>>>>>>> 99c5ee1
def question_detail(request, pk):
    if request.method == "POST":
        return HttpResponse('OK')
    question = get_object_or_404(Question, pk=pk)
    form = AnswerForm(initial={'question': str(pk)})
    context = {'question' : question,
               'answers' : question.answer_set.all(),
               'form' : form }
    return render(request, 'question.html', context)

@require_GET
def popular(request,  *args, **kwargs):

    question_lists = Question.objects.popular()
    paginator = Paginator(question_lists,10)
    page = request.GET.get('page')
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        questions = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        questions = paginator.page(paginator.num_pages)

    context = {'questions': questions}
    return render(request, 'popular.html', context)

def ask(request):
    #handle form post
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            url = question.get_absolute_url()
            return  HttpResponseRedirect(url)
    else:
        #show clean form
        form = AskForm()
    #show worm with wgong data
    return render(request, 'ask_add.html',{
        'form' : form
    })

#@require_POST
def answer(request):
    if request.method == "GET":
        return HttpResponse('OK')
    answer_form = AnswerForm(request.POST)
    if answer_form.is_valid():
        answer = answer_form.save()
        answer.question
        return  redirect(answer.question)
    else:
        context = {'form':answer_form}
        return render(request, 'question.html', context)

