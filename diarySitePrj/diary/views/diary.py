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
    'calendar_detail',
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


def diary_add(request):
    user = request.user

    if request.method == 'POST':
        form = DiaryForm(request.POST)

        if form.is_valid():
            diary = form.save(commit=False)
            diary.author = user
            diary.save()
            return redirect('diary:diary_calendars')
    else:
        form = DiaryForm()
        return render(request, 'diary/diary_add.html', {'form': form})


def month_calendar(request, year, month):
    year = int(year)
    month = int(month)
    monthdays = calendar.Calendar(calendar.SUNDAY).monthdays2calendar(year, month)
    context = {
        'monthdays': monthdays,
        'year': year,
        'month': month,
        'days': ('일', '월', '화', '수', '목', '금', '토',)
    }

    return render(request, 'diary/month_calendar.html', context)


def calendar_detail(request, year, month, day):
    selected_date = datetime.strptime(year+month+day, '%Y%m%d').date()
    diary_query = Diary.objects.filter(written_date=selected_date)

    if diary_query.exists():
        return HttpResponse("calendar detail")
    else:
        messages.info(request, '일기를 작성해 주세요.')
        return redirect('diary:diary_add')
