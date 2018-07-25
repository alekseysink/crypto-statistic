from django.db import models

# Create your models here.


class CryptoCurrency(models.Model):

    icon = models.URLField(default='')
    symbol = models.CharField(max_length=64)
    name = models.CharField(max_length=128, unique=True)
    algorithm = models.CharField(max_length=64)
    start_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.symbol}'


class CryptoCurrencyRateData(models.Model):

    crypto_currency = models.ForeignKey(CryptoCurrency, on_delete=models.CASCADE)
    date = models.DateField()
    open_rate = models.DecimalField(max_digits=16, decimal_places=2)
    close_rate = models.DecimalField(max_digits=16, decimal_places=2)
    high_rate = models.DecimalField(max_digits=16, decimal_places=2)
    low_rate = models.DecimalField(max_digits=16, decimal_places=2)
    adj_close = models.DecimalField(max_digits=16, decimal_places=2)
    volume = models.DecimalField(max_digits=16, decimal_places=2)

    def __str__(self):
        return f'{self.crypto_currency.name} -- {self.date}'


class CryptoCurrencyRateDataChanges(models.Model):
    crypto_currency = models.ForeignKey(CryptoCurrency, on_delete=models.CASCADE)
    date = models.DateField()
    changes = models.DecimalField(max_digits=16, decimal_places=8)