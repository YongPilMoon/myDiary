from django.shortcuts import render

__all__ = [
    'login',
]


def login(request):
    user = request.user
    context = {
        'user': user,
    }
    return render(request, 'member/login.html', context)
