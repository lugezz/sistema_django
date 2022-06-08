from django.forms import *
from erp.models import Category


class CategoryForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Category
        fields = '__all__'
        # exclude = ... si necesitara excluir campos

        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': "Ingrese el nombre de categoría"
                }
            ),

            'desc': Textarea(
                attrs={
                    'placeholder': "Ingrese la descipción del nombre de categoría",
                    'rows': 3,
                    'cols': 3
                }
            )
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
