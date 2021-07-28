from django.shortcuts import render
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .models import Menu, Project, Banner, Team, Service, Feature, Setting

# Create your views here.

menu = Menu.objects.all()
project = Project.objects.all()
banner = Banner.objects.all()
team = Team.objects.all()
service = Service.objects.all()
feature = Feature.objects.all()
setting = Setting.objects.all()

def index(request):
    
    if request.method == 'POST':
        searched = request.POST.get('search')
        search_resoult = Menu.objects.filter(title = searched)
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        ctx = {
           'name': name,
           'phone': phone,
           'email': email,
           'subject': subject,
           'message': message
        }
        
        message = render_to_string('mail.html', ctx)

        send_mail(
            subject,
            message,
            'doston.3401@gmail.com',
            ['doston.davronbekovich@gmail.com'],
            fail_silently=False, 
            html_message=message,
        )
        return render( request, 'index.html', {'menus': menu, 'projects': project, 'banners': banner, 'teams': team, 'services': service, 'features': feature, 'settings': setting, 'searchs': search_resoult })

    else:
        return render( request, 'index.html', {'menus': menu, 'projects': project, 'banners': banner, 'teams': team, 'services': service, 'features': feature, 'settings': setting })
