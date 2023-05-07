"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from .forms import FeedbackForm
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.db import models
from .models import *
from .forms import *

def home(request):
    """Renders the home page."""
    posts = Blog.objects.all().order_by('-posted')[:3]
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'posts': posts,
            'title':'Главная страница',
            'year':datetime.now().year,
        }
    )

def catalog(request):
    """Renders the home page."""
    products = Catalog.objects.all()
    employers = Employer.objects.all()

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/catalog.html',
        {
            'products': products,
            'employers': employers,
            'title':'Каталог',
            'year':datetime.now().year,
        }
    )

def catalog_buy(request, product_pk):
    """Renders the home page."""
    all_products = Catalog.objects.all()
    employers = Employer.objects.all()
    return render(
        request,
        'app/basket.html',
        {
            'title': 'Корзина',
            'product_id': product_pk,
            'all_products': all_products,
            'employers': employers,
            'year': datetime.now().year,
            'times': [
                ["08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00"],
                ["08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00"],
                ["08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00"],
                ["08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00"],
                ["08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00"],
                ["08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00"],
                ["08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00"],
                ["08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00"],
                ["08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00"],
                ["08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00"],
                ["08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00"],
                ["08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00"],
                ["08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00"],
                ["08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00"],
                ["08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00"],
                ["08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00"],
                ["08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00"],
                ["08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00"],
                ["08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00"],
                ["08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00"],
                ["08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00"],
                ["08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00"],
                ["08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00"],
                ["08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00"],
                ["08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00"],
                ["08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00"],
                ["08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00"],
                ["08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00"],
                ["08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00"],
                ["08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00"],
            ]
        }
    )

def add_product(request):
    """Renders the home page."""
    products = Catalog.objects.all()

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/add_product.html',
        {
            'products': products,
            'title':'Редактирование каталога',
            'year': datetime.now().year,
        }
    )

def del_product(request, product_id):
    """Renders the home page."""
    if request.user.is_superuser:
        product = Catalog.objects.get(id=product_id)
        product.delete()
    return redirect('add_product')


def del_post(request, post_id):
    """Renders the home page."""
    if request.user.is_superuser:
        post = Blog.objects.get(id=post_id)
        post.delete()
    return redirect('blog')


def create_product(request):
    if request.method == "POST": # после отправки формы
        prodform = ProductForm(request.POST, request.FILES)
        if prodform.is_valid(): #валидация полей формы
            prod_f = prodform.save(commit=False) # не сохраняем автоматически данные формы
            prod_f.save() # сохраняем изменения после добавления данных
            return redirect('catalog') # переадресация на главную страницу после регистрации
        else:
            print(prodform.data)
            print(prodform.media)
            print('NOT VALID')
    else:
        prodform = ProductForm() # создание объекта формы для ввода данных нового пользователя
    return render(
        request,
        'app/create_product.html',
        {
            'prodform': prodform, # передача формы в шаблон веб-страницы
            'title': 'Добавление услуги',
            'year':datetime.now().year,
        }
    )

# def basket(request):
#     assert isinstance(request, HttpRequest)
#     if not request.user.is_authenticated:
#         return redirect('registration')
#     basket = Service_basket.objects.filter(user_id=request.user.pk)
#     total = 0
#     for item in basket:
#         total += item.price
#     return render(
#         request,
#         'app/basket.html',
#         {
#             'total': total,
#             'title':'Запись',
#             'year':datetime.now().year,
#         }
#     )

def orders(request):
    assert isinstance(request, HttpRequest)
    if not request.user.is_authenticated:
        return redirect('registration')
    orders = Order.objects.filter(user_id=request.user.pk)[::-1]
    products_all = Catalog.objects.all()
    employers = Employer.objects.all()
    total = 0
    for order in orders:
        total += order.price

    return render(
        request,
        'app/orders.html',
        {
            'total': total,
            'products_all': products_all,
            'employers': employers,
            'orders': orders,
            'title':'Мои заказы',
            'year':datetime.now().year,
        }
    )

def make_order(request, product_id):
    assert isinstance(request, HttpRequest)
    if not request.user.is_authenticated:
        return redirect('registration')
    product = Catalog.objects.get(id=product_id)

    if request.method == "POST":
        print(request.POST['datetimepicker'])
        print(type(request.POST['datetimepicker']))
        date_time = datetime.strptime(request.POST['datetimepicker'], '%Y/%m/%d %H:%M')

        order = Order(user_id=request.user.pk, product_id=product_id,
                      price=product.price, employer_id=request.POST['dropdown'], date=date_time)
        order.save()

    #     form = OrderForm(request.POST)
    #     if form.is_valid():
    #         order_f = form.save(commit=False)
    #         order_f.user_id = request.user.pk
    #         order_f.product_id = product_id
    #         order_f.price = product.price
    #         order_f.employer_id = request.POST['dropdown']
    #         order_f.date = datetime.now()
    #         order_f.status = 'заказано'
    #         order_f.save()
    #         print('valid')
    #     else:
    #         print(request.user.pk)
    #         print(product_id)
    #         print(product.price)
    #         # print(request.POST)
    #         print(request.POST['dropdown'])
    #         print(datetime.today())
    #         print('no valid')
    #
    #         return redirect('orders')
    # else:
    #     form = OrderForm()

    return redirect('orders')


def manage_orders(request):
    assert isinstance(request, HttpRequest)
    if not request.user.is_authenticated and not request.user.is_staff:
        return redirect('registration')
    orders = Order.objects.all()
    products_all = Catalog.objects.all()
    users_all = User.objects.all()
    # print(users_all.get(1))
    # <h4> Заказал: {{ users_all.get(pk=product.user_id) }} </h4>
    total = 0
    for order in orders:
        total += order.price

    return render(
        request,
        'app/manage_orders.html',
        {
            'users_all': users_all,
            'total': total,
            'products_all': products_all,
            'orders': orders,
            'title':'Заказы',
            'year':datetime.now().year,
        }
    )

def change_order(request, order_id, status):
    assert isinstance(request, HttpRequest)
    if not request.user.is_authenticated and not request.user.is_staff:
        return redirect('registration')
    order = Order.objects.get(id=order_id)
    order.status = status
    order.save()
    return redirect('manage_orders')


def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Контакты',
            'message':'Страница с нашими контактами.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    employers = Employer.objects.all()
    return render(
        request,
        'app/about.html',
        {
            'title':'О нас',
            'employers': employers,
            'message':'Лучшая студия в городе',
            'year':datetime.now().year,
        }
    )

def links(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/links.html',
        {
            'title':'Полезные ресурсы',
            'message':'Рецепты',
            'year':datetime.now().year,
        }
    )

def anketa(request):
    assert isinstance(request, HttpRequest)
    data = None
    gender = {'1': 'Мужчина', '2': 'Женщина'}
    coffee = {'1': 'Каждый день', '2': 'Несколько раз в неделю', '3': 'Несколько раз в месяц', '4': 'Не пью'}
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            data = dict()
            data['name'] = form.cleaned_data['name']
            data['city'] = form.cleaned_data['city']
            data['job'] = form.cleaned_data['job']
            data['gender'] = gender[form.cleaned_data['gender'] ]
            data['coffee'] = coffee[form.cleaned_data['coffee'] ]
            if(form.cleaned_data['notice'] == True):
                data['notice'] = 'Да'
            else:
                data['notice'] = 'Нет'
            data['email'] = form.cleaned_data['email']
            data['message'] = form.cleaned_data['message']
            form = None
    else:
        form = FeedbackForm()
    return render(
            request,
            'app/anketa.html',
            {
                'form':form,
                'data':data,
                }
           )

def registration(request):
    assert isinstance(request, HttpRequest)
    if request.method == "POST": # после отправки формы
        regform = UserCreationForm (request.POST)
        if regform.is_valid(): #валидация полей формы
            reg_f = regform.save(commit=False) # не сохраняем автоматически данные формы
            reg_f.is_staff = False # запрещен вход в административный раздел
            reg_f.is_active = True # активный пользователь
            reg_f.is_superuser = False # не является суперпользователем
            reg_f.date_joined = datetime.now() # дата регистрации
            reg_f.last_login = datetime.now() # дата последней авторизации
            reg_f.save() # сохраняем изменения после добавления данных
            return redirect('home') # переадресация на главную страницу после регистрации
    else:
        regform = UserCreationForm() # создание объекта формы для ввода данных нового пользователя
    return render(
        request,
        'app/registration.html',
        {
            'regform': regform, # передача формы в шаблон веб-страницы

            'year':datetime.now().year,
        }
    )

def blog(request):
    posts = Blog.objects.all().order_by('-posted')

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/blog.html',
        {
            'title':'Блог',
            'posts': posts,
            'year':datetime.now().year,
        }
    )

def blogpost(request, parametr):
    assert isinstance(request, HttpRequest)
    post_1 = Blog.objects.get(id=parametr)
    comments = Comment.objects.filter(post=parametr)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_f = form.save(commit=False)
            comment_f.author = request.user
            comment_f.date = datetime.now()
            comment_f.post = Blog.objects.get(id=parametr)
            comment_f.save()

            return redirect('blogpost', parametr=post_1.id)
    else:
        form = CommentForm()


    return render(
        request,
        'app/blogpost.html',
        {
            'post_1': post_1,

            'comments': comments,
            'form': form,

            'year':datetime.now().year,
        }
    )

def newpost(request):
    assert isinstance(request, HttpRequest)

    if request.method == "POST":
        blogform = BlogForm(request.POST, request.FILES)
        if blogform.is_valid():
            blog_f = blogform.save(commit=False)
            blog_f.posted = datetime.now()
            blog_f.autor = request.user 
            blog_f.save()

            return redirect('blog')
    else:
        blogform = BlogForm() 


    return render(
        request,
        'app/newpost.html',
        {
            
            'blogform': blogform,
            'title': 'Добавить статью блога',

            'year':datetime.now().year,
        }
    )

def videopost(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/videopost.html',
        {
            'title':'Видео',
            'year':datetime.now().year,
        }
    )
