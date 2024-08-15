from django import forms
import _sweetsaratov_.widgets as widgets
from . import models


class ForumMessages(forms.ModelForm):
    class Meta:
        model = models.ForumMessage
        fields = ('content', )

        labels = {
            'content': 'Содержание',
            'sender_id': 'ID отправителя',
            'date': 'Дата создания'
        }
        widgets = {
            "content": forms.Textarea(
                attrs={
                    'rows': 16,
                    'cols': 64,
                }
            ),
            "date": widgets.DateInput(
                format='%d/%m/%Y',
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Выберите дату',
                    'type': 'date'
                }
            )
        }
