from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone

# Create your models here.


class Medication(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["owner", "name"], name="medication_owner_name_unique"
            )
        ]

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.TextField("Medication Name")

    def __str__(self):
        return self.name


class MedicationDosage(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["owner", "medication", "dosage"],
                name="medication_dosage_owner_medication_dosage_unique",
            )
        ]

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE, null=False)
    dosage = models.TextField("Dosage")

    def __str__(self):
        return f"{self.medication.name} - {self.dosage}"


class Tag(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["owner", "name"], name="tag_owner_name_unique"
            ),
        ]

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.TextField("Tag Name")

    def __str__(self):
        return self.name


class Record(models.Model):
    SKIPPED = 0
    LITTLE = 1
    MODERATE = 2
    GREAT = 3
    EXCESS = 4
    QUALITATIVE_QUANTIFIERS = [
        (SKIPPED, "None"),
        (LITTLE, "A little"),
        (MODERATE, "A moderate amount"),
        (GREAT, "A large amount"),
        (EXCESS, "An excessive amount"),
    ]

    EATING_QUANTIFIERS = [
        (SKIPPED, "None"),
        (LITTLE, "Light"),
        (MODERATE, "Normal"),
        (GREAT, "Excessive"),
    ]

    VERY_DEPRESSED = 0
    DEPRESSED = 1
    MILDLY_DEPRESSED = 2
    LOW = 3
    GOOD = 4
    ELEVATED = 5
    MILDLY_MANIC = 6
    MANIC = 7
    VERY_MANIC = 8
    OVERALL_MOOD_OPTIONS = [
        (VERY_DEPRESSED, "Very Depressed"),
        (DEPRESSED, "Depressed"),
        (MILDLY_DEPRESSED, "Mildly Depressed"),
        (LOW, "Low"),
        (GOOD, "Good"),
        (ELEVATED, "Elevated"),
        (MILDLY_MANIC, "Mildly Manic"),
        (MANIC, "Manic"),
        (VERY_MANIC, "Very Manic"),
    ]

    hours_validators = [MaxValueValidator(24), MinValueValidator(0)]
    qualitative_quantifier_validators = [MaxValueValidator(4), MinValueValidator(0)]
    overall_mood_validators = [MaxValueValidator(8), MinValueValidator(0)]
    eating_validators = [MaxValueValidator(GREAT), MinValueValidator(SKIPPED)]

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1
    )
    date = models.DateField(default=timezone.now)
    location = models.TextField(help_text="Where did you stay for the day.")
    sex = models.BooleanField()
    sleep_hours = models.DecimalField(
        "hours of sleep", max_digits=3, decimal_places=1, validators=hours_validators
    )
    work_hours = models.DecimalField(
        "hours of work",
        max_digits=3,
        decimal_places=1,
        default=0,
        validators=hours_validators,
    )
    parenting_hours = models.DecimalField(
        "hours of parenting",
        max_digits=3,
        decimal_places=1,
        default=0,
        validators=hours_validators,
    )
    overnight_parenting = models.BooleanField("parenting overnight", default=True)
    personal_hours = models.DecimalField(
        "hours of personal time",
        max_digits=3,
        decimal_places=1,
        default=0,
        validators=hours_validators,
    )
    social_hours = models.DecimalField(
        "hours of social time",
        max_digits=3,
        decimal_places=1,
        default=0,
        validators=hours_validators,
    )
    exercise_minutes = models.PositiveSmallIntegerField(default=0)
    calories_burned = models.PositiveSmallIntegerField(default=0)
    eating = models.PositiveSmallIntegerField(
        choices=EATING_QUANTIFIERS, validators=eating_validators, default=MODERATE
    )
    sweets_eaten = models.PositiveSmallIntegerField(
        choices=QUALITATIVE_QUANTIFIERS, validators=qualitative_quantifier_validators
    )
    stress_level = models.PositiveSmallIntegerField(
        choices=QUALITATIVE_QUANTIFIERS, validators=qualitative_quantifier_validators
    )
    stress_score = models.FloatField(
        "stress score", blank=True, null=True, default=None
    )
    sex_drive = models.PositiveSmallIntegerField(
        choices=QUALITATIVE_QUANTIFIERS,
        validators=qualitative_quantifier_validators,
        default=SKIPPED,
    )
    motivation_level = models.PositiveSmallIntegerField(
        choices=QUALITATIVE_QUANTIFIERS, validators=qualitative_quantifier_validators
    )
    concentration_level = models.PositiveSmallIntegerField(
        choices=QUALITATIVE_QUANTIFIERS, validators=qualitative_quantifier_validators
    )
    energy_level = models.PositiveSmallIntegerField(
        choices=QUALITATIVE_QUANTIFIERS, validators=qualitative_quantifier_validators
    )
    physical_health_level = models.PositiveSmallIntegerField(
        choices=QUALITATIVE_QUANTIFIERS, validators=qualitative_quantifier_validators
    )
    illness_level = models.PositiveSmallIntegerField(
        choices=QUALITATIVE_QUANTIFIERS, validators=qualitative_quantifier_validators
    )
    irritability = models.PositiveSmallIntegerField(
        choices=QUALITATIVE_QUANTIFIERS,
        validators=qualitative_quantifier_validators,
        default=SKIPPED,
    )
    overall_mood = models.PositiveSmallIntegerField(
        choices=OVERALL_MOOD_OPTIONS,
        validators=overall_mood_validators,
    )

    tags = models.ManyToManyField(Tag)
    medications_taken = models.ManyToManyField(MedicationDosage)

    class Meta:
        ordering = ["-date"]
        constraints = [
            models.UniqueConstraint(
                fields=["owner", "date"], name="record_owner_date_unique"
            ),
        ]
