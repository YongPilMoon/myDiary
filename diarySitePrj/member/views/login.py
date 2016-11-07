from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate as auth_authenticate
from django.contrib.auth import login as auth_login

__all__ = [
    'login',
]


def login(request):
    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']
        except KeyError:
            messages.debug(request, 'username 또는 password를 확인해주세요')
            return redirect('member:login')
        user = auth_authenticate(
            username=username,
            password=password
        )
        if user is not None:
            auth_login(request, user)
            messages.success(request, '로그인에 성공하였습니다.')
            return redirect('diary:month_calendar')
        else:
            messages.error(request, '로그인에 실패하였습니다.')
            return render(request, 'member/login.html', {})
    else:
        return render(request, 'member/login.html', {})
