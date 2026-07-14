import time

from django.http import JsonResponse
from django.shortcuts import render


def home(request):
    return render(request, "index.html")


def ping(request):
    return JsonResponse({"message": f"pong {time.time()}"})


# Celowy blad skladni
def broken_function():
    return syntax_error_tutaj
