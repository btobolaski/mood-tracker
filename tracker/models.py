from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone

# Create your models here.
class Record(models.Model):
    SKIPPED = 0
    LITTLE = 1
    MODERATE = 2
    GREAT = 3
    EXCESS = 4
    QUALITATIVE_QUANTIFIERS=[
        (SKIPPED, "None"),
        (LITTLE, "A little"),
        (MODERATE, "A moderate amount"),
        (GREAT, "A large amount"),
        (EXCESS, "An excessive amount"),
    ]

    hours_validators = [MaxValueValidator(24), MinValueValidator(0)]
    qualitative_quantifier_validators = [MaxValueValidator(4), MinValueValidator(0)]

    date = models.DateField(default=timezone.now)
    location = models.TextField(help_text="Where did you stay for the day.")
    sex = models.BooleanField()
    sleep_hours = models.DecimalField("hours of sleep", max_digits=3, decimal_places=1, validators=hours_validators)
    work_hours = models.DecimalField("hours of work", max_digits=3, decimal_places=1, default=0, validators=hours_validators)
    parenting_hours = models.DecimalField("hours of parenting", max_digits=3, decimal_places=1, default=0, validators=hours_validators)
    personal_hours = models.DecimalField("hours of personal time", max_digits=3, decimal_places=1, default=0, validators=hours_validators)
    social_hours = models.DecimalField("hours of social time", max_digits=3, decimal_places=1, default=0, validators=hours_validators)
    exercise_minutes = models.PositiveSmallIntegerField(default=0)
    calories_burned = models.PositiveSmallIntegerField(default=0)
    sweets_eaten = models.PositiveSmallIntegerField(choices=QUALITATIVE_QUANTIFIERS, validators=qualitative_quantifier_validators)
    stress_level = models.PositiveSmallIntegerField(choices=QUALITATIVE_QUANTIFIERS, validators=qualitative_quantifier_validators)
    motivation_level = models.PositiveSmallIntegerField(choices=QUALITATIVE_QUANTIFIERS, validators=qualitative_quantifier_validators)
    energy_level = models.PositiveSmallIntegerField(choices=QUALITATIVE_QUANTIFIERS, validators=qualitative_quantifier_validators)
    physical_health_level = models.PositiveSmallIntegerField(choices=QUALITATIVE_QUANTIFIERS, validators=qualitative_quantifier_validators)
    illness_level = models.PositiveSmallIntegerField(choices=QUALITATIVE_QUANTIFIERS, validators=qualitative_quantifier_validators)
