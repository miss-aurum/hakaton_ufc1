from django.db import models


class Sportman(models.Model):
    CATEGORY = (
                ('w_1','Наилегчайший вес'),
                ('w_2','Легчайший вес'),
                ('w_3','Полулёгкий вес'),
                ('w_4','Легкий вес '),
                ('w_5','Полусредний вес'),
                ('w_6','Средний вес'),
                ('w_7','Полутяжёлый вес'),
                ('w_8','Тяжёлый вес'),
                )
    category = models.CharField(max_length=3,choices=CATEGORY)
    name = models.CharField(max_length=200, verbose_name='Ф.И.О спортсмена')
    trainer = models.ForeignKey('Trainer', on_delete=models.CASCADE)
    reiting = models.IntegerField(verbose_name='Рейтинг')
    image = models.ImageField(verbose_name='Фото', upload_to='Фото спортсмена')
 
    
    

    class Meta:
        verbose_name = 'Спортсмен'
        verbose_name_plural = 'Спортсмены'


    def __str__(self):
        return self.name

class Trainer(models.Model):
    name = models.CharField(max_length=200,verbose_name='Ф.И.О тренера')
    image = models.ImageField(verbose_name='Фотка Информация о тренере ', upload_to='photoTrainer/%Y/%m/%d/')
    
    class Meta:
        verbose_name = 'Тренер'
        verbose_name_plural = 'Тренеры'


    def __str__(self):
        return self.name
    
    

class News(models.Model):
    news = models.TextField(verbose_name='Новости')
    data_publish = models.DateField(verbose_name='Дата публикации')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


    def __str__(self):
        return self.news    

class SocialMedia(models.Model):
    instagram = models.CharField(max_length=500)
    youtube = models.CharField(max_length=500)
    name = models.CharField(max_length=20, verbose_name='')

    class Meta:
        verbose_name = 'Социальная сеть'
        verbose_name_plural = 'Социальные сети'

    def __str__(self) -> str:
        return self.name



    
class Contact(models.Model):
    COOPERATION = (
        ('1','Журналисты'),
        ('2', 'Прямой эфир'),
        ('3','Бизнесмены'),
        ('4','Судьи'),
        
    )
    
    name = models.CharField(max_length=200, verbose_name='И.Ф.О для сотрудничества')
    number = models.CharField(max_length=20, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Адрес электронной почты')
    massage = models.TextField(verbose_name='Сообщения о сотрудничестве')

    class Meta:
        verbose_name = 'Контакт для сотрудничество'
        verbose_name_plural = 'Контакты для сотрудничество'

    def __str__(self):
        return self.name
    
    
    

class Turnir(models.Model):
    title = models.CharField(max_length=200,verbose_name='Заголовок')
    pub_date = models.DateTimeField(verbose_name='Дата публикации')

    class Meta:
        verbose_name = 'Турнир'
        verbose_name_plural = 'Турниры'
    
    def __str__(self):
        return self.title
    
class PeopleTurnir(models.Model):
    sportsmen = models.ForeignKey(Sportman, verbose_name='Боец', on_delete=models.CASCADE)
    anamy = models.CharField(max_length=100, verbose_name="Имя соперника: ")
    knowdown = models.CharField(max_length=10, verbose_name='Нокдауны')
    tot_strokes = models.CharField(max_length=10, verbose_name='Всего ударов')
    accent_hits = models.CharField(max_length=10, verbose_name='Акцент удары')
    tr_ground = models.CharField(max_length=10, verbose_name='Переводы в партер')
    surr_attemps = models.CharField(max_length=10, verbose_name='Попытки сдачи')
    turnir = models.ManyToManyField(Turnir, verbose_name='Номер турнира')


    class Meta:
        verbose_name = 'Участник турнира'
        verbose_name_plural = 'Учасники турнира'

    def __str__(self):
        return self.knowdown







    

    

    
    

    
