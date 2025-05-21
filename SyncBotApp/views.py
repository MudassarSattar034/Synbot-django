from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import google.generativeai as genai
import markdown
from SyncBotApp.forms import loginUserForm, CreateNewUserForm

# Use API key from settings (which reads from .env)
genai.configure(api_key=settings.GEMINI_API_KEY)

def login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)

        if user is not None:
            if not user.is_superuser:
                auth_login(request, user)
                messages.success(request, 'Login successful')
                return redirect('home')
            else:
                auth_login(request, user)
                messages.error(request, 'You are not authorized to access this page')
                return redirect('login')
                
        else:
            messages.error(request, 'Invalid email or password')
            return redirect('login')
    
    context = {
        "form": loginUserForm(),
    }
    
    return render(
        request=request, 
        template_name='login.html', 
        context=context
        )

def sign_up(request):

    if request.method == 'POST':
        form = CreateNewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            auth_user = authenticate(username=username, password=password)

            if auth_user is not None:
                auth_login(request, auth_user)
                messages.success(request, 'Account created successfully')
                return redirect('home')
            else:
                messages.error(request, 'Authentication failed after signup')
                return redirect('sign_up')
        else:
            messages.error(request, 'Error creating account')
            
    context = {
        "form": CreateNewUserForm(),
    }
    
    return render(
        request=request, 
        template_name='sign-up.html', 
        context=context
        )

def logout(request):
    if request.method == 'POST':
        auth_logout(request)
        messages.success(request, 'Logout successful')
        return redirect('login')
    
    messages.error(request, 'Logout failed')
    return redirect(request.META.get('HTTP_REFERER', 'login'))

def index(request):
    return render(request, 'chat/index.html')

def home(request):
    return render(request, 'chat/home.html')

@csrf_exempt
def get_response(request):
    if request.method == 'POST':
        user_message = request.POST.get('message')

        try:
            model = genai.GenerativeModel('models/gemini-1.5-flash-latest')
            response = model.generate_content(user_message)
            bot_reply = response.text.strip()

            # Convert Markdown response to HTML
            bot_reply_html = markdown.markdown(bot_reply)
        except Exception as e:
            bot_reply_html = f"Error from Gemini: {str(e)}"

        return JsonResponse({'response': bot_reply_html})


@login_required
def user_profile(request):
    return render(request, 'chat/profile.html', {'user': request.user})

    logout(request)
    return redirect('index')