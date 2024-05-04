from django.db import models

class Medicine(models.Model):
    m_id = models.IntegerField(primary_key=True, unique=True)
    mname = models.CharField(max_length=30)
    desc = models.CharField(max_length=100)
    price = models.IntegerField()
    stock = models.IntegerField()

    def __str__(self):
        return self.mname


