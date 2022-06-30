from django.contrib.auth.forms import UserCreationForm

from . models import Empresa

class EmpresaForm(UserCreationForm):
    
    class Meta:
        model = Empresa
        fields = (
            'nome',
            'cnpj',
            'contato',
            'cep',
            'username',
            'email',
            'password1',
            'password2'
        )