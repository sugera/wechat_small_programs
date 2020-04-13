'''笑笑'''
'''使用须知：需要先打开一次小程序，保证待测小程序在你最近打开的小程序列表中的第一个'''
'''必须先手动完成小程序位置和用户信息授权'''
import time
import uiautomator2 as u2
from common import devices

#打开微信前，清理一下运行中的程序
devices.kill_server()   #封装好的清理程序函数
d = u2.connect_usb('79URX19315008342')   #此处填写连接在电脑上的devices name

#设备信息
def open():
    print("打开微信--")
    # 打开微信
    d.app_start('com.tencent.mm')
    time.sleep(2)
    # 点击发现
    d.xpath('//*[@resource-id="com.tencent.mm:id/cwx"]').click()
    print("打开小程序--")
    time.sleep(2)
    # 点击小程序
    d.xpath('//*[@text="小程序"]').click()
    # 点击列表中第一个小程序
    d.xpath(
        '//android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/'
        'android.widget.LinearLayout[1]/android.widget.LinearLayout[1]').click()
    time.sleep(5)
open()
time.sleep(1)

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

#返回首页
def return_index():
    d.click(0.054, 0.059)
    time.sleep(1)
    d.click(0.054, 0.059)
    time.sleep(2)
    return print("成功返回首页")

#是否继续购买
while True:
    print("是否继续购买：是（1）/ 否（0）")
    num = input("请输入1或0:")
    if num == "1":
        return_index()
        buy_goods()
    if num == "0":
        break

