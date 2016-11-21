from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

def test(request, *args, **kwargs):
    return HttpResponse('OK')


def index(request):
    aaa = 'aaa'

    template = loader.get_template('index.html')
    context= Context({
        "aaa": aaa,
    })
    return HttpResponse(template.render(context))