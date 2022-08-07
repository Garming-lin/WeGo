from pyexpat import model
from django.db import models

from django.core.validators import RegexValidator
from django.core.validators import EmailValidator,URLValidator,DecimalValidator,\
    MaxLengthValidator,MinLengthValidator,MaxValueValidator,MinValueValidator

# Create your models here.
class AddUser(models.Model):
    id = models.IntegerField(primary_key=True)#参数需和表字段保持一致
    wxid = models.CharField(max_length=255,error_messages={"null":"输入不能为空！","required":"请输入微信ID！","invalid":"格式错误！"})#参数需和表字段保持一致
    wxname = models.CharField(max_length=50,
    error_messages={
        "invalid":"格式错误！",
        'c1': '优先错信息1','c2': '优先错信息2','c3': '优先错信息3',},
        validators=[
            RegexValidator(regex='root_\d+', message='格式开头错误', code='c1'),
            RegexValidator(regex='[0-9][0-9][0-9][0-9]', message='非数字', code='c2'),
            EmailValidator(message='邮箱格式错误', code='c3'), ])#参数需和表字段保持一致
    identify = models.IntegerField()#参数需和表字段保持一致
    email = models.EmailField(error_messages={"requery":"请输入您的邮箱！","invalid":"格式错误！"})
    #token = models.CharField(max_length=255)#参数需和表字段保持一致
    #tokenTime = models.DateTimeField()#参数需和表字段保持一致
    #lastTime = models.DateTimeField()#参数需和表字段保持一致
    class Meta:
        verbose_name_plural = "去掉s用户类"
        verbose_name = "用户类"
        db_table = "user"#指定表名称，不指定则默认：应用名称_类名，此处是UserInfo_user


class OrderForm(models.Model):
    #id = models.IntegerField(primary_key=True)#参数需和表字段保持一致
    wxid = models.CharField(max_length=255)#参数需和表字段保持一致
    wxname = models.CharField(max_length=50)#参数需和表字段保持一致
    identify = models.IntegerField()#参数需和表字段保持一致
    #token = models.CharField(max_length=255)#参数需和表字段保持一致
    #tokenTime = models.DateTimeField()#参数需和表字段保持一致
    #lastTime = models.DateTimeField()#参数需和表字段保持一致
    class Meta:
        db_table = "u"#指定表名称，不指定则默认：应用名称_类名，此处是UserInfo_user
        