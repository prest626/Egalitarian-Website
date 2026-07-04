from django.shortcuts import render
from django.contrib.auth.decorators import login_required

SAMPLE_EXAM = {
    'title': 'Web Development with Django — Final Exam',
    'duration_minutes': 60,
    'passing_score': 70,
    'questions': [
        {
            'id': 1,
            'text': 'Which Django component is responsible for mapping URLs to views?',
            'choices': [
                {'id': 'a', 'text': 'URLconf (urls.py)'},
                {'id': 'b', 'text': 'settings.py'},
                {'id': 'c', 'text': 'models.py'},
                {'id': 'd', 'text': 'admin.py'},
            ],
        },
        {
            'id': 2,
            'text': 'What does the Django ORM stand for?',
            'choices': [
                {'id': 'a', 'text': 'Object-Relational Mapper'},
                {'id': 'b', 'text': 'Online Resource Manager'},
                {'id': 'c', 'text': 'Output Rendering Module'},
                {'id': 'd', 'text': 'Optimized Request Method'},
            ],
        },
        {
            'id': 3,
            'text': 'Which template tag is used to extend a base template in Django?',
            'choices': [
                {'id': 'a', 'text': '{% extends "base.html" %}'},
                {'id': 'b', 'text': '{% include "base.html" %}'},
                {'id': 'c', 'text': '{% inherit "base.html" %}'},
                {'id': 'd', 'text': '{% load "base.html" %}'},
            ],
        },
    ],
}


@login_required
def exam_take(request, slug):
    return render(request, 'exams/exam_take.html', {'exam': SAMPLE_EXAM, 'course_slug': slug})


@login_required
def exam_result(request, slug):
    result = {
        'score': 85,
        'passing_score': SAMPLE_EXAM['passing_score'],
        'passed': True,
        'total_questions': len(SAMPLE_EXAM['questions']),
        'correct': 3,
        'exam': SAMPLE_EXAM,
    }
    return render(request, 'exams/exam_result.html', {'result': result, 'course_slug': slug})
