from django.db import models

# Таблица справочника курсов
class Course(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название курса")
    color = models.CharField(max_length=7, verbose_name="Цвет (HEX-код)", default="#FFFFFF")

    def str(self):
        return self.title

# Таблица текстов и тем, связанных с курсом
class CourseContent(models.Model):
    course = models.ForeignKey(Course, related_name='contents', on_delete=models.CASCADE, verbose_name="Курс")
    topic = models.CharField(max_length=200, verbose_name="Тема")
    text = models.TextField(verbose_name="Текст")

    def str(self):
        return f"{self.topic} - {self.course.title}"

# Таблица видеокурсов
class VideoCourse(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название видеокурса")
    color = models.CharField(max_length=7, verbose_name="Цвет (HEX-код)", default="#FFFFFF")
    video_url = models.URLField(verbose_name="Ссылка на видео")

    def str(self):
        return self.title