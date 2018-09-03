from random import randrange

from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


def test_view(request):
    return HttpResponse("Hello!")


def random_numbers(request):
    random_nums = [randrange(0, 100) for i in range(10)]  # List of 10 random numbers

    return render(request, 'test.html', {'numbers': random_nums})


#examples of functions we will test, may later use
def a_function():
    return "beans"


def random_numbers_1_100():
    return randrange(0, 101)
