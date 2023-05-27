from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from .helper import quiz_json
from .models import Quiz
# Create your views here.
class CreateQuiz(APIView):
    def post(self, request):
        data = request.data
        
        # Extract Required Fields
        question = data.get('question')
        options = data.get('options')
        right_answer = data.get('right_answer')
        status = data.get('static')
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        
        quiz = Quiz()
        quiz.question = question
        quiz.options = options
        quiz.right_answer = right_answer
        quiz.status = status
        quiz.start_date = start_date
        quiz.end_date = end_date
        quiz.save()
        return Response({"quiz": quiz_json(quiz)})
    

def change_status():
    pass