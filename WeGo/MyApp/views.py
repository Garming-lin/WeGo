from pydoc import classname
from tkinter import E
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader,Template,Context

# Create your views here.
from MyApp.models import AddUser


def test_views(request):
    user = AddUser(id=1,wxid='11',wxname='1234',identify=1,email='uu')
    msg = ''
    try:
        msg = user.clean_fields()
    except Exception as e:
        msg = e
    return HttpResponse(msg)

def test(request):
    '''
    AddUser.objects.create(wxid='1002',wxname='ljm',identify=1)#插入新数据
    user = AddUser(wxid='1003',wxname='aaa',identify=1)
    user.wxname = "admin"#修改字段
    user.save()#保存并插入新数据
    '''
    
    def fun(s):
        return s

    class cla():
        def __init__(self):
            self.classname = "类属性"
        def get(self):
            return "测试类函数（classname：" + self.classname + "）"
        def gr(s):
            return s

    dic = {
	"res":"响应内容",
	"result":["响应内容",123,{"key":"value"}],
	"name":{"key":"测试响应","num":123},
	"num":456,
	"person":{"name":"Jone","age":26,"sex":"男"},
	"t1":{"t2":{"t5":"t6"},"t3":"4"},
    "cla":cla(),
    "clafun":cla.gr("测试类函数"),
    "fun":fun("测试函数"),
    }
    return render(request,"t.html",dic)
