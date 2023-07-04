from django.forms import ModelForm
from .models import Empleados


class EmpleadosForm(ModelForm):
    class Meta:
        model = Empleados
        #'__all__' tambien incluye a todos
        fields = ['name','last_name','email']
        # extra_fields = ['salario'] agergar extra
        # exclude = ('email',) para excluir un dato
        
    