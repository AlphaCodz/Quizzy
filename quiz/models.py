from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Options(models.Model):
    options = models.CharField(max_length=300, null=True)
    
    def __str__(self):
        return self.options
class Quiz(models.Model):
    STATUS=(
        ("inactive", "inactive"),
        ("active", "active"),
        ("finished", "finished")
    )
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.TextField()
    options = models.ForeignKey(Options, on_delete=models.PROTECT, related_name="quiz_options", null=True)
    right_answer = models.IntegerField()
    status=models.CharField(choices=STATUS, max_length=8)
    start_date = models.DateTimeField(editable=True)
    end_date = models.DateTimeField(editable=True)
    
    def __str__(self):
        return self.question
    