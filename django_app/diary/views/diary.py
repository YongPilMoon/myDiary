# python
import calendar
from datetime import datetime
from django.contrib import messages
from django.shortcuts import render, redirect

from diary.forms import DiaryForm
from diary.models import Diary

__all__ = [
    'diary_add',
    'month_calendar',
    'diary_detail',

]


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
    if request.GET.get('pre_calendar'):
        pre_cal = (request.GET.get('pre_calendar')).split('-')
        year = int(pre_cal[0])
        month = int(pre_cal[1])
    elif request.GET.get('next_calendar'):
        next_cal = (request.GET.get('next_calendar')).split('-')
        year = int(next_cal[0])
        month = int(next_cal[1])
    else:
        today = datetime.today()
        year = today.year
        month = today.month

    pre_month = 12 if month-1 < 1 else month - 1
    pre_year = year - 1 if pre_month == 12 else year
    next_month = 1 if month + 1 > 12 else month + 1
    next_year = year + 1 if next_month == 1 else year
    pre_calendar = str(pre_year) + "-" + str(pre_month)
    next_calendar = str(next_year) + "-" + str(next_month)

    this_month_diary = Diary.objects.filter(diary_date__year=year, diary_date__month=month)
    monthdays = calendar.Calendar(calendar.SUNDAY).monthdayscalendar(year, month)
    monthdays = [[('0'+str(day), day) if day < 10 else (str(day), day) for day in week] for week in monthdays]
    context = {
        'monthdays': monthdays,
        'year': year,
        'month': ('{:02d}'.format(month), month),
        'days': ('일', '월', '화', '수', '목', '금', '토',),
        'this_month_diary': this_month_diary,
        'pre_calendar': pre_calendar,
        'next_calendar': next_calendar
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
