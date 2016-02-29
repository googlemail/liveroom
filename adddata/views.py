#coding=utf-8
from django.shortcuts import render,HttpResponse
from .models import room
from django.views import generic
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def Zhuye(request):
    dt = datetime.now()
    extime = dt.strftime('%Y%m%d%H%M%S')
    extime = extime[0:10]
    allroom = room.objects.all().filter(updatetime__startswith=extime)
    douyu = allroom.filter(sitename ="douyu tv").order_by('-renqi')
    douyu = douyu[:4]
    huya = allroom.filter(sitename ="huya").order_by('-renqi')
    huya = huya[:4]
    PandaTv = allroom.all().filter(sitename ="pandatv").order_by('-renqi')
    PandaTv = PandaTv[:4]
    plu = allroom.all().filter(sitename ="plu").order_by('-renqi')
    plu = plu[:4]
    qf56 = allroom.all().filter(sitename ="56").order_by('-renqi')
    qf56 = qf56[:4]
    chushou = allroom.all().filter(sitename ="chushou").order_by('-renqi')
    chushou = chushou[:4]
    zhanqi = allroom.all().filter(sitename ="zhanqiTV").order_by('-renqi')
    zhanqi = zhanqi[:4]
    alltag = room.tags.all()
    alltag = alltag[:50]
    allwebsite = [douyu,huya,PandaTv,plu,qf56,zhanqi,chushou]
    siteurl = [{'websiteurl':'douyutv','websitenamecn':'斗鱼TV排行',"websitealllist":douyu},{'websiteurl':'huya','websitenamecn':'虎牙TV排行',"websitealllist":huya},{'websiteurl':'PandaTv','websitenamecn':'熊猫TV排行',"websitealllist":PandaTv},
    {'websiteurl':'zhanqiTV','websitenamecn':'战旗TV',"websitealllist":zhanqi},{'websiteurl':'chushou','websitenamecn':'触手TV',"websitealllist":chushou},{'websiteurl':'plu','websitenamecn':'龙珠排行',"websitealllist":plu},{'websiteurl':'56','websitenamecn':'千帆56排行',"websitealllist":qf56},]
    return render(request,"adddata/cesi.html",{
        "allwebsite":allwebsite,
        "siteurl":siteurl,
        'alltag':alltag,
        })
    
def Listroom(request,question_id):
    if question_id == "douyutv":
        question_id = "douyu tv"
    dt = datetime.now()
    extime = dt.strftime('%Y%m%d%H%M%S')
    extime = extime[0:2]
    allroom = room.objects.all().filter(updatetime__startswith=extime)
    roomlist = allroom.filter(sitename = question_id).order_by('-renqi')
    objects, page_range = my_pagination(request, roomlist)
    return render(request,'adddata/all.html',{'room':objects,"page_range": page_range,})

def My_pagination(request, queryset, display_amount=40, after_range_num = 5,bevor_range_num = 4):
    paginator = Paginator(queryset, display_amount)
    try:
        page =int(request.GET.get('page'))
    except:
        page = 1
    try:
        objects = paginator.page(page)
    except EmptyPage:
        objects = paginator.page(paginator.num_pages)
    except:
        objects = paginator.page(1)
    if page >= after_range_num:
        page_range = paginator.page_range[page-after_range_num:page+bevor_range_num]
    else:
        page_range = paginator.page_range[0:page+bevor_range_num]
    return objects,page_range
