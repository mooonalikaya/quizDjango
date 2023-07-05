from django.contrib import admin
from .models import Quiz, Question, Answer

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display=['title']

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display=['title',]

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display=['title',]