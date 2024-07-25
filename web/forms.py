from django import forms

class TicketForm(forms.Form):
    ticket_title = forms.CharField(label = "Título", widget=forms.TextInput(attrs={'class': 'form-control w-auto'}))
    ticket_description = forms.CharField(label = "Descripción", widget=forms.TextInput(attrs={'class': 'form-control w-auto'}))
    user_name = forms.CharField(label = "Nombre Usuario", widget=forms.TextInput(attrs={'class': 'form-control w-auto'}))
    user_phone = forms.CharField(label = "Teléfono Usuario", widget=forms.TextInput(attrs={'class': 'form-control w-auto'}))