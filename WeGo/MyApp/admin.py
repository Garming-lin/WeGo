from django.contrib import admin
from django import forms

# Register your models here.
from MyApp.models import AddUser,OrderForm
from django.core.validators import RegexValidator

class AddUserForm(forms.ModelForm):
    age = forms.IntegerField(initial=1,error_messages={"required":"请输入您的年龄！","invalid":"格式错误！"})
    class Meta:
        model = AddUser
        fields = "__all__"
        exclude = ['title']
        labels = { 'name':'测试', }
        help_texts = {'name':'模型类提示内容',}
        error_messages={
            'a1':"输入内容不能为空！",
            'a2':"输入内容错误，请重新更正！",
            }
        validators=[
            RegexValidator(regex='', message='内容不能为空', code='a1'),
            RegexValidator(regex='root_112233\d+', message='请输入有效值！', code='c2')]

class AddUserAdmin(admin.ModelAdmin):
    form = AddUserForm

#admin.site.register(AddUser,AddUserAdmin)#注册admin后台管理修改模型类



admin.site.register([AddUser,OrderForm])#注册admin后台管理修改模型类
