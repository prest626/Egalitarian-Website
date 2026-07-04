from django.shortcuts import render

SAMPLE_EVENTS = [
    {
        'slug': 'blockchain-bootcamp-july-2026',
        'title': 'Blockchain Developer Bootcamp',
        'date': 'July 15–19, 2026',
        'time': '9:00 AM – 5:00 PM WAT',
        'location': 'Egalitarian Computers, No. 24 Oyekola Shopping Complex, Jakande Gate, Oke-Afa Isolo, Lagos',
        'price': 500,
        'capacity': 30,
        'seats_left': 20,
        'type': 'Bootcamp',
        'description': 'An intensive five-day bootcamp covering blockchain fundamentals, smart contract development on Ethereum, and building your first decentralized application. Hands-on labs throughout.',
        'topics': ['Blockchain & distributed ledgers', 'Solidity smart contracts', 'Ethereum ecosystem', 'DApp development with Web3.js', 'Security best practices', 'Live project build'],
    },
    {
        'slug': 'ai-ml-seminar-aug-2026',
        'title': 'AI & Machine Learning Seminar',
        'date': 'August 2, 2026',
        'time': '10:00 AM – 2:00 PM WAT',
        'location': 'Online (Zoom)',
        'price': 0,
        'capacity': 100,
        'seats_left': 50,
        'type': 'Seminar',
        'description': 'A free half-day seminar exploring the current state of artificial intelligence and machine learning. Ideal for professionals curious about where AI fits in their field.',
        'topics': ['What is AI/ML?', 'Supervised vs unsupervised learning', 'Industry applications', 'Tools & frameworks overview', 'Career pathways in AI', 'Q&A with practitioners'],
    },
    {
        'slug': 'cybersecurity-workshop-aug-2026',
        'title': 'Cybersecurity Workshop',
        'date': 'August 20–21, 2026',
        'time': '9:00 AM – 4:00 PM WAT',
        'location': 'Egalitarian Computers, No. 24 Oyekola Shopping Complex, Jakande Gate, Oke-Afa Isolo, Lagos',
        'price': 200,
        'capacity': 25,
        'seats_left': 15,
        'type': 'Workshop',
        'description': 'A practical two-day workshop on cybersecurity fundamentals. Participants will learn to identify common vulnerabilities, understand attacker mindsets, and implement defensive measures.',
        'topics': ['Threat landscape & attack types', 'Network security fundamentals', 'Penetration testing basics', 'Secure coding practices', 'Incident response', 'Hands-on CTF challenge'],
    },
    {
        'slug': 'cloud-computing-seminar-sept-2026',
        'title': 'Cloud Computing for Professionals',
        'date': 'September 10, 2026',
        'time': '11:00 AM – 3:00 PM WAT',
        'location': 'Online (Zoom)',
        'price': 0,
        'capacity': 80,
        'seats_left': 80,
        'type': 'Seminar',
        'description': 'Understand the cloud landscape: AWS, Azure, and GCP compared. This seminar targets professionals looking to understand cloud strategy, cost management, and migration basics.',
        'topics': ['Cloud providers compared', 'IaaS, PaaS, SaaS explained', 'Cost management strategies', 'Migration planning', 'Security in the cloud', 'Certification roadmaps'],
    },
]


def event_list(request):
    event_type = request.GET.get('type', 'All')
    if event_type and event_type != 'All':
        events = [e for e in SAMPLE_EVENTS if e['type'] == event_type]
    else:
        events = SAMPLE_EVENTS
    types = ['All', 'Bootcamp', 'Seminar', 'Workshop']
    return render(request, 'events/event_list.html', {
        'events': events,
        'types': types,
        'active_type': event_type,
    })


def event_detail(request, slug):
    event = next((e for e in SAMPLE_EVENTS if e['slug'] == slug), None)
    if event is None:
        from django.http import Http404
        raise Http404
    return render(request, 'events/event_detail.html', {'event': event})


def event_register(request, slug):
    event = next((e for e in SAMPLE_EVENTS if e['slug'] == slug), None)
    if event is None:
        from django.http import Http404
        raise Http404
    return render(request, 'events/event_register.html', {'event': event})
