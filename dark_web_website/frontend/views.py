from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from dark_web_website.api.models import vehicleStatus
from django.contrib.auth.decorators import login_required
from dark_web_website.frontend.forms import SignUpForm, LoginForm
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import login
from django.contrib.auth import authenticate
import json

def indexView(request):
    template_name = 'index.html'
    return render(request, 'default.html', {'page': template_name})

def statusView(request):
    if request.user.is_active:
        vehicleid = request.user.profile.vehicle_id
        vehicle_statusses = vehicleStatus.objects.filter(vehicleid=vehicleid)
        args = {'page':'status.html', 'vehicle_statusses': vehicle_statusses, 'vehicleid':vehicleid}
        return render(request, 'default.html', args)
    else:
        args = {'page': 'status.html', 'vehicle_statusses': None, 'vehicleid': None }
        return render(request, 'default.html', args)

def registerView(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # user can't login until link confirmed
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your connected vehicles Account'
            message = render_to_string('registration/account-activation-email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            })
            user.email_user(subject, message)
            return redirect('account-activation-send')
    else:
        form = SignUpForm()
        return render(request, 'default.html', {'page': 'registration/register.html', 'form': form})

def loginView(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    return redirect('/status')
                else:
                    form = LoginForm
                    return render(request, 'default.html', {'page': 'registration/login.html', 'form': form, 'error': 'Account is not activated'})
            else:
                form = LoginForm
                return render(request, 'default.html', {'page': 'registration/login.html', 'form': form, 'error': 'Your username and password were incorrect.'})
        except:
            form = LoginForm
            return render(request, 'default.html', {'page': 'registration/login.html', 'form': form, 'error': 'Invalid Form'})

    else:
        form = LoginForm
        return render(request, 'default.html', {'page': 'registration/login.html', 'form': form, 'error': ""})