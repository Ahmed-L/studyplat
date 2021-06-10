from django.shortcuts import render, get_list_or_404
from .models import Quiz


class MCQ:
    def __init__(self, question, answers):
        self.question = question
        self.answers = answers

    def __str__(self):
        return self.question


# Create your views here.
def quiz_view(request, name):
    context = {}
    total = 0
    obj = Quiz.objects.filter(chapter__exact=name)
    # obj = get_list_or_404(Quiz, chapter=name)
    mcq_list = []
    for q in obj[0].get_all_questions():
        total += 1
        answers = []
        for a in q.get_question_answers():
            answers.append(a)

        mcq_list.append(MCQ(q.question_text, answers))

    context = {'mcq_list': mcq_list, 'total': total, 'chapter': name}
    return render(request, 'quiz/quiz.html', context)
