from django.shortcuts import render

from app.models import Manager

import hashlib
import os.path
import uuid
from turtle import update

import openpyxl
from django.db.models import Q
from django.shortcuts import render
from django.http import JsonResponse
import json

from django.conf import settings

from app.views import read_excel


# Create your views here.
# 展示用户
def get_managers(request):
    # 获取所有普通用户的信息

    try:
        obj_managers = Manager.objects.all().values()
        # 把结果转化为list
        managers = list(obj_managers)
        return JsonResponse({'code': 1, 'data': managers})
    except Exception as e:
        # 如果出现异常，返回
        return JsonResponse({'code': 0, 'msg': "获取普通用户信息出现异常，具体错误：" + str(e)})


# 添加用户
def add_manager(request):
    data = json.loads(request.body.decode("utf-8"))

    #  添加
    try:
        obj_manager = Manager(username=data['username'], password=data['password'],
                              real_name=data['real_name'], gender=data['gender'], mobile=data['mobile'],
                              email=data['email'], address=data['address'], image=data['image'])
        #  执行添加
        obj_manager.save()
        try:
            obj_managers = Manager.objects.all().values()
            # 把结果转化为list
            managers = list(obj_managers)
            return JsonResponse({'code': 1, 'data': managers})
        except Exception as e:
            # 如果出现异常，返回
            return JsonResponse({'code': 0, 'msg': "添加管理员信息出现异常，具体错误：" + str(e)})
    except Exception as e:
        return JsonResponse({'code': 0, 'msg': "添加到数据库出现异常，具体：" + str(e)})


def login_manager(request):
    data = json.loads(request.body.decode('utf-8'))

    try:
        obj_user = Manager.objects.get(username=data["username"])
        if obj_user.password == data['password']:
            session_id = data["username"]
            return JsonResponse({'code': 1, 'sessionId': session_id})
        else:
            return JsonResponse({'code': 0, 'msg': '密码错误'})

    except Exception as e:
        return JsonResponse({'code': 0, 'msg': "登录出现异常，具体：" + str(e)})


def update_manager(request):
    data = json.loads(request.body.decode("utf-8"))

    #  添加
    try:
        #  查找到要修改的用户
        obj_manager = Manager.objects.get(username=data['username'])
        #  执行修改
        obj_manager.password = data['password']
        obj_manager.real_name = data['real_name']
        obj_manager.gender = data['gender']
        obj_manager.mobile = data['mobile']
        obj_manager.email = data['email']
        obj_manager.address = data['address']
        obj_manager.image = data['image']

        try:
            obj_manager.save()
            obj_managers = Manager.objects.all().values()
            # 把结果转化为list
            managers = list(obj_managers)
            return JsonResponse({'code': 1, 'data': managers})
        except Exception as e:
            # 如果出现异常，返回
            return JsonResponse({'code': 0, 'msg': "修改用户信息出现异常，具体错误：" + str(e)})
    except Exception as e:
        return JsonResponse({'code': 0, 'msg': "修改到数据库出现异常，具体：" + str(e)})


def query_managers(request):
    data = json.loads(request.body.decode('utf-8'))

    try:
        obj_managers = Manager.objects.filter(
            Q(real_name__contains=data['inputstr']) | Q(gender__contains=data['inputstr']) |
            Q(mobile__contains=data['inputstr']) | Q(email__contains=data['inputstr']) |
            Q(address__contains=data['inputstr'])).values()
        managers = list(obj_managers)
        return JsonResponse({'code': 1, 'data': managers})
    except Exception as e:
        # 异常
        return JsonResponse({'code': 1, 'msg': "查询管理员信息失败：" + str(e)})


def delete_manager(request):
    data = json.loads(request.body.decode("utf-8"))

    #  添加
    try:
        #  查找到要删除的学生
        obj_manager = Manager.objects.get(username=data['username'])

        obj_manager.delete()
        try:
            obj_managers = Manager.objects.all().values()
            # 把结果转化为list
            managers = list(obj_managers)
            return JsonResponse({'code': 1, 'data': managers})
        except Exception as e:
            # 如果出现异常，返回
            return JsonResponse({'code': 0, 'msg': "删除管理员信息出现异常，具体错误：" + str(e)})
    except Exception as e:
        return JsonResponse({'code': 0, 'msg': "删除到数据库出现异常，具体：" + str(e)})


def delete_managers(request):
    data = json.loads(request.body.decode('utf-8'))

    try:
        for one_manager in data['user']:
            obj_manager = Manager.objects.get(username=one_manager['username'])
            obj_manager.delete()
        # 获取最后结果
        try:
            obj_managers = Manager.objects.all().values()
            # 把结果转化为listtha
            managers = list(obj_managers)
            return JsonResponse({'code': 1, 'data': managers})
        except Exception as e:
            # 如果出现异常，返回
            return JsonResponse({'code': 0, 'msg': "批量删除管理员信息出现异常，具体错误：" + str(e)})
    except Exception as e:
        return JsonResponse({'code': 0, 'msg': "批量删除到数据库出现异常，具体：" + str(e)})


def get_random_str():
    uuid_val = uuid.uuid4()
    uuid_str = str(uuid_val).encode('utf-8')
    md5 = hashlib.md5()
    md5.update(uuid_str)
    return md5.hexdigest()


def import_managers_excel(request):
    rev_file = request.FILES.get('excel')
    #   判断是否有文件
    if not rev_file:
        return JsonResponse({'code': 0, 'msg': '文件不存在！'})
    #   获得一个唯一的名字
    excel_name = get_random_str()
    #   准备写入的URL
    file_path = os.path.join(settings.MEDIA_ROOT, excel_name + os.path.splitext(str(rev_file))[1])
    # print("fpath:" + file_path)
    try:
        f = open(file_path, 'wb')
        for i in rev_file.chunks():
            f.write(i)
        f.close()
    except Exception as e:
        JsonResponse({'code': 0, 'msg': str(e)})

    ex_users = read_excel(file_path)
    # print(ex_users)
    success = 0
    error = 0
    error_snos = []
    for one_manager in ex_users:
        try:
            obj_manager = Manager.objects.create(username=one_manager['username'], password=one_manager['password'],
                                                 real_name=one_manager['real_name'],
                                                 gender=one_manager['gender'], mobile=one_manager['mobile'],
                                                 email=one_manager['email'], address=one_manager['address'])
            success += 1
        except:
            error += 1
            error_snos.append(one_manager['username'])
    obj_managers = Manager.objects.all().values()
    managers = list(obj_managers)
    return JsonResponse({'code': 1, 'success': success, 'error': error, 'errors': error_snos, 'data': managers})


def export_managers_excel(request):
    obj_managers = Manager.objects.all().values()
    managers = list(obj_managers)
    # 准备写入的路径
    excel_name = get_random_str() + ".xlsx"
    path = os.path.join(settings.MEDIA_ROOT, excel_name)
    # 写入
    write_to_excel(managers, path)
    return JsonResponse({'code': 1, 'name': excel_name})


def write_to_excel(data: list, path: str):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = 'manager'
    keys = data[0].keys()
    for index, item in enumerate(data):
        for k, v in enumerate(keys):
            sheet.cell(row=index + 1, column=k + 1, value=str(item[v]))

    workbook.save(path)


def upload(request):
    #   接受上传的文件
    rev_file = request.FILES.get('avatar')
    #   判断是否有文件
    if not rev_file:
        return JsonResponse({'code': 0, 'msg': '图片不存在！'})
    #   获得一个唯一的名字
    new_name = get_random_str()
    #   准备写入的URL
    file_path = os.path.join(settings.MEDIA_ROOT, new_name + os.path.splitext(str(rev_file))[1])
    # print("fpath:" + file_path)
    try:
        f = open(file_path, 'wb')
        for i in rev_file.chunks():
            f.write(i)
        f.close()
        return JsonResponse({'code': 1, 'name': new_name + os.path.splitext(str(rev_file))[1]})
    except Exception as e:
        JsonResponse({'code': 0, 'msg': str(e)})
