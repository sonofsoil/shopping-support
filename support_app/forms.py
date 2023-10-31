from django import forms
from support_app.models import OrderQuery, OrderDetails

class OrderQueryForm(forms.ModelForm):
    class Meta:
        model = OrderQuery
        fields = ("user_id", "user_query",)

class OrderDetailsForm(forms.ModelForm):
    class Meta:
        model = OrderDetails
        fields = ("user_id",)
