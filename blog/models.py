from django.db import models

# Create your models here.
from django.db import models

class Post(models.Model):
    # 게시물 제목을 저장
    # CharField : 글자수의 제한이 있는 문자열
    # max_length = 300: 300 글자까지 저장
    title = models.CharField(max_length= 300)

    # 게시글의 작성자를 저장
    writer = models.CharField(max_length= 30)

    # 게시글의 내용을 저장
    content = models.TextField()

    # 작성일을 저장
    created_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return '[id='+str(self.id)+',title='+str(self.title)+',writer='+str(self.writer)+\
               ",content="+str(self.content)+',created_at='+str(self.created_at)+"]"
