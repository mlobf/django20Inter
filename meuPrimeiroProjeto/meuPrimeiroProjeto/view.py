from django.http import HttpResponse


def hello(response):
    return HttpResponse('Hello World')


def articles(request, year):
    return HttpResponse('O ano enviado foi ' + str(year))
