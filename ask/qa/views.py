from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404
from django.http import HttpResponse
from django.template import Context, loader
from .models import Question
from django.views.decorators.http import require_GET

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

@require_GET
def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    context = {'question' : question}
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