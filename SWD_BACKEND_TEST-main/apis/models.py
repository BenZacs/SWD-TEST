from django.db import models


class SchoolStructure(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, default=None, null=True, blank=True)


class Schools(models.Model):
    title = models.CharField(max_length=50, unique=True, null=False, blank=False)

    def __str__(self):
        return self.title


class Classes(models.Model):
    school = models.ForeignKey(Schools, on_delete=models.CASCADE, null=False, blank=False)
    class_order = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return f"Class {self.class_order} of {self.school}"

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['school', 'class_order'], name='unique_school_order')
        ]


class Personnel(models.Model):
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    school_class = models.ForeignKey(Classes, on_delete=models.CASCADE, null=False, blank=False)
    personnel_type = models.IntegerField(default=2, null=False, blank=False,
                                         choices=(("class_teacher", 0),  ("head_of_the_room", 1), ("student", 2)))


class Subjects(models.Model):
    title = models.CharField(max_length=50, unique=True, null=False, blank=False)


class StudentSubjectsScore(models.Model):
    student = models.ForeignKey(Personnel, on_delete=models.CASCADE, null=False, blank=False)
    subjects = models.ForeignKey(Subjects, on_delete=models.CASCADE, null=False, blank=False)
    credit = models.IntegerField(null=False, blank=False)
    score = models.FloatField(null=False, blank=False, default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['student', 'subjects'], name='unique_subject_score')
        ]
