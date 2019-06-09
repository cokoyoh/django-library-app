from django.shortcuts import render, redirect


def welcome(request):
    if request.user.is_authenticated:
        return redirect('user_home')

    return render(request, 'library/welcome.html')
