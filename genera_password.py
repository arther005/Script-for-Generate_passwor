import secrets
import string

# the  script for generatte_password

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for i in range(length))
    return password


if request.method == 'GET' and 'generate_password' in request.GET:
    # Handle password generation request
    length = int(request.GET.get('gen_length', 12))
    generated_password = generate_password(length)

    messages.success(request, f'Mot de passe généré: {generated_password}')  

    # Return to users page with generated password in context
    return render(request, 'core/users.html', {
        'users': qs,
        'search_query': search_query,
        'role_choices': UserProfile.ROLE_CHOICES,
        'generated_password': generated_password,
    })
