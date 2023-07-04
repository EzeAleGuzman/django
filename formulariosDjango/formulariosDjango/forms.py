from django import forms


class CommentForm(forms.Form):
    name = forms.CharField(label='escribe tu nombre', max_length=100,help_text="menos de 100 caracteres")
    url = forms.URLField(label='Tu sitio web', required=False)
    comment = forms.CharField()
    
    
class ContactForm(forms.Form):
    name= forms.CharField(
        label='Nombre',
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(
        label='Email',
        max_length=50,
        widget=forms.EmailInput(attrs={'class': 'form-control'}))
    message = forms.CharField(
        label='menssage',
        #sirven para darle estilo a el formulario
        widget=forms.Textarea(attrs={'class': 'form-control'}))

#añadir validacion extra(el nombre tiene que ser open)
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name != 'Open':
            raise forms.ValidationError(' solo Open esta permitido')
        else:
            return name
        
    
