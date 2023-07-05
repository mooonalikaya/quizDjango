from django.db import models
class Quiz(models.Model):
    title=models.CharField(max_length=100,verbose_name="Название")
    desc=models.TextField(max_length=400,verbose_name="Описание")

    def __str__(self) -> str:
        return f"{self.title} | {self.desc}"
    
    class Meta:
        verbose_name="Тест"
        verbose_name_plural="Тесты"


class Question(models.Model):
    title=models.CharField(max_length=100,verbose_name="Название")
    quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE,verbose_name="Тест",related_name="question_list")


    def __str__(self) -> str:
        return f"{self.title} | {self.quiz}"
    
    class Meta:
        verbose_name="Вопрос"
        verbose_name_plural="Вопросы"

class Answer(models.Model):
    title=models.CharField(max_length=100,verbose_name="Название")
    question=models.ForeignKey(Question,on_delete=models.SET_NULL,null=True,verbose_name="Вопрос",related_name="list_answer")
    is_current=models.BooleanField(default=False,verbose_name="Вариант правильный")

    def __str__(self) -> str:
        return f"{self.title} | {self.question} | {self.is_current}"
    
    class Meta:
        verbose_name="Ответ"
        verbose_name_plural="Ответы"