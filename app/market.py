import hashlib
import os
import uuid

import openpyxl
from django.shortcuts import render

from app.models import Market

from django.db.models import Q
from django.http import JsonResponse
import json

from django.conf import settings
def get_Markets(request):
    # 获取所有普通商品的信息

    try:
        obj_Markets = Market.objects.all().values()
        # 把结果转化为list
        Markets = list(obj_Markets)
        return JsonResponse({'code': 1, 'data': Markets})
    except Exception as e:
        # 如果出现异常，返回
        return JsonResponse({'code': 0, 'msg': "获取商品信息出现异常，具体错误：" + str(e)})


# 添加用户
def add_Market(request):
    data = json.loads(request.body.decode("utf-8"))
    # print(data['imageUrl'])

    #  图片上传
    #  添加
    try:
        # print("wohao")
        obj_Market = Market(name=data['name'], price=data['price'],
                        owner=data['owner'], nikcname=data['nickname'],
                            catagory=data['catagory'], mobile=data['mobile'],
                        status=data['status'], image=data['image'],imageUrl=data['imageUrl'])
        # print("nihao")

        cnt = Market.objects.filter(name=data['name']).count()
        if cnt > 0:
            return JsonResponse({'code': 2, 'msg': "商品已存在！"})

        #  执行添加
        # print(obj_Market.imageUrl)
        obj_Market.save()
        try:
            obj_Markets = Market.objects.all().values()
            # 把结果转化为list
            Markets = list(obj_Markets)
            return JsonResponse({'code': 1, 'data': Markets})
        except Exception as e:
            # 如果出现异常，返回
            return JsonResponse({'code': 0, 'msg': "添加商品信息出现异常，具体错误：" + str(e)})
    except Exception as e:
        return JsonResponse({'code': 0, 'msg': "添加到数据库出现异常，具体：" + str(e)})


# 修改用户
def update_Market(request):
    data = json.loads(request.body.decode("utf-8"))

    #  添加
    try:
        #  查找到要修改的用户
        obj_Market = Market.objects.get(name=data['name'])
        #  执行修改
        obj_Market.name = data['password']
        obj_Market.price = data['price']
        obj_Market.owner = data['owner']
        obj_Market.mobile = data['mobile']
        obj_Market.category = data['category']
        obj_Market.status = data['status']
        obj_Market.image = data['image']
        obj_Market.imageUrl = data['imageUrl']

        try:
            obj_Market.save()
            obj_Markets = Market.objects.all().values()
            # 把结果转化为list
            Markets = list(obj_Markets)
            return JsonResponse({'code': 1, 'data': Markets})
        except Exception as e:
            # 如果出现异常，返回
            return JsonResponse({'code': 0, 'msg': "修改商品信息出现异常，具体错误：" + str(e)})
    except Exception as e:
        return JsonResponse({'code': 0, 'msg': "修改到数据库出现异常，具体：" + str(e)})
    

def query_Markets(request):
    data = json.loads(request.body.decode('utf-8'))

    try:
        obj_Markets = Market.objects.filter(Q(name__contains=data['inputstr']) | Q(price__contains=data['inputstr']) |
                                        Q(mobile__contains=data['inputstr']) | Q(nickname__contains=data['inputstr']) |
                                        Q(catagory__contains=data['inputstr']) | Q(status__contains=data['inputstr'])).values()
        Markets = list(obj_Markets)
        return JsonResponse({'code': 1, 'data': Markets})
    except Exception as e:
        # 异常
        return JsonResponse({'code': 1, 'msg': "查询用户信息失败：" + str(e)})
    
    
def delete_Market(request):
    data = json.loads(request.body.decode("utf-8"))

    #  添加
    try:
        #  查找到要删除的学生
        obj_Market = Market.objects.get(Marketname=data['Marketname'])

        obj_Market.delete()
        try:
            obj_Markets = Market.objects.all().values()
            # 把结果转化为list
            Markets = list(obj_Markets)
            return JsonResponse({'code': 1, 'data': Markets})
        except Exception as e:
            # 如果出现异常，返回
            return JsonResponse({'code': 0, 'msg': "删除商品信息出现异常，具体错误：" + str(e)})
    except Exception as e:
        return JsonResponse({'code': 0, 'msg': "删除到数据库出现异常，具体：" + str(e)})


def delete_Markets(request):
    data = json.loads(request.body.decode('utf-8'))

    try:
        for one_Market in data['Market']:
            obj_Market = Market.objects.get(Marketname=one_Market['Marketname'])
            obj_Market.delete()
        # 获取最后结果
        try:
            obj_Markets = Market.objects.all().values()
            # 把结果转化为listtha
            Markets = list(obj_Markets)
            return JsonResponse({'code': 1, 'data': Markets})
        except Exception as e:
            # 如果出现异常，返回
            return JsonResponse({'code': 0, 'msg': "批量删除用户信息出现异常，具体错误：" + str(e)})
    except Exception as e:
        return JsonResponse({'code': 0, 'msg': "批量删除到数据库出现异常，具体：" + str(e)})


#   随机数
def get_random_str():
    uuid_val = uuid.uuid4()
    uuid_str = str(uuid_val).encode('utf-8')
    md5 = hashlib.md5()
    md5.update(uuid_str)
    return md5.hexdigest()