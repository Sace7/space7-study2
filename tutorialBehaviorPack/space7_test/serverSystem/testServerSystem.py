# -*- coding: utf-8 -*-

import mod.server.extraServerApi as serverApi
import random
import math
import time
ServerSystem = serverApi.GetServerSystemCls()
from ..modCommon import modConfig


class TestServerSystem(serverApi.GetServerSystemCls()):

    def __init__(self, namespace, name):
        super(TestServerSystem, self).__init__(namespace, name)

        self.ListenForEvent("mod名", "发布事件的服务端System名",
                            "事件名称", self, self.事件处理方法)

    # 监听到事件之后,进行逻辑处理的方法
    def 事件处理方法(self, args):
        print "111111111"
        print "222222222"
        # 进行逻辑处理, 比如生成特效, 播放音效之类
        pass