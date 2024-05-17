from django import forms

class BookingForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=200)
    last_name = forms.CharField(label='Last Name', max_length=200)
    number_of_guests = forms.IntegerField(label='Number of Guests')
    comments = forms.CharField(label='Comments', widget=forms.Textarea(attrs={'rows': 4}), required=False)
