from .forms import CardForm, TechnologyForm, DirectionForm, StudentForm
from .models import technology, direction, student, card  # Capitalized model names
from django.http import JsonResponse
from django.shortcuts import render, redirect

def technology_options(request):
    search = request.GET.get('search', '')
    data = list(technology.objects.filter(name__icontains=search).values('id', 'name'))
    return JsonResponse({'results': [{'id': tech['id'], 'text': tech['name']} for tech in data]})
def new_card_home(request):
    technologies = technology.objects.all()  # More descriptive variable name
    return render(request, 'new_card/new_card_home.html', {'technologies': technologies})


def create(request):
    if request.method == 'POST':
        card_form = CardForm(request.POST)
        technology_form = TechnologyForm(request.POST)
        direction_form = DirectionForm(request.POST)
        student_form = StudentForm(request.POST)

        if all([card_form.is_valid(), technology_form.is_valid(), direction_form.is_valid(), student_form.is_valid()]):
            card_form.save()

            # Сохранение данных в сессию для их отображения после перенаправления
            request.session['student_count'] = card_form.cleaned_data.get('number_of_students')
            request.session['direction_name'] = direction_form.cleaned_data.get('direction_name')
            request.session['group_name'] = student_form.cleaned_data.get('group_number')
            request.session['course_name'] = student_form.cleaned_data.get('course')
            request.session['selected_technologies'] = [tech.id for tech in technology_form.cleaned_data.get('technology_code', [])]

            print(request.session['selected_technologies'])

            return redirect('new_card_home')
        else:
            error = 'Одна или несколько форм неверны'
    else:
        card_form = CardForm()
        technology_form = TechnologyForm()
        direction_form = DirectionForm()
        student_form = StudentForm()
        error = ''

    # Загрузка данных для выбора технологий и направлений
    technology_choices = technology.objects.all()
    direction_choices = direction.objects.values('direction_name').distinct()
    unique_student_groups = student.objects.values('group_number').distinct()
    unique_student_courses = student.objects.values('course').distinct()
    unique_card_number_of_students = card.objects.values('number_of_students').distinct()
    context = {
        'card_form': card_form,
        'technology_form': technology_form,
        'direction_form': direction_form,
        'student_form': student_form,
        'error': error,
        'technology_choices': technology_choices,
        'direction_choices': direction_choices,
        'unique_student_groups': unique_student_groups,
        'unique_student_courses': unique_student_courses,
        'unique_card_number_of_students': unique_card_number_of_students
    }

    return render(request, 'new_card/create.html', context)