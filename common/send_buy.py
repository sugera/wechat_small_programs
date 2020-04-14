'''笑笑'''
'''使用须知：需要先打开一次小程序，保证待测小程序在你最近打开的小程序列表中的第一个'''
'''必须先手动完成小程序位置和用户信息授权'''
'''在门店页面选择外卖或自取下单流程'''
import time
import uiautomator2 as u2
from wechat_small_programs.common import devices


#打开微信前，清理一下运行中的程序
devices.kill_server()   #封装好的清理程序函数
d = u2.connect_usb('79URX19315008342')   #此处填写连接在电脑上的devices name

#打开微信、小程序
devices.open()

#购买商品
def buy_goods():
    #进入分类页面
    d.click(0.378, 0.886)
    time.sleep(1)
    #选择配送方式
    devices.change()
    #购买第一个商品
    d.click(0.352, 0.289)
    time.sleep(1)
    #加入购物车
    d.click(0.488, 0.861)
    time.sleep(1)
    #结算
    d(text="结算").click()
    time.sleep(2)
   #选择优惠券
    d.click(0.896, 0.525)
    time.sleep(1)
    #选择第一张优惠券
    d.xpath(
        '//*[@text="wxa2d1f79fd1f0c5d7:pages/couponSelect/couponSelect.html:VISIBLE"]/android.view.View[1]/android.view.View[2]/'
        'android.view.View[6]/android.widget.Image[1]').click()
    time.sleep(1)
    d(text="确定").click()
    #付款，确定
    time.sleep(1)
    d(text="付款").click()
    time.sleep(2)
    d(resourceId="com.tencent.mm:id/dm3").click()
    return print("成功购买商品")
buy_goods()
time.sleep(3)

#是否继续购买
devices.loop(devices,buy_goods)

