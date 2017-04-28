# coding=utf-8
from django.shortcuts import render
from .models import Bugs
from django.views import generic
from django.contrib import staticfiles


class IndexView(generic.ListView):
    """获取bug列表"""
    template_name = 'index.html'
    context_object_name = 'bugs_list'
    def get_queryset(self):
        return Bugs.objects.order_by('-id')


def SignView(request,bug_id):
    """标记状态"""
    bug = Bugs.objects.get(id=bug_id)
    bug.result = True
    bug.save()
    return render(request,'index.html',{'bugs_list':Bugs.objects.order_by('-id')})