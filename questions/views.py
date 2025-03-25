from django.shortcuts import render,redirect
from .forms import QuestionForm, CommentForm
from .models import Question, Comment

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
    
    context = {
        "primary_percent": primary_percent,  # 파란색 진행률
        "danger_percent": danger_percent,   # 빨간색 진행률
    }
    return render(request, "progress.html", context)