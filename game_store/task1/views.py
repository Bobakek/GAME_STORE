from django.shortcuts import render
from .forms import UserRegister
from .models import Buyer
from .models import Game

# Create your views here.
def index(request):
    return render(request, 'fourth_task/index.html')

# Магазин
def shop(request):
    games = Game.objects.all()
    return render(request, 'fourth_task/shop.html', {'games': games})

# Корзина
def cart(request):
    return render(request, 'fourth_task/cart.html')


users = ['Bob', 'Jane', 'Mikka']
def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif Buyer.objects.filter(name=username).exists():
                info['error'] = 'Пользователь уже существует'
            else:
                Buyer.objects.create(name=username, age=age)
                info['message'] = f'Приветствуем, {username}!'
        else:
            info['error'] = 'Некорректно заполненная форма'
    else:
        form = UserRegister()

    info['form'] = form
    return render(request, 'fourth_task/registration_page.html', info)

# Представление для обработки формы вручную
def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        try:
            age = int(age)
        except ValueError:
            info['error'] = 'Некорректный возраст'
        else:
            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif username in users:
                info['error'] = 'Пользователь уже существует'
            else:
                info['message'] = f'Приветствуем, {username}!'
                users.append(username)

    return render(request, 'fourth_task/registration_page.html', info)