'''笑笑'''
'''使用须知：需要先打开一次小程序，保证待测小程序在你最近打开的小程序列表中的第一个'''
'''必须先手动完成小程序位置和用户信息授权'''
'''首页广告位自取下单流程'''
import time
import uiautomator2 as u2
from wechat_small_programs.common import devices

#打开微信前，清理一下运行中的程序
devices.kill_server()   #封装好的清理程序函数
d = u2.connect_usb('79URX19315008342')   #此处填写连接在电脑上的devices name

#打开微信，进入小程序
devices.open()

#购买商品
def buy_goods():
    #进入小程序首页
    d.click(0.131, 0.892)
    time.sleep(2)
    #购买第一个商品
    d.click(0.233, 0.252)
    time.sleep(2)
    #加入购物车
    d.click(0.506, 0.803)
    time.sleep(1)
    #结算
    d.click(0.838, 0.808)
    time.sleep(2)
   #选择优惠券
    d.click(0.885, 0.479)
    time.sleep(1)
    #选择第一张优惠券
    d.xpath(
        '//*[@text="wxa2d1f79fd1f0c5d7:pages/couponSelect/couponSelect.html:VISIBLE"]/android.view.View[1]/android.view.View[2]/'
        'android.view.View[6]/android.widget.Image[1]').click()
    time.sleep(1)
    d(text="确定").click()
    #付款，确定
    time.sleep(1)
    d.click(0.866, 0.9)
    time.sleep(1)
    d(resourceId="com.tencent.mm:id/dm3").click()
    return print("成功购买商品")
buy_goods()
time.sleep(3)

devices.loop(devices,buy_goods)

