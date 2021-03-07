
from django import forms
from django.forms import TextInput, NumberInput,SelectMultiple,Select

from hospital.models import BloodStock


class BloodStockForm(forms.ModelForm):

    class Meta:
        model = BloodStock
        fields = '__all__'

        widgets = {
            'hospital':Select(attrs={
                'class':'form-control',
                'required':'true',
                'min':'0',
                'placeholder':'Enter Hospital Username',
            }),
            'w_a_positive':NumberInput(attrs={
                'class':'form-control',
                'required':'true',
                'min':'0',
            }),
            'w_a_negative': NumberInput(attrs={
                'class': 'form-control',
                'required':'true',
                'min':'0',
            }),
            'w_b_positive': NumberInput(attrs={
                'class': 'form-control',
                'required':'true',
                'min':'0',
            }),
            'w_b_negative': NumberInput(attrs={
                'class': 'form-control',
                'required':'true',
                'min':'0',
            }),
            'w_ab_positive': NumberInput(attrs={
                'class': 'form-control',
                'required':'true',
                'min':'0',
            }),
            'w_ab_negative': NumberInput(attrs={
                'class': 'form-control',
                'required':'true',
                'min':'0',
            }),
            'w_o_positive': NumberInput(attrs={
                'class': 'form-control',
                'required':'true',
                'min':'0',
            }),
            'w_o_negative': NumberInput(attrs={
                'class': 'form-control',
                'required':'true',
                'min':'0',
            }),

            'b_a_positive': NumberInput(attrs={
                'class': 'form-control',
                'required':'true',
                'min':'0',
            }),
            'b_a_negative': NumberInput(attrs={
                'class': 'form-control',
                'required':'true',
                'min':'0',
            }),
            'b_b_positive': NumberInput(attrs={
                'class': 'form-control',
                'required':'true',
                'min':'0',
            }),
            'b_b_negative': NumberInput(attrs={
                'class': 'form-control',
                'required':'true',
                'min':'0',
            }),
            'b_ab_positive': NumberInput(attrs={
                'class': 'form-control',
                'required':'true',
                'min':'0',
            }),
            'b_ab_negative': NumberInput(attrs={
                'class': 'form-control',
                'required':'true',
                'min':'0',
            }),
            'b_o_positive': NumberInput(attrs={
                'class': 'form-control',
                'required':'true',
                'min':'0',
            }),
            'b_o_negative': NumberInput(attrs={
                'class': 'form-control',
                'required':'true',
                'min':'0',
            }),

            'RDP': NumberInput(attrs={
                'class': 'form-control',
                'required':'true',
                'min':'0',
            }),
            'SDP': NumberInput(attrs={
                'class': 'form-control',
                'required':'true',
                'min':'0',
            }),
            'FFP': NumberInput(attrs={
                'class': 'form-control',
                'required':'true',
                'min':'0',
            }),
            'CRYO': NumberInput(attrs={
                'class': 'form-control',
                'required':'true',
                'min':'0',
            }),

        }