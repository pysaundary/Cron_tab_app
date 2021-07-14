from django.db import models
from multiselectfield import MultiSelectField
# Create your models here.
sex_choice=[
('M','Male'),
('F','Female'),
]
subject_choices=(
            (1, 'Java'),
           (2, 'Python'),
           (3, 'Ruby'),
           (4, 'C++'),
           (5, 'DotNet'),
           )
class Students(models.Model):



    name=models.CharField(max_length=20)
    sex=models.CharField(choices=sex_choice,max_length=6)
    profile_pic=models.ImageField(upload_to="profiles_pics", height_field=None, width_field=None, max_length=None)
    is_active=models.BooleanField(default=False)
    subject=MultiSelectField(choices=subject_choices,
                                 max_choices=3,
                                 max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='student'
        verbose_name_plural='students'
