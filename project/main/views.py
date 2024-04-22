from django.shortcuts import render

# вывод шаблона html-страницы, какую нужно выводить html-страницу, когда пользователь перейдет на ту или др страницу
def index(request):
    data = {
        'title': 'Профиль'
    }
    return render(request, 'main/index.html', data)

def card(request):
    return render(request, 'main/card.html')

def create_card(request):
    data = {
        'title': 'Новый проект'
    }
    return render(request, 'main/create_card.html', data)