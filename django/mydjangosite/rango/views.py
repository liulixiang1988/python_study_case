from django.shortcuts import render, render_to_response, redirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime

from .models import Category, Page, UserProfile
from .forms import CategoryForm, PageForm, UserForm, UserProfileForm


def decode_url(category_name_url):
    return category_name_url.replace('_', ' ')


def encode_url(category_name):
    return category_name.replace(' ', '_')


def get_category_list():
    cat_list = Category.objects.all()
    for cat in cat_list:
        cat.url = encode_url(cat.name)
    return cat_list


def index(request):
    context = RequestContext(request)
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}

    page_list = Page.objects.order_by('-views')[:5]
    context_dict['pages'] = page_list
    context_dict['cat_list'] = get_category_list()

    for category in category_list:
        category.url = encode_url(category.name)

    if request.session.get('last_visit'):
        last_visit_time = request.session['last_visit']
        visits = request.session.get('visits', 0)

        if (datetime.datetime.now() - datetime.datetime.strptime(last_visit_time[:-7], '%Y-%m-%d %H:%M:%S')).days > 0:
            request.session['visits'] = visits + 1
            request.session['last_visit'] = str(datetime.datetime.now())
    else:
        request.session['visits'] = 1
        request.session['last_visit'] = str(datetime.datetime.now())
    return render_to_response('rango/index.html', context_dict, context)


def about(request):
    return render(request, 'rango/about.html')


def category(request, category_name_url):
    category_name = decode_url(category_name_url)
    context_dict = {'category_name': category_name,
                    'category_name_url': category_name_url}
    try:
        category = Category.objects.get(name=category_name)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        pass

    return render(request, 'rango/cateogry.html', context_dict)


@login_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)  #显示首页
        else:
            print(form.errors)
    else:
        form = CategoryForm()
    return render(request, 'rango/add_category.html', {'form': form})


@login_required
def add_page(request, category_name_url):
    category_name = decode_url(category_name_url)
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            page = form.save(commit=False)

            try:
                cat = Category.objects.get(name=category_name)
                page.category = cat
            except Category.DoesNotExist:
                return redirect(reverse('rango:add_category'))

            page.views = 0
            page.save()
            return redirect(reverse('rango:category', args={category_name_url}))
        else:
            print(form.errors)
    else:
        form = PageForm()
    return render(request, 'rango/add_page.html', {'form': form,
                                                   'category_name_url': category_name_url})


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request, 'rango/register.html', locals())


def user_login(request):
    context_dict = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                if request.session.get('redirect_url', None):
                    redirect_url = request.session['redirect_url']
                    del request.session['redirect_url']
                    return redirect(redirect_url)
                else:
                    return redirect(reverse('rango:index'))
            else:
                context_dict['disabled_account'] = True
                return render(request, 'rango/login.html', context_dict)
        else:
            context_dict['bad_details'] = True
            return render(request, 'rango/login.html', context_dict)
    else:
        if request.GET.get('next', None):
            request.session['redirect_url'] = request.GET['next']
        return render(request, 'rango/login.html', context_dict)


@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('rango:index'))


@login_required
def profile(request):
    context_dict = {'cat_list': get_category_list()}
    u = User.objects.get(username=request.user)

    try:
        up = UserProfile.objects.get(user=u)
    except:
        up = None

    context_dict['user'] = u
    context_dict['userprofile'] = up
    return render(request, 'rango/profile.html', context_dict)


def track_url(request, page_id):
    #page_id = None
    url = '/rango/'
    # if request.method == 'GET':
    #     if 'page_id' in request.GET:
    #         page_id = request.GET['page_id']
    try:
        page = Page.objects.get(id=page_id)
        page.views += 1
        page.save()
        url = page.url
    except:
        pass
    return redirect(url)


@login_required
def like_category(request):
    cat_id = None
    if request.method == 'GET':
        cat_id = request.GET['category_id']

    likes = 0
    if cat_id:
        category = Category.objects.get(id=cat_id)
        if category:
            likes = category.likes + 1
            category.likes = likes
            category.save()
    return HttpResponse(likes)
