# from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('I''m a teenage lobotomy!')


def detail(request, question_id):
    response = "Detail of question %s"
    return HttpResponse(response % question_id)


def results(request, question_id):
    response = "Results of question %s"
    return HttpResponse(response % question_id)


def vote(request, question_id):
    response = "Register a vote on question %s"
    return HttpResponse(response % question_id)