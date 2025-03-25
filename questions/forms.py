from django.forms import ModelForm
from .models import Question, Comment
from django import forms

class QuestionForm(ModelForm):
    class Meta():
        model = Question
        fields = '__all__'
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'content1': forms.TextInput(attrs={'class':'form-control'}),
            'content2': forms.TextInput(attrs={'class':'form-control'}),
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
        