#from django.http import HttpResponse

#def index(request):
#    return HttpResponse("hello hdrb")

from django.shortcuts import render
from .models import Question


def index(request):
    """
    hdrb 목록 출력
    """
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'hdrb/calender.html', context)