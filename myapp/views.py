from django.shortcuts import render


def only_bootstrap(request):
    return render(request, "myapp/only_bootstrap.html")


def duplicate_filter(request):
    return render(request, "myapp/duplicate_filter.html")
