from django.db import models
from django.utils import timezone

class Category(models.Model):
    catname = models.CharField('Категория', max_length=50)
    catlabel = models.CharField('Описание', max_length=150, null="True")

    def __str__(self):       #метод вызывается в момент когда мы выводим на экран обьект этого класса
        return self.catname


class Titul(models.Model):
    titname = models.CharField('Титул', max_length=50)
    zavod = models.CharField('Завод', max_length=50)
    titlocation = models.CharField('Зона №', max_length=50)

    def __str__(self):       #метод вызывается в момент когда мы выводим на экран обьект этого класса
        return self.titname

class Backup(models.Model):
    backname = models.CharField('Имя бекапа', max_length=50)
    bfile = models.FileField(null=True, blank=True)
    btime = models.DateTimeField('Дата и время', max_length=50, auto_now=True)

    def __str__(self):       #метод вызывается в момент когда мы выводим на экран обьект этого класса
        return self.backname


class Switch(models.Model):
    #id = models.AutoField(primary_key=True)
    backkey = models.ForeignKey(Backup, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Бекап')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null="True", verbose_name='Категория')
    tit = models.ForeignKey(Titul, on_delete=models.PROTECT, null="True", verbose_name='Титул')
    status = models.CharField('Статус', max_length=50, default="no connection", blank=True)
    label = models.CharField('Имя устройства', max_length=50)
    model = models.CharField('Модель устройства', max_length=50)
    ipaddr = models.GenericIPAddressField('IP Address')
    mask = models.GenericIPAddressField('Маска', default="255.255.252.0")
    binfile = models.CharField('Файл прошивки', max_length=50, default="jg537a-cmw520-r1120.bin", blank=True)
    serial = models.CharField('Серийный номер', max_length=50, default="CN66G1H09L", blank=True)
    reliz = models.CharField('Версия релиза', max_length=50, default="5.20.99 Release 1120", blank=True)
    fullmodel = models.CharField('Полная модель устройства', max_length=50, default="HPE 3600-24-PoE+ (65W) Switch JG937A", blank=True)
    contact = models.CharField('Контакты', max_length=50, default="37-99-53", blank=True)
    ports = models.CharField('Количество портов', max_length=2, default="26")
    notes = models.TextField('Заметки', max_length=1150, default=" ", blank=True)
    location = models.CharField('Локация', max_length=50, default="A18_R342", blank=True)
    cfg = models.TextField('Конфигурация', max_length=4150, default="need connect", blank=True)
    interfaces = models.TextField('Интерфейсы', max_length=35150, default="need connect", blank=True)
    logs = models.TextField('Логи', max_length=20150, default="need connect", blank=True)


    def __str__(self):       #метод вызывается в момент когда мы выводим на экран обьект этого класса
        return self.label

    class Meta:
        verbose_name = 'Устройство'
        verbose_name_plural = 'Устройства'


#class Company(models.Model):
 #   name = models.CharField(max_length=30)


