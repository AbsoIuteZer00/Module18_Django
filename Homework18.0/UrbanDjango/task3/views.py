from django.shortcuts import render


# Create your views here.
def platform(request):
    title = 'Магазин "ПарСек"'
    text = 'Главная страница'
    context = {
        'title': title,
        'text': text
    }
    return render(request, 'third_task/platform.html', context)


def products(request):
    heading = 'Каталог игр'
    game1 = 'Космические рейнджеры'
    game2 = 'Герои меча и магии III'
    game3 = 'X2: The Threat'
    back = 'Вернуться обратно'
    context = {
        'heading': heading,
        'game1': game1,
        'game2': game2,
        'game3': game3,
        'back': back
    }
    return render(request, 'third_task/products.html', context)


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
    return render(request, 'third_task/cart.html', context)
