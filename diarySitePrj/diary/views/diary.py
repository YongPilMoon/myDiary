from django.http import HttpResponse
from django.shortcuts import render
from diary.forms import DiaryForm
__all__ = [
    'diary_add',
    'diary_calendar',
]


def diary_add(request):
    user = request.user

    if request.method == 'POST':
        form = DiaryForm(request.POST)

        if form.is_valid():
            diary = form.save(commit=False)
            diary.author = user
            diary.save()
            return HttpResponse("diary detail")
    else:
        form = DiaryForm()
        return render(request, 'diary/diary_add.html', {'form':form})


def diary_calendar(request):
    context = {

    }
    return render(request, 'diary/diary_calendar.html', context)

