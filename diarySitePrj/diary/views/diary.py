# python
from datetime import datetime
import calendar
import pprint

# django
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect

# custom
from diary.forms import DiaryForm
from diary.models import Diary, ExampleModel

__all__ = [
    'diary_add',
    'month_calendar',
    'diary_detail',
    'index',
    'photo',
]


def photo(request):
    exampleModel = ExampleModel.objects.all()
    context = {
        "exampleModel":exampleModel
    }
    return render(request, 'diary/diary_photo.html', context)


def index(request):
    user = request.user
    context = {
        'user': user,
    }
    return render(request, 'index.html', context)


def diary_add(request, year, month, day):
    user = request.user
    diary_date = datetime.strptime(year+'-'+month+'-'+day, "%Y-%m-%d").date()
    if request.method == 'POST':
        form = DiaryForm(request.POST)
        if form.is_valid():
            diary = form.save(commit=False)
            diary.author = user
            diary.diary_date = diary_date
            diary.save()
            return redirect('diary:diary_detail', year=year, month=month, day=day)
    else:
        form = DiaryForm()
        context = {
            'form': form,
            'year': year,
            'month': month,
            'day': day
        }
        return render(request, 'diary/diary_add.html', context)


def month_calendar(request):
    today = datetime.today()
    year = today.year
    month = today.month

    this_month_diary = Diary.objects.filter(diary_date__year=year, diary_date__month=month)
    monthdays = calendar.Calendar(calendar.SUNDAY).monthdayscalendar(year, month)
    monthdays = [[('0'+str(day), day) if day < 10 else (str(day), day) for day in week] for week in monthdays]
    context = {
        'monthdays': monthdays,
        'year': year,
        'month': ('{:02d}'.format(month), month),
        'days': ('일', '월', '화', '수', '목', '금', '토',),
        'this_month_diary': this_month_diary,
    }

    return render(request, 'diary/month_calendar.html', context)


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
