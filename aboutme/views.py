from django.shortcuts import render


def about_me(request):
    return render(request, 'aboutme/aboutme.html', {})