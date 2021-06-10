from django.db import models

# Create your models here.
from app_core.models import Chapter


class Quiz(models.Model):
    chapter = models.ForeignKey(Chapter, models.CASCADE)
    total_questions = models.IntegerField()

    def __str__(self):
        return self.chapter.name+" Quiz"

    def get_all_questions(self):
        return self.question_set.all()

    class Meta:
        verbose_name_plural = "quizzes"


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, models.CASCADE)
    question_text = models.CharField(max_length=300, help_text="Set the Question here")
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_text

    def get_question_answers(self):
        return self.answer_set.all()


class Answer(models.Model):
    question = models.ForeignKey(Question, models.CASCADE)
    answer_text = models.CharField(max_length=300, help_text="Set the Choice question here")
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text
