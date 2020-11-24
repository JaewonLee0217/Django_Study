from django.conf import settings
from django.db import models
from django.utils import timezone
# Django의 이러한 파일에서 코드들을 불러와라.

# class Post(models.Model): # Post라는 객체를 모델 정의.
#     author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     title = models.CharField(max_length=200)
#     text = models.TextField()
#     created_date = models.DateTimeField(
#             default=timezone.now)
#     published_date = models.DateTimeField(
#             blank=True, null=True)
#
#     def publish(self):
#         self.published_date = timezone.now()
#         self.save()
#
#     def __str__(self):
#         return self.title
#     #__STR__함수 호출하면 Post클래스로 찍은 객체의 이름을 알수 있음.