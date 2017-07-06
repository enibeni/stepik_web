# -- coding: utf-8 --
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


from .models import QuestionManager
from .models import Question
from .models import Answer
from .forms import QuestionForm, SignUpForm
from .forms import AnswerForm


def test(request, *args, **kwargs):
    return HttpResponse('OK!!!1')


def index(request):
    # questions = Question.objects.order_by('added_at')=
    questions = QuestionManager().new()
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, limit)
    paginator.base_url = '/?page='
    page = paginator.page(page)
    return render(request, 'qa/index.html', {'questions': page.object_list,
                                             'paginator': paginator, 'page': page})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def question(request, pk):
    question = Question.objects.get(pk=pk)
    answers = Answer.objects.filter(question=pk)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.published_date = timezone.now()
            answer.question_id = question.pk
            answer.save()
            return redirect('question', pk=question.pk)
    else:
        form = AnswerForm()
    return render(request, 'qa/question.html', {'question': question,
                                                'answers': answers,
                                                'form': form})


def popular(request):
    popular_questions = QuestionManager().popular()
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(popular_questions, limit)
    paginator.base_url = '/popular/?page='
    page = paginator.page(page)
    return render(request, 'qa/popular.html', {'popular_questions': page.object_list,
                                               'paginator': paginator, 'page': page})


@login_required
def ask(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.published_date = timezone.now()
            question.save()
            return redirect('question', pk=question.pk)
    else:
        form = QuestionForm()
    return render(request, 'qa/ask.html', {'form': form})
