from django import forms
import _sweetsaratov_.widgets as widgets
from . import models


class ForumMessages(forms.ModelForm):
    class Meta:
        model = models.ForumMessage
        fields = ('content', 'attached_file')

        labels = {
            'content': 'Содержание',
            'sender_id': 'ID отправителя',
            'date': 'Дата создания',
            'attached_file': 'Прикрепить файл'
        }
        widgets = {
            'content': forms.Textarea(attrs={
                    'rows': 16,
                    'cols': 64,
                }),
            'attached_file': forms.widgets.FileInput(),
            'date': widgets.DateInput(
                format='%d/%m/%Y',
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Выберите дату',
                    'type': 'date'
                }
            )
        }
