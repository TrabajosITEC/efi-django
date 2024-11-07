from cars.models import Category 
from users.models import Profile

def all_names_categories(request):
    categories = Category.objects.all()
    names = [category.name for category in categories]
    return dict(
        names_categories = names
    )

def current_username(request):
    return dict(
        username = request.user

    )

def profile_language(request, ):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
    else:
        profile = None

    return dict(
        profile = profile

    )