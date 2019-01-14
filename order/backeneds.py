from django.contrib.auth.models import User


def authenticate(username=None, password=None):
    try:
        user = User.objects.get(email=username)
    except User.MultipleObjectsReturned:
        # if user have more than one Email
        user = User.objects.filter(email=username).order_by('id').first()
    except User.DoesNotExist:
        return None

    if getattr(user, 'is_active') and user.check_password(password):
        return user
    return None


def get_user(self, user_id):
    try:
        user = User.objects.get(pk=user_id)
        return user
    except User.DoesNotExist:
        return None