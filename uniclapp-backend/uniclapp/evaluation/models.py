from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Evaluation(models.Model):
    student = models.ForeignKey(
        "accounts.Student", on_delete=models.CASCADE, related_name="post_evaluations")
    rate = models.IntegerField(default=2, validators=[
                               MinValueValidator(0), MaxValueValidator(5)])
    event = models.ForeignKey(
        "event.Event", on_delete=models.CASCADE, related_name="get_evaluations")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.student.student_id} - {self.event.name} - {self.rate}'

    class Meta:
        ordering = ["date"]
