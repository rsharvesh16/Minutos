#
# Import functionality from Django

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.sessions.models import Session
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings

#
#

from apps.team.models import Invitation
from apps.userprofile.models import Userprofile


#
# Views

def frontpage(request):
    return render(request, 'core/frontpage.html')

def privacy(request):
    return render(request, 'core/privacy.html')

def terms(request):
    return render(request, 'core/terms.html')

def plans(request):
    return render(request, 'core/plans.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.email = user.username
            user.save()

            # userprofile = Userprofile.objects.create(user=request.user)

            login(request, user)

            invitations = Invitation.objects.filter(email=user.email, status=Invitation.INVITED)

            if invitations:
                return redirect('accept_invitation')
            else:
                return redirect('dashboard')
    else:
        form = UserCreationForm()

    return render(request, 'core/signup.html', {'form': form})




User = get_user_model()

def is_user_logged_in(request, username):
    try:
        user = User.objects.get(username=username)
        

        if user.active == True:
            is_logged_in = True
        else:
            is_logged_in = False
     

        return JsonResponse({'username': username, 'is_logged_in': is_logged_in})
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)
