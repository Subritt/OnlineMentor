from django.shortcuts import render


def home(request):

    return render(request, 'home.html')


def about(request):

    return render(request, "about.html")


def tutor(request):

    return render(request, "tutor.html")


def contactus(request):

    return render(request, "contactus.html")


def signin(request):

    return render(request, "signin.html")


def signup(request):

    return render(request, "signup.html")


def blog(request):

    return render(request, "blog.html")
