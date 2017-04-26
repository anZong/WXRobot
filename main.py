# coding=utf-8
import sys,os,django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ['DJANGO_SETTINGS_MODULE'] = 'collectBugs.settings'
django.setup()

from django.shortcuts import render
from base.models import Bugs
import itchat
from itchat.content import *

RobotName =u'小安'


@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def get_text(msg):
    """处理消息"""
    Bugs.objects.create(user=msg.user.NickName, content=msg.text, result=False)


@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    """下载图片"""
    msg.download('static/'+msg.fileName)
    typeSymbol = {
        PICTURE:'img',
        VIDEO:'vid',
    }.get(msg.type, 'fil')
    Bugs.objects.create(user=msg.user.NickName, img=msg.fileName, result=False)


@itchat.msg_register(FRIENDS)
def add_friend(msg):
    """添加朋友"""
    msg.user.verify()
    msg.user.send('Nice to meet you!')


@itchat.msg_register(TEXT, isGroupChat=True)
def get_text(msg):
    """回复群消息"""
    if msg['isAt'] and msg.Content.startswith(u'@%s' % RobotName):
        itchat.send(u'@%s\u2005 %s' % (msg['ActualNickName'], msg['Content'].replace(u'@%s' % RobotName,'')),msg['FromUserName'])


itchat.auto_login(hotReload = True)
itchat.run(True)