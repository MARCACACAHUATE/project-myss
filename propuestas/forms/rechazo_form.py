from django import forms
from usuarios.models import Motivo


class RechazarPropuestaForm(forms.Form):
    motivos_rechazo = Motivo.objects.all()

    opciones = [(motivo.Titulo, motivo.Descripcion)
                for motivo in motivos_rechazo]

    descripcion = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 5, }), required=False)
    motivo_rechazo = forms.ChoiceField(
        choices=opciones, label="Seleccionar el motivo del rechazo")

    def convert_into_tuple(self, lista):
        return tuple((lista.Motivo, lista.Motivo) for motivo in lista)
