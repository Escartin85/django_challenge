from django.db import models

# Create your models here.
class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.file)

class ClientData(models.Model):
    TYPES_CHOICES = [
        ('TypeCSV', 'Type .csv'),
        ('TypeJSON', 'Type .json'),
    ]

    file = models.ForeignKey(UploadedFile, on_delete=models.CASCADE, default=None, null=True)
    data = models.TextField()
    type = models.CharField(max_length=10, choices=TYPES_CHOICES)

    def __str__(self):
        return f"{self.type} - {self.file}"