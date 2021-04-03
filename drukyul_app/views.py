from django.shortcuts import render
from django.contrib import messages
from .models import Contact, Volunteer, Producer, Director, Adviser, Initiative, News_Update, Blog_CommuniteeStory, \
    BreathingBook, BhutanPage, DrukyulSalon, LockdownRead, StoryTelling, Sponsor_Partner


def home(request):
    intiative = Initiative.objects.filter()[:3]
    news = News_Update.objects.filter()[:3]
    story = Blog_CommuniteeStory.objects.filter()[:3]
    context = {
        'initiatives': intiative,
        'news': news,
        'storys': story
    }

    return render(request, 'index.html', context)


def sponsor(request):
    pp = Sponsor_Partner.objects.filter(sponsor_type='PP')
    vp = Sponsor_Partner.objects.filter(sponsor_type='VP')
    mp = Sponsor_Partner.objects.filter(sponsor_type='MP')
    pp2 = Sponsor_Partner.objects.filter(sponsor_type='PP2')
    sd = Sponsor_Partner.objects.filter(sponsor_type='SD')
    context = {
        'pp':pp,
        'vp':vp,
        'pp2':pp2,
        'mp':mp,
        'sd':sd,

    }
    return render(request, 'sponsors.html', context)


def royal_patron(request):
    return render(request, 'royalpatron.html')


def our_story(request):
    return render(request, 'ourstory.html')


def festival_committee(request):
    advisor = Adviser.objects.all()
    director = Director.objects.all()
    producer = Producer.objects.all()

    context = {
        'advisors': advisor,
        'directors': director,
        'producers': producer
    }

    return render(request, 'festivalcommittee.html', context)


def breathing_book(request):
    queryset = BreathingBook.objects.all().order_by('-date_published')
    context = {
        'breathing_book': queryset
    }
    return render(request, 'breathing_book.html', context)


def community_story(request):
    queryset = Blog_CommuniteeStory.objects.all().order_by('-date_published')
    context = {
        'blogs': queryset
    }
    return render(request, 'community_story.html', context)


def bhutan(request):
    queryset = BhutanPage.objects.all().order_by('-date_published')
    context = {
        'bhutan_pages': queryset
    }
    return render(request, 'bhutan.html', context)


def digital_saloon(request):
    queryset = DrukyulSalon.objects.all().order_by('-date_published')
    context = {
        'digital_saloons': queryset
    }
    return render(request, 'digital_saloon.html', context)


def lockdown_read(request):
    queryset = LockdownRead.objects.all().order_by('-date_published')
    context = {
        'lockdown_reads': queryset
    }
    return render(request, 'lockdown_read.html', context)


def news_update(request):
    queryset = News_Update.objects.all().order_by('-date_published')
    context = {
        'news_updates': queryset
    }
    return render(request, 'news_update.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        try:
            Contact.objects.create(name=name, email=email, phone=phone, message=message)
            messages.success(request, 'Thanks for contacting us! We will back to you soon')
        except:
            messages.error('Something went wrong! sorry try again')

    context = {
        'messages': messages,
    }

    return render(request, 'contact.html', context=None)


def story_telling(request):
    queryset = StoryTelling.objects.all()
    context = {
        'story_tellings': queryset
    }
    return render(request, 'story_telling.html', context)


def volunteer(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        occupation = request.POST['occupation']
        address = request.POST['address']
        try:
            Volunteer.objects.create(name=name, email=email, phone=phone, message=message, occupation=occupation,
                                     address=address)
            messages.success(request, 'Thanks for participating with us! We will back to you soon')
        except:
            messages.error('Something went wrong! sorry try again')
    context = {
        'messages': messages
    }
    return render(request, 'volunteer.html', context=None)


def literature_arts(request):
    return render(request, 'literature_arts.html')


def initiative(request):
    queryset = Initiative.objects.all()
    context = {
        'initiatives': queryset
    }
    return render(request, 'initiative.html', context)


def news_update_detail(request, pk):
    news = News_Update.objects.get(pk=pk)
    context = {
        'news': news
    }
    return render(request, 'news_update_detail.html', context)


def community_story_detail(request, pk):
    blog = Blog_CommuniteeStory.objects.get(pk=pk)
    context = {
        'blog': blog,
    }
    return render(request, 'community_story_detail.html', context)


def lockdown_read_detail(request, pk):
    lockdown_read = LockdownRead.objects.get(pk=pk)
    context = {
        'lockdown_read': lockdown_read,
    }
    return render(request, 'lockdown_read_detail.html', context)


def digital_saloon_detail(request, pk):
    digital_saloon = DrukyulSalon.objects.get(pk=pk)
    context = {
        'digital_saloon': digital_saloon,
    }
    return render(request, 'digital_saloon_detail.html', context)


def initiative_detail(request, pk):
    initiative = Initiative.objects.get(pk=pk)
    context = {
        'initiative': initiative,
    }
    return render(request, 'initiative_detail.html', context)
