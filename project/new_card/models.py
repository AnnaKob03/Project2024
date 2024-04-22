from django.db import models


class card(models.Model):
    card_code = models.AutoField(primary_key=True)
    topic_name = models.TextField()
    number_of_students = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'card'


class direction(models.Model):
    direction_id = models.AutoField(primary_key=True)
    direction_name = models.TextField()

    class Meta:
        managed = True
        db_table = 'direction'


class student(models.Model):
    student_id = models.AutoField(primary_key=True)
    student_name = models.TextField()
    course = models.IntegerField()
    group_number = models.TextField()
    fk_direction = models.ForeignKey(direction, models.DO_NOTHING, db_column='fk_direction', blank=True, null=True)
    email = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'student'


class student_card(models.Model):
    student_card_id = models.AutoField(primary_key=True)
    fk_student = models.ForeignKey(student, models.DO_NOTHING, db_column='fk_student', blank=True, null=True)
    fk_card = models.ForeignKey(card, models.DO_NOTHING, db_column='fk_card', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'student_card'


class technology(models.Model):
    technology_code = models.AutoField(primary_key=True)
    technology_name = models.TextField()

    class Meta:
        managed = True
        db_table = 'technology'


class technology_project(models.Model):
    technology_project_id = models.AutoField(primary_key=True)
    fk_technology = models.ForeignKey(technology, models.DO_NOTHING, db_column='fk_technology', blank=True, null=True)
    fk_project = models.ForeignKey('work_in_the_project', models.DO_NOTHING, db_column='fk_project', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'technology_project'



class tecnology_card(models.Model):
    tecnology_card_id = models.AutoField(primary_key=True)
    fk_technology = models.ForeignKey(technology, models.DO_NOTHING, db_column='fk_technology', blank=True, null=True)
    fk_card = models.ForeignKey(card, models.DO_NOTHING, db_column='fk_card', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tecnology_card'


class tecnology_student(models.Model):
    tecnology_student_id = models.AutoField(primary_key=True)
    rating = models.FloatField()
    fk_technology = models.ForeignKey(technology, models.DO_NOTHING, db_column='fk_technology', blank=True, null=True)
    fk_student = models.ForeignKey(student, models.DO_NOTHING, db_column='fk_student', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tecnology_student'


class work_in_the_project(models.Model):
    project_id = models.AutoField(primary_key=True)
    mark = models.IntegerField()
    score = models.FloatField()
    fk_student = models.ForeignKey(student, models.DO_NOTHING, db_column='fk_student', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'work_in_the_project'
