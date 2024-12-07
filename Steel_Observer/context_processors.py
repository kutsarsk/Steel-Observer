from Steel_Observer.accounts.models import AppUser


def user_is_authenticated(request):
    return {'authenticated': request.user.is_authenticated}


def user_is_staff(request):
    return {'staff': request.user.is_staff}


def user_is_superuser(request):
    return {'superuser': request.user.is_superuser}