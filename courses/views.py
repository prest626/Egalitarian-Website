from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

SAMPLE_COURSES = [
    {
        'slug': 'full-stack-web-development',
        'title': 'Full Stack Web Development',
        'price': 700,
        'category': 'Programming',
        'description': 'Master both front-end and back-end development. Build complete, production-ready web applications from scratch using modern tools and frameworks.',
        'syllabus': 'HTML & CSS fundamentals, JavaScript & TypeScript, React, Node.js, Databases (SQL & NoSQL), REST APIs, Deployment & DevOps basics.',
        'duration': '16 weeks',
        'level': 'Beginner to Advanced',
    },
    {
        'slug': 'web-development-django',
        'title': 'Web Development with Django',
        'price': 350,
        'category': 'Programming',
        'description': 'Learn to build powerful, scalable web applications using Django, Python\'s premier web framework. Covers models, views, templates, authentication, and deployment.',
        'syllabus': 'Python refresher, Django project setup, ORM & models, Views & URLs, Templates, Forms, Authentication, REST with DRF, Deployment on Linux.',
        'duration': '8 weeks',
        'level': 'Intermediate',
    },
    {
        'slug': 'data-analysis-python',
        'title': 'Data Analysis Using Python',
        'price': 300,
        'category': 'Programming',
        'description': 'Transform raw data into actionable insights. Learn pandas, NumPy, Matplotlib, and Seaborn to clean, analyze, and visualize datasets effectively.',
        'syllabus': 'Python for data science, NumPy, pandas DataFrames, Data cleaning, Exploratory data analysis, Matplotlib & Seaborn, Intro to machine learning.',
        'duration': '6 weeks',
        'level': 'Beginner to Intermediate',
    },
    {
        'slug': 'computer-vision-opencv',
        'title': 'Computer Vision with OpenCV',
        'price': 600,
        'category': 'Programming',
        'description': 'Dive into the world of computer vision. Learn to process images and video, detect objects, and build intelligent visual recognition systems.',
        'syllabus': 'Image processing fundamentals, OpenCV core operations, Feature detection, Object detection & tracking, Deep learning for vision, Real-world projects.',
        'duration': '10 weeks',
        'level': 'Advanced',
    },
    {
        'slug': 'desktop-publishing',
        'title': 'Desktop Publishing',
        'price': 60,
        'category': 'Business',
        'description': 'Create professional-quality print and digital publications. Master layout, typography, and design principles using industry-standard tools.',
        'syllabus': 'Layout principles, Typography, Color theory, Adobe InDesign basics, Creating brochures, flyers, and newsletters, Print vs digital publishing.',
        'duration': '3 weeks',
        'level': 'Beginner',
    },
    {
        'slug': 'front-end-web-development',
        'title': 'Front End Web Development',
        'price': 500,
        'category': 'Web Design',
        'description': 'Build beautiful, responsive user interfaces. Master HTML, CSS, JavaScript, and modern frameworks to craft engaging web experiences.',
        'syllabus': 'HTML5 semantic structure, CSS3 & Flexbox/Grid, Responsive design, JavaScript ES6+, DOM manipulation, React fundamentals, Performance optimization.',
        'duration': '10 weeks',
        'level': 'Beginner to Intermediate',
    },
    {
        'slug': 'basic-blockchain-developer-bootcamp',
        'title': 'Basic Blockchain Developer Bootcamp',
        'price': 500,
        'category': 'Programming',
        'description': 'Get started in blockchain development. Understand distributed ledger technology, consensus mechanisms, and write your first smart contracts.',
        'syllabus': 'Blockchain fundamentals, Cryptography basics, Ethereum & Solidity, Smart contracts, Testing & deployment, Web3.js, DApp overview.',
        'duration': '8 weeks',
        'level': 'Beginner',
    },
    {
        'slug': 'advanced-blockchain-developer-bootcamp',
        'title': 'Advanced Blockchain Developer Bootcamp',
        'price': 500,
        'category': 'Programming',
        'description': 'Go deeper into blockchain engineering. Build complex DeFi protocols, NFT platforms, and multi-chain applications with advanced Solidity patterns.',
        'syllabus': 'Advanced Solidity patterns, DeFi protocols, NFTs & ERC standards, Layer 2 solutions, Security auditing, Multi-sig wallets, Full DApp projects.',
        'duration': '10 weeks',
        'level': 'Advanced',
    },
    {
        'slug': 'data-analysis',
        'title': 'Data Analysis',
        'price': 300,
        'category': 'Programming',
        'description': 'A comprehensive introduction to data analysis concepts, tools, and workflows. Ideal for those moving into data-driven roles.',
        'syllabus': 'Data types & sources, Spreadsheet analysis, SQL basics, Python introduction, Statistical thinking, Reporting & dashboards.',
        'duration': '5 weeks',
        'level': 'Beginner',
    },
]

CATEGORIES = ['All', 'Programming', 'Web Design', 'Business', 'Language', 'Film & Video', 'Photography']


def course_list(request):
    category = request.GET.get('category', 'All')
    if category and category != 'All':
        courses = [c for c in SAMPLE_COURSES if c['category'] == category]
    else:
        courses = SAMPLE_COURSES
    return render(request, 'courses/course_list.html', {
        'courses': courses,
        'categories': CATEGORIES,
        'active_category': category,
    })


def course_detail(request, slug):
    course = next((c for c in SAMPLE_COURSES if c['slug'] == slug), None)
    if course is None:
        from django.http import Http404
        raise Http404
    course = dict(course)
    course['syllabus_items'] = [item.strip() for item in course['syllabus'].split(',')]
    return render(request, 'courses/course_detail.html', {'course': course})


@login_required
def enroll(request, slug):
    course = next((c for c in SAMPLE_COURSES if c['slug'] == slug), None)
    if course is None:
        from django.http import Http404
        raise Http404
    return render(request, 'courses/enroll.html', {'course': course})
