from django.shortcuts import render,redirect
from .forms import QuestionForm, CommentForm, ProgressForm
from .models import Question, Comment
import random

# Create your views here.
def create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('questions:index')

    else:
        form = QuestionForm()

    context = {
        'form':form,
    }
    return render(request, 'create.html',context)

def index(request):
    questions=Question.objects.all()

    context={
        'questions':questions,
    }
    return render(request, 'index.html', context)

def detail(request, id):
    question=Question.objects.get(id=id)
    form = CommentForm()
    comments = question.comment_set.all()

    context = {
        'question':question,
        'form':form,
        'comments':comments,
    }
    return render(request, 'detail.html', context)

def comment_create(request, question_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            question = Question.objects.get(id=question_id)
            comment.question = question
            comment.save()

            return redirect('questions:detail', id=question_id)

    else:
        return redirect('questions:index')

def progress_view(request):
    form = ProgressForm(request.GET)  # GET 요청에서 데이터 가져오기
    primary_percent = 60  # 기본값

    if form.is_valid():
        primary_percent = form.cleaned_data["percent"]

    context = {"form": form, "primary_percent": primary_percent}
    return render(request, "progress.html", context)

def random_link(request):
    questions = Question.objects.all()
    random_num = random.randint(1, len(questions))
    return redirect('questions:detail', id=random_num)