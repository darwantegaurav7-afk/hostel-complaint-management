from django.db import models
from django.contrib.auth.models import User

class Complaint(models.Model):
    # Status ke options
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    )
    
    # Complaint ki category ke options
    CATEGORY_CHOICES = (
        ('Electrical', 'Electrical'),
        ('Plumbing', 'Plumbing'),
        ('Cleanliness', 'Cleanliness'),
        ('Internet', 'Internet'),
        ('Other', 'Other'),
    )

    student = models.ForeignKey(User, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=10)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.category} Complaint by {self.student.username} - {self.status}"
