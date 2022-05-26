from django import forms
from .models import Restaurant,Comment
from .snippets import choices

class RestaurantCreateForm(forms.ModelForm):
    CHOICES= (
    ('Telefonlar','Telefonlar'),
    ('Komputerlər','Komputerlər'),
    ('Planşetlər','Planşetlər'),
    ('Saatlar','Saatlar'),
    ('Digər','Digər'),
    )

    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Marka, Model'}))
    categories = forms.ChoiceField(widget=forms.Select, choices=CHOICES)
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    location = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Şəhər'}))
    price = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Qiymtət'}))
    vat = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Telefon Nömrəsi'}))
    taste = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Yeni?'}))
    persons = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Çatdırılma?'}))
    details = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Restaurant
        fields = ['title','image','categories','location','price','vat','taste','persons','details']
