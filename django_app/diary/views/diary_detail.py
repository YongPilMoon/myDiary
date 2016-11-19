# python
from datetime import datetime

from django.contrib import messages
from django.shortcuts import render, redirect

from diary.models import Diary

__all__ = [
    'diary_detail',
]


def diary_detail(request, year, month, day):
    selected_date = datetime.strptime(year+month+day, '%Y%m%d').date()
    diary_query = Diary.objects.filter(diary_date=selected_date)
    context = {
        'diary_query': diary_query,
    }
    if diary_query.exists():
        return render(request, 'diary/diary_detail.html', context)
    else:
        messages.info(request, '일기를 작성해 주세요.')
        return redirect('diary:diary_add', year=year, month=month, day=day)
