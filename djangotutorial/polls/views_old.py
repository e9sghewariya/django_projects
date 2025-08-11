from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
# from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.urls import reverse

from .models import Question, Choice

# Create your views here.

#using loader
# def index(request):
     
#     latest_question_list = Question.objects.order_by("-published_date")[:5]     
#     template = loader.get_template("polls/index.html")
#     context = {"latest_question_list": latest_question_list}
#     return HttpResponse(template.render(context, request))


#using render
def index(request):
    latest_question_list = Question.objects.order_by("-published_date")[:5]    
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)
    

#without using get_object_or_404
# def detail(request, question_id):

# #old way    
# # return HttpResponse("Your're looking at question %s" % question_id)
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExits:
#         raise Http404("Question does not exist")
#     return render(request, "polls/detail.html",{"question":question})

#with using get_object_or_404
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    
    return render(request, "polls/detail.html", {"question": question})

#old 
# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)

#new
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    
    return render(request, "polls/results.html", {"question": question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
          selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
           return render(
               request, "polls/detail.html",
               {
               "question": question,"error_message": "You Didn't select a choice",    
                },
            )
    else:
           selected_choice.votes = F("votes") + 1
           selected_choice.save()
           
    return HttpResponseRedirect(reverse("polls:results", args=(question_id,)))