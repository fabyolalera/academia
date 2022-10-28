from django import forms

class ContactoForm(forms.Form):
    nombre = forms.CharField(
                            widget=forms.TextInput(attrs={'placeholder':'Nombre'})
                            )
    
    email = forms.EmailField(
                            widget=forms.EmailInput(attrs={'placeholder':'Email'})
                            )
    
    telefono = forms.IntegerField(
                            widget=forms.TextInput(attrs={'placeholder':'Telefono'})
                            )
    
    mensaje = forms.CharField(
                            max_length=150,
                            widget=forms.Textarea(attrs={'placeholder':'Mensaje','rows':5, 'cols':71})
                            )

class Form_CrearClase(forms.Form):
    nombre = forms.CharField(max_length=50)
    descripcion = forms.CharField(max_length=500)
    