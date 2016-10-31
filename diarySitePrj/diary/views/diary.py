from django.shortcuts import render

__all__ = [
    'diary_add',
    'diary_calendar',
]


def diary_add(request):
    context = {

    }
    return render(request, 'diary/diary_add.html', context)


def diary_calendar(request):
    context = {

    }
    return render(request, 'diary/diary_calendar.html', context)

