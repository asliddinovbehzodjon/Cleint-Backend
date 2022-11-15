from django.db import models

# Create your models here.
class BotUsers(models.Model):
    name = models.CharField(max_length=500,help_text="Enter name",verbose_name="Bot User",blank=True,null=True)
    telegram = models.CharField(max_length=20,verbose_name="Telegram ID",help_text="Enter telegram id",unique=True)
    created = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Bot User "
        verbose_name_plural = "Bot Users "