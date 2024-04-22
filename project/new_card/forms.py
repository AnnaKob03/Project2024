
from .models import card, technology, direction, student
from django.forms import ModelForm, TextInput, NumberInput, SelectMultiple
from django import forms
from django.core.validators import MinValueValidator


class CardForm(forms.ModelForm):
    number_of_students = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        validators=[MinValueValidator(2, message="Количество студентов не может быть меньше 2")]
    )

    class Meta:
        model = card
        fields = ['topic_name', 'number_of_students']
        widgets = {
            "topic_name": forms.TextInput(attrs={'class': 'form-control'}),
        }


class TechnologyForm(ModelForm):
    class Meta:
        model = technology
        fields = ['technology_name']

    technology_name = forms.ModelMultipleChoiceField(
        queryset=technology.objects.all(),
        widget=forms.SelectMultiple(attrs={
            'class': 'form-control django-select2'
        }),
        label="Технологии"
    )

class DirectionForm(ModelForm):
    class Meta:
        model = direction
        fields = ['direction_name']

        widgets ={
            "direction_name": TextInput(attrs={
            'class': 'form-control'
            })
        }
        required = {
            'direction_name': False
        }

class StudentForm(ModelForm):
    class Meta:
        model = student
        fields = ['course', 'group_number']

        widgets = {
            "course": NumberInput(attrs={
                'class': 'form-control'
            }),
            "group_number": TextInput(attrs={
                'class': 'form-control'
            })
        }
        required = {
            'course': False,
            'group_number': False
        }

