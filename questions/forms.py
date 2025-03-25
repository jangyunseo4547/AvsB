from django.forms import ModelForm
from .models import Question, Comment
from django import forms

class QuestionForm(ModelForm):
    class Meta():
        model = Question
        fields = '__all__'
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control', 'placeholder':"질문을 입력하세요"}),
            'content1': forms.TextInput(attrs={'class':'form-control', 'placeholder':"보기 A를 입력하세요"}),
            'content2': forms.TextInput(attrs={'class':'form-control', 'placeholder':"보기 B를 입력하세요"}),
        }

class CommentForm(ModelForm):
    answer = forms.ChoiceField(
        widget = forms.RadioSelect,
        choices = {"1":"1", "2":"2"},
    )

    class Meta():
        model = Comment
        exclude = ('question', )
        widgets = {
            'content':forms.Textarea(attrs={
                'class': 'form-control', 'rows':'3'
                })
        }

class ProgressForm(forms.Form):
    percent = forms.IntegerField(min_value=0, max_value=100, initial=60, label="진행률 선택")
        