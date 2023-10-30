from django import forms
from support_app.models import OrderQuery

class OrderQueryForm(forms.ModelForm):
    class Meta:
        model = OrderQuery
        fields = ("user_id", "user_query",)
