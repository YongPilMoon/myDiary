import datetime

from django.shortcuts import redirect, render

from diary.forms import DiaryForm

__all__ =[
    'diary_add'
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
