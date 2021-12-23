from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Evaluation(models.Model):
    student = models.ForeignKey(
        "accounts.Student", on_delete=models.CASCADE, related_name="evaluations")
    content = models.TextField()
    rate = models.IntegerField(default=0, validators=[
                               MinValueValidator(0), MaxValueValidator(5)])
    event = models.ForeignKey(
        "event.Event", on_delete=models.CASCADE, related_name="evaluations")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["date"]
