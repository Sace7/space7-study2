import mod.client.extraClientApi as clientApi
ClientSystem = clientApi.GetClientSystemCls()
from ..modCommon import modConfig

class TestClientSystem(ClientSystem):

    def __init__(self, namespace, systemName):
        ClientSystem.__init__(self, namespace, systemName)


        self.ListenForEvent("mod名", "发布事件的服务端System名",
                            "事件名称", self, self.事件处理方法)


    # 监听到事件之后,进行逻辑处理的方法
    def 事件处理方法(self, args):
        # 进行逻辑处理, 比如生成特效, 播放音效之类
        pass