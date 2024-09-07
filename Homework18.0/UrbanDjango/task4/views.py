from django.shortcuts import render


# Create your views here.
def platform(request):
    title = 'Магазин "ПарСек"'
    heading = 'Главная страница'
    context = {
        'title': title,
        'heading': heading
    }
    return render(request, 'fourth_task/platform.html', context)


def products(request):
    heading = 'Каталог игр'
    games = ['Космические рейнджеры', 'Герои меча и магии III', 'X2: The Threat']
    back = 'Вернуться обратно'
    context = {
        'heading': heading,
        'games': games,
        'back': back
    }
    return render(request, 'fourth_task/products.html', context)


def cart(request):
    title = 'Корзина'
    heading = 'Корзина'
    text = 'Извините, Ваша корзина пуста'
    back = 'Вернуться обратно'
    context = {
        'title': title,
        'heading': heading,
        'text': text,
        'back': back
    }
    return render(request, 'fourth_task/cart.html', context)
