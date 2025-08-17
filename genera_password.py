import secrets
import string
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserProfile

# Function to generate secure password
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password


# Django view
def users_view(request):
    # Example: query all users (adapt as needed)
    qs = UserProfile.objects.all()
    search_query = request.GET.get('q', '')

    if request.method == 'GET' and 'generate_password' in request.GET:
        # Handle password generation request
        length = int(request.GET.get('gen_length', 12))
        generated_password = generate_password(length)

        messages.success(request, f'Mot de passe généré: {generated_password}')

        return render(request, 'core/users.html', {
            'users': qs,
            'search_query': search_query,
            'role_choices': UserProfile.ROLE_CHOICES,
            'generated_password': generated_password,
        })

    # Default rendering without password generation
    return render(request, 'core/users.html', {
        'users': qs,
        'search_query': search_query,
        'role_choices': UserProfile.ROLE_CHOICES,
    })
