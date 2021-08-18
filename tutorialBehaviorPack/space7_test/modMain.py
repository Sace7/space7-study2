# -*- coding: utf-8 -*-
# 上面这行是让这个文件按utf-8进行编码，这样就可以在注释中写中文了

# 这行是import到MOD的绑定类Mod，用于绑定类和函数
from mod.common.mod import Mod
# 这行import到的是引擎服务端的API模块
import mod.server.extraServerApi as serverApi
# 这行import到的是引擎客户端的API模块
import mod.client.extraClientApi as clientApi
from space7DragonBall.modCommon import modConfig


# 用Mod.Binding来绑定MOD的类，引擎从而能够识别这个类是MOD的入口类
@Mod.Binding(name=modConfig.ModName, version=modConfig.ModVersion)
class TutorialMod(object):

    # 类的初始化函数
    def __init__(self):
        print("===== init modConfig.ModName mod =====")

    # InitServer绑定的函数作为服务端脚本初始化的入口函数，通常是用来注册服务端系统system和组件component
    @Mod.InitServer()
    def ServerInit(self):
        print("===== init modConfig.ModName server =====")
        # 注册服务端系统
        serverApi.RegisterSystem(modConfig.ModName, modConfig.ServerSystemName, modConfig.ServerSystemPath)

        # 以下不用改,多模组共用
        # 如果rank服务端没有被注册,则注册rank服务端,用于处理rank,多模组联动只会有一个服务端系统
        if not serverApi.GetSystem("Space7DragonBall", "RankServerSystem"):
            serverApi.RegisterSystem("Space7DragonBall", "RankServerSystem", modConfig.RankServerSystem)

    # DestroyServer绑定的函数作为服务端脚本退出的时候执行的析构函数，通常用来反注册一些内容,可为空
    @Mod.DestroyServer()
    def ServerDestroy(self):
        print("===== destroy modConfig.ModName server =====")

    # InitClient绑定的函数作为客户端脚本初始化的入口函数，通常用来注册客户端系统system和组件component
    @Mod.InitClient()
    def ClientInit(self):
        print("===== init modConfig.ModName client =====")

        # 下面内容注册自定义Component
        # 拔刀Component  用于更新用户的拔刀操作
        clientApi.RegisterComponent(modConfig.ModName, "DragonBallComponent",
                                    "space7DragonBall.componentSystem.DragonBallComponent.DragonBallComponent")
        clientApi.RegisterComponent(modConfig.ModName, "DragonBallChangeComponent",
                                    "space7DragonBall.componentSystem.DragonBallChangeComponent.DragonBallChangeComponent")
        clientApi.RegisterComponent(modConfig.ModName, "DragonBallExposionComponent",
                                    "space7DragonBall.componentSystem.DragonBallExposionComponent.DragonBallExposionComponent")

        # 注册客户端系统
        clientApi.RegisterSystem(modConfig.ModName, modConfig.ClientSystemName, modConfig.ClientSystemPath)
        # 注册客户端UI系统
        clientApi.RegisterSystem(modConfig.ModName, modConfig.MainUISystemName, modConfig.MainUISystemPath)

        # 以下不用改,多模组共用
        if not clientApi.GetSystem("space7DragonBall", "rankUISystem"):
            clientApi.RegisterSystem("space7DragonBall", "rankUISystem", modConfig.rankUISystem)
        # 多模组时,只需要一个rankSystem
        if not clientApi.GetSystem("space7DragonBall", "RankClientSystem"):
            clientApi.RegisterSystem("space7DragonBall", "RankClientSystem", modConfig.RankClientSystem)


    # DestroyClient绑定的函数作为客户端脚本退出的时候执行的析构函数，通常用来反注册一些内容,可为空
    @Mod.DestroyClient()
    def TutorialClientDestroy(self):
        print("===== destroy modConfig.ModName client =====")
