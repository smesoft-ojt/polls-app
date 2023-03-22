from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from apps.polls.models import PollsQuestion


def index(request):
    latest_question_list = PollsQuestion.objects.order_by('-pub_date')[:5]

    context = {
        'latest_question_list': latest_question_list,
    }
    return render(
        request,
        'polls/index.html',
        context
    )


def detail(request, question_id):

    # question = get_object_or_404(PollsQuestion, pk=question_id)

    try:
        question = PollsQuestion.objects.get(pk=question_id)

    except PollsQuestion.DoesNotExist:
        raise Http404("Question does not exist")

    return render(request, 'polls/detail.html', {'question': question})
