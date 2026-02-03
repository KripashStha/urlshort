from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta
from .models import ShortURL
from .forms import CreateNewShortURL, SignUpForm, EditURLForm
import string

# base62 characters for generating short urls
BASE62_CHARS = string.ascii_letters + string.digits

# function to generate base62 short code
def generate_short_code(length=6):
    import random
    code = ''
    for i in range(length):
        code = code + random.choice(BASE62_CHARS)
    return code

# home page view
def home(request):
    return render(request, 'home.html')

# redirect to original url and track clicks
def redirect_url(request, url):
    try:
        url_obj = ShortURL.objects.get(short_url=url)
        
        # check if url has expired
        if url_obj.is_expired():
            return render(request, 'expired.html', {'obj': url_obj})
        
        # increment the click count
        url_obj.click_count = url_obj.click_count + 1
        url_obj.save()
        context = {'obj': url_obj}
        return render(request, 'redirect.html', context)
    except ShortURL.DoesNotExist:
        return render(request, 'pagenotfound.html')

# create new short url - only for logged in users
@login_required
def createShortURL(request):
    if request.method == 'POST':
        form = CreateNewShortURL(request.POST)
        if form.is_valid():
            original_url = form.cleaned_data['original_url']
            custom_code = form.cleaned_data.get('custom_code', '').strip()
            
            # check if user provided custom code
            if custom_code:
                # check if custom code already exists
                if ShortURL.objects.filter(short_url=custom_code).exists():
                    messages.error(request, 'This custom URL is already taken. Try another one.')
                    return render(request, 'create.html', {'form': form})
                short_code = custom_code
            else:
                # generate unique short code using base62
                short_code = generate_short_code()
                # make sure its unique
                while ShortURL.objects.filter(short_url=short_code).exists():
                    short_code = generate_short_code()
            
            # create the new url object
            new_url = ShortURL(
                original_url=original_url,
                short_url=short_code,
                user=request.user
            )
            
            # set expiration if user selected one
            expiration_hours = form.cleaned_data.get('expiration', '')
            if expiration_hours:
                new_url.expires_at = timezone.now() + timedelta(hours=int(expiration_hours))
            
            new_url.save()
            
            return render(request, 'urlcreated.html', {'chars': short_code})
    else:
        form = CreateNewShortURL()
    
    return render(request, 'create.html', {'form': form})

# view all urls for the logged in user
@login_required
def my_urls(request):
    urls = ShortURL.objects.filter(user=request.user).order_by('-time_date_created')
    return render(request, 'my_urls.html', {'urls': urls})

# edit an existing url
@login_required
def edit_url(request, url_id):
    url_obj = get_object_or_404(ShortURL, id=url_id, user=request.user)
    
    if request.method == 'POST':
        form = EditURLForm(request.POST, instance=url_obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'URL updated successfully!')
            return redirect('my_urls')
    else:
        form = EditURLForm(instance=url_obj)
    
    return render(request, 'edit_url.html', {'form': form, 'url_obj': url_obj})

# delete a url
@login_required
def delete_url(request, url_id):
    url_obj = get_object_or_404(ShortURL, id=url_id, user=request.user)
    
    if request.method == 'POST':
        url_obj.delete()
        messages.success(request, 'URL deleted!')
        return redirect('my_urls')
    
    return render(request, 'delete_confirm.html', {'url_obj': url_obj})

# user registration view
def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('home')
    else:
        form = SignUpForm()
    
    return render(request, 'register.html', {'form': form})

# logout view
def logout_user(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('home')
