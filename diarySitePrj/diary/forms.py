from django import forms
from .models import Diary


class DiaryForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ('title', 'content', 'written_date', )
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'written_date': forms.SelectDateWidget(
            ),
            }

