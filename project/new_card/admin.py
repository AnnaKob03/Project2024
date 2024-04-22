from django.contrib import admin
from .models import technology
from .models import direction
from .models import student
from .models import card
from .models import work_in_the_project
from .models import student_card
from .models import tecnology_card
from .models import technology_project
from .models import tecnology_student

admin.site.register(direction)
admin.site.register(technology)
admin.site.register(student)
admin.site.register(card)
admin.site.register(work_in_the_project)
admin.site.register(student_card)
admin.site.register(tecnology_card)
admin.site.register(technology_project)
admin.site.register(tecnology_student)
