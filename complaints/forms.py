from django import forms
from .models import Complaint

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        # 'student' ko list se hata diya hai
        fields = ['room_number', 'category', 'description']