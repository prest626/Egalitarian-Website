from urllib.parse import quote

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST

from courses.models import Course
from events.models import Event


def home(request):
    featured_courses = Course.objects.all()[:6]
    upcoming_events = Event.objects.all()[:3]
    stats = {
        'countries': 150,
        'graduates': '28,000',
        'staff': 750,
        'courses': '1,200',
    }
    build_message = quote(
        "Hello Egalitarian Computers! I'd like to discuss a software project "
        "with your engineering team."
    )
    build_whatsapp_url = f'https://wa.me/{settings.WHATSAPP_NUMBER}?text={build_message}'
    return render(request, 'core/home.html', {
        'featured_courses': featured_courses,
        'upcoming_events': upcoming_events,
        'stats': stats,
        'build_whatsapp_url': build_whatsapp_url,
    })


def about(request):
    team = [
        {'name': 'Michael Nnadi', 'role': 'Co-Founder & CEO', 'bio': 'A serial entrepreneur and investor leading Egalitarian Computers toward its mission of democratizing tech education across Africa and beyond.'},
        {'name': 'Edwin Osamezu', 'role': 'Co-Founder & Lead Instructor', 'bio': 'An experienced educator with decades of training and workshop facilitation, driving the curriculum and learner outcomes at Tech Egalitarian.'},
    ]
    return render(request, 'core/about.html', {'team': team})


def contact(request):
    return render(request, 'core/contact.html')


@login_required
def dashboard(request):
    enrollments = request.user.enrollments.select_related('course')
    notifications = request.user.notifications.all()[:5]
    return render(request, 'core/dashboard.html', {
        'enrollments': enrollments,
        'notifications': notifications,
    })


@login_required
def notifications(request):
    notifications = request.user.notifications.all()
    return render(request, 'core/notifications.html', {'notifications': notifications})


@login_required
@require_POST
def mark_all_notifications_read(request):
    request.user.notifications.filter(is_read=False).update(is_read=True)
    return redirect('notifications')
