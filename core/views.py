from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home(request):
    featured_courses = [
        {'title': 'Full Stack Web Development', 'price': 700, 'slug': 'full-stack-web-development', 'category': 'Programming'},
        {'title': 'Web Development with Django', 'price': 350, 'slug': 'web-development-django', 'category': 'Programming'},
        {'title': 'Data Analysis Using Python', 'price': 300, 'slug': 'data-analysis-python', 'category': 'Programming'},
        {'title': 'Computer Vision with OpenCV', 'price': 600, 'slug': 'computer-vision-opencv', 'category': 'Programming'},
        {'title': 'Front End Web Development', 'price': 500, 'slug': 'front-end-web-development', 'category': 'Web Design'},
        {'title': 'Desktop Publishing', 'price': 60, 'slug': 'desktop-publishing', 'category': 'Business'},
    ]
    upcoming_events = [
        {'title': 'Blockchain Developer Bootcamp', 'date': '2026-07-15', 'price': 500, 'slug': 'blockchain-bootcamp-july', 'seats_left': 20},
        {'title': 'AI & Machine Learning Seminar', 'date': '2026-08-02', 'price': 0, 'slug': 'ai-ml-seminar-aug', 'seats_left': 50},
        {'title': 'Cybersecurity Workshop', 'date': '2026-08-20', 'price': 200, 'slug': 'cybersecurity-workshop-aug', 'seats_left': 15},
    ]
    stats = {
        'countries': 150,
        'graduates': '28,000',
        'staff': 750,
        'courses': '1,200',
    }
    return render(request, 'core/home.html', {
        'featured_courses': featured_courses,
        'upcoming_events': upcoming_events,
        'stats': stats,
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
    enrollments = []
    notifications = []
    return render(request, 'core/dashboard.html', {
        'enrollments': enrollments,
        'notifications': notifications,
    })


@login_required
def notifications(request):
    notifications = []
    return render(request, 'core/notifications.html', {'notifications': notifications})
