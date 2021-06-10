from django.contrib import admin
from .models import Quiz, Question, Answer


# Register your models here.


class AnswerTabular(admin.TabularInline):
    model = Answer


class QuestionTabular(admin.TabularInline):
    model = Question


class QuestionChannel(admin.ModelAdmin):
    inlines = [AnswerTabular]
    extra = 1


admin.site.register(Question, QuestionChannel)
# admin.site.register(Answer)
admin.site.register(Quiz)
