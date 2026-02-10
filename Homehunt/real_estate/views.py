from django.shortcuts import render, get_object_or_404
from .models import Property, Favourite
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q


# Create your views here.
def index(request):
    query = request.GET.get("q")
    if query:
        properties = Property.objects.filter(
            Q(name__icontains=query) | Q(location__icontains=query)
        )
    else:
        properties = Property.objects.all()

    context = {"properties": properties}

    return render(request, "index.html", context)


# def property_detail(request, pk):
#     prop = get_object_or_404(Property, pk=pk)
#     return render(request, "property_detail.html", {"property": prop})
def property_detail(request, pk):
    prop = get_object_or_404(Property, pk=pk)

    is_favourite = False
    if request.user.is_authenticated:
        is_favourite = Favourite.objects.filter(
            user=request.user, property=prop
        ).exists()

    return render(
        request,
        "property_detail.html",
        {
            "property": prop,
            "is_favourite": is_favourite,
        },
    )


@login_required
def toggle_favourite(request, pk):
    prop = get_object_or_404(Property, pk=pk)

    fav, created = Favourite.objects.get_or_create(
        user=request.user,
        property=prop,
    )

    if not created:
        fav.delete()  # remove from favourite

    return redirect("property_detail", pk=pk)


@login_required
def favourite_list(request):
    favourites = Favourite.objects.filter(user=request.user)
    return render(request, "favourites.html", {"favourites": favourites})


# SIGNUP
def signup_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect("signup")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("signup")

        user = User.objects.create_user(username=username, password=password1)
        messages.success(request, "Account created successfully. Please login.")
        return redirect("login")

    return render(request, "signup.html")


# LOGIN
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # Redirect to next page if exists
            next_url = request.GET.get("next")
            if next_url:
                return redirect(next_url)

            # Otherwise go to favourites page
            return redirect("favourite_list")

        else:
            messages.error(request, "Invalid username or password")
            return redirect("login")

    return render(request, "login.html")


# LOGOUT
def logout_view(request):
    logout(request)
    return redirect("index")
