from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest


def hello_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello World!")
