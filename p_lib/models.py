from django.db import models

# Create your models here.
class Author(models.Model):
    last_name = models.CharField("Фамилия", max_length=255)
    first_name = models.CharField("Имя", max_length=255)
    additional_name = models.CharField("Отчество", max_length=255, blank=True)
    birth_year = models.SmallIntegerField("Год рождения")
    country = models.CharField("Страна", max_length=255)

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

    def __str__(self):
        if self.additional_name:
            return str(self.last_name) + " " + str(self.first_name) + " " + str(self.additional_name)
        else:
            return str(self.last_name) + " " + str(self.first_name)


class Publisher(models.Model):
    pub_name = models.CharField("Название издательства", max_length=255)
    pub_city = models.CharField("Город издательства", max_length=255)
    pub_site = models.URLField("Сайт издательства", blank=True)
    foundation_year = models.SmallIntegerField("Год основания")

    class Meta:
        verbose_name = "Издательство"
        verbose_name_plural = "Издательства"

    def __str__(self):
        return self.pub_name


class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    title = models.TextField("Название книги")
    description = models.TextField("Описание книги")
    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.CASCADE,
        related_name="book_publisher",
        verbose_name= ("Издательство"))
    year_release = models.SmallIntegerField("Год издания")
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="book_author",
        verbose_name= ("Автор"))
    copy_count = models.PositiveSmallIntegerField("Кол-во копий", default=1)
    price = models.DecimalField("Цена", decimal_places=2, max_digits=8, default=0)
    photo = models.ImageField(upload_to='books_photo', blank=True)
    small_photo = models.ImageField(upload_to='books_photo/small', blank=True)

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def __str__(self):
        return self.title

