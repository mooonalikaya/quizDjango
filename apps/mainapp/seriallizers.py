from rest_framework import serializers
from .models import Quiz,Question,Answer
class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model=Quiz
        fields=['id','title','desc']

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Question
        fields=['id','title','quiz']

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Answer
        fields=['id','title','question','is_current']

class GetQuestionSerializer(serializers.ModelSerializer):
    list_answer=AnswerSerializer(many=True)

    class Meta:
        model=Question
        fields=['id','title','list_answer']


class GetQuizSerializer(serializers.ModelSerializer):
    question_list=GetQuestionSerializer(many=True)

    class Meta:
        model=Quiz
        fields=['id','title','desc','question_list']