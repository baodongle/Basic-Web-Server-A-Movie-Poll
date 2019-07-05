from django.shortcuts import get_object_or_404, render

from .models import Question


def index(request):
    """The home page displays the latest few questions."""
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'IntekMovieFridayPoll/index.html', context)


def detail(request, question_id):
    """Displays a question text, with no results but with a form to vote."""
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'IntekMovieFridayPoll/detail.html', {'question': question})


def results(request, question_id):
    """Displays results for a particular question."""
    return render(request, f"You're looking at the results of question {question_id}.")


def vote(request, question_id):
    """Handles voting for a particular choice in a particular question."""
    return render(request, f"You're voting on question{question_id}.")
