from django.db import models

class MsgMessage(models.Model):
    content = models.CharField(max_length=256)
    sender_id = models.ForeignKey(
        'users.User', on_delete=models.PROTECT
    )
    creation_date = models.DateField(auto_now=True)


