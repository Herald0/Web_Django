from django.db import models


TYPE_SELECT = [
  ('0', 'Мужской'),
  ('1', 'Женский')
]


class User(models.Model):
  name = models.CharField('имя', max_length=50)
  surname = models.CharField('фамилия', max_length=50)
  password = models.CharField('пароль', max_length=20)
  email = models.CharField('email', max_length=30)
  age = models.IntegerField('возраст')
  gender = models.CharField('пол', max_length=8, choices=TYPE_SELECT, default=None)

  def __str__(self):
    return f"{self.name} {self.surname}"

  class Meta:
    verbose_name = 'Пользователь'
    verbose_name_plural = 'Пользователи'


class Post(models.Model):
  post_heading = models.CharField(max_length=200)
  post_text = models.TextField()
  like_count = models.IntegerField(default=0)
  dislike_count = models.IntegerField(default=0)
  
  def __str__(self):
    return f"{self.post_heading}"


class Like(models.Model):
  post = models.ForeignKey(Post, on_delete = models.CASCADE)
  user = models.ForeignKey(User, on_delete = models.CASCADE)
  vote = models.IntegerField(default=0)
  
  def __str__(self):
    return f"{self.post}"
  