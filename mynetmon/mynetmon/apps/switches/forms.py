from .models import *
from django.forms import ModelForm, TextInput, Select


class SwitchForm(ModelForm):
    class Meta:
        model = Switch
        fields = ["tit", "category", "status", "label", "model", "ipaddr", "mask", "binfile", "serial", "reliz", "fullmodel", "contact", "ports", "notes", "location", "cfg", "interfaces", "logs", ]
        widgets = {

            "label": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Имя"
            }),
            "model": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Модель"
            }),
            "ipaddr": TextInput(attrs={
                "class": "form-control",
                "placeholder": "IP адрес"
            }),
            "mask": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Маска"
            }),
            "ports": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Кол-во портов"
            }),
            "category": Select(attrs={
                "class": "form-control",
            }),
            "tit": Select(attrs={
                "class": "form-control",
            }),
            "notes": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Комментарий",
            }),


        }

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ["catname", "catlabel"]
        widgets = {

            "catname": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Категория",
                "value": ""
            }),

            "catlabel": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Описание",
                "value": ""
            }),

        }


class TitulForm(ModelForm):
    class Meta:
        model = Titul
        fields = ["titname", "zavod", "titlocation"]
        widgets = {

            "titname": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Титул",
                "value": ""
            }),
            "zavod": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Завод",
                "value": ""
            }),
            "titlocation": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Зона №",
                "value": ""
            }),

            "model": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Модель"
            }),

        }