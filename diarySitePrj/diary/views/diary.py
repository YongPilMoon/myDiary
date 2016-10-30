from django.shortcuts import render

__all__ = [
    'diary_add'
]


def diary_add(request):
    context = {

    }
    return render(request, 'diary/diary_add.html', context)
