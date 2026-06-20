from django.db import models

class Conscript(models.Model):
    GENDER_CHOICES = [
        ('M', 'Мужской'),
        ('F', 'Женский'),
    ]
    STATUS_CHOICES = [
        ('registered', 'На учёте'),
        ('exempt', 'Освобождён'),
        ('serving', 'В армии'),
        ('reserve', 'В запасе'),
    ]

    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    middle_name = models.CharField(max_length=50, blank=True, verbose_name="Отчество")
    birth_date = models.DateField(verbose_name="Дата рождения")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Пол")
    address = models.TextField(verbose_name="Адрес проживания")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='registered', verbose_name="Статус призыва")

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"

    class Meta:
        verbose_name = "Призывник"
        verbose_name_plural = "Призывники"


class MedicalInfo(models.Model):
    conscript = models.OneToOneField(Conscript, on_delete=models.CASCADE, related_name='medical', verbose_name="Призывник")
    fitness_category = models.CharField(max_length=10, verbose_name="Категория годности")
    diagnosis = models.TextField(blank=True, verbose_name="Диагноз")
    notes = models.TextField(blank=True, verbose_name="Примечания")

    def __str__(self):
        return f"Мед. данные: {self.conscript}"

    class Meta:
        verbose_name = "Медицинские данные"
        verbose_name_plural = "Медицинские данные"


class DraftCampaign(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название кампании")
    start_date = models.DateField(verbose_name="Дата начала")
    end_date = models.DateField(verbose_name="Дата окончания")
    conscripts = models.ManyToManyField(Conscript, related_name='campaigns', verbose_name="Призывники")
    notes = models.TextField(blank=True, verbose_name="Примечания")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Призывная кампания"
        verbose_name_plural = "Призывные кампании"