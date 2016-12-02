from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect, response
from django.template import Context, loader
from .models import Question,Answer,Session
from django.views.decorators.http import require_GET,require_POST
from .forms import *
from datetime import datetime, timedelta
from lib.login import do_login
from lib.logout import do_logout

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
        form._user = request.user
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
    answer_form._user = request.user
    if answer_form.is_valid():
        answer = answer_form.save()
        answer.question
        return  redirect(answer.question)
    else:
        context = {'form':answer_form}
        return render(request, 'question.html', context)


def signup(request):
    # handle form post
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            answer = form.save()
            sessionid = do_login(request.POST.get('username'), request.POST.get('password'))
            url = '/'
            response = HttpResponseRedirect(url)
            response.set_cookie('sessionid', sessionid,
                                httponly=True, expires=datetime.now() + timedelta(hours=48)
                                )
            return response
    else:
        # show clean form
        form = SignupForm()
    # show worm with wgong data
    return render(request, 'signup.html', {
        'form': form
    })


def login(request):
    error = ''
    if request.method == "POST":
        form = LoginForm(request.POST)
        login = request.POST.get('username')
        passw = request.POST.get('password')
        url = request.POST.get('contunie', '/')
        sessionid = do_login(login, passw)
        if sessionid:
            response = HttpResponseRedirect(url)
            response.set_cookie('sessionid', sessionid,
                                httponly=True, expires=datetime.now() + timedelta(hours=48)
                                )
            return response
        else:
            error = u'Wrong login/password'
    else:
        form = LoginForm()
    return render(request, 'login.html', {
        'error' : error,
        'form' : form
    })

@require_POST
def logout(request):
    sessionid = request.COOKIES.get('sessionid')
    if sessionid is not None:
        do_logout(sessionid)
    response = redirect('/')
    response.delete_cookie('sessionid')
    return response