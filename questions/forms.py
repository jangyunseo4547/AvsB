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
    class Meta():
        model = Comment
        exclude = ('question', )