from django import forms


class RechazarPropuestaForm(forms.Form):
    opciones = (
        ("Opcion 1", "Opcion 1"),
        ("Opcion 2", "Opcion 2"),
        ("Opcion 3", "Opcion 3"),
        ("Opcion 4", "Opcion 4"),
    )

    descripcion = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 5, }), required=False)
    motivo_rechazo = forms.ChoiceField(
        choices=opciones, label="Seleccionar el motivo del rechazo")
