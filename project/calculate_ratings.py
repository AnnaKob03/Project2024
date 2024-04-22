import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from new_card.models import technology, technology_project, work_in_the_project, tecnology_student


def calculate_student_ratings():
    for tech in technology.objects.all():
        project_ids = technology_project.objects.filter(fk_technology=tech).values_list('fk_project', flat=True)
        projects = work_in_the_project.objects.filter(project_id__in=project_ids).select_related('fk_student')

        student_data = {}
        for project in projects:
            student_id = project.fk_student.student_id
            if student_id not in student_data:
                student_data[student_id] = {
                    'score_sum': 0,
                    'mark_sum': 0,
                    'count': 0
                }
            student_data[student_id]['score_sum'] += project.score
            student_data[student_id]['mark_sum'] += project.mark
            student_data[student_id]['count'] += 1

        for student_id, data in student_data.items():
            average_score = data['score_sum'] / data['count']
            average_mark = data['mark_sum'] / data['count']
            project_count = data['count']
            rating = (average_score * average_mark * project_count) / 100

            tecnology_student.objects.update_or_create(
                fk_student_id=student_id,
                fk_technology=tech,
                defaults={'rating': rating}
            )


if __name__ == "__main__":
    calculate_student_ratings()
