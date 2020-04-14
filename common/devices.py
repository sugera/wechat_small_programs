'''公用模块'''
import uiautomator2 as u2
import time
d = u2.connect_usb('79URX19315008342')
# 清空正在运行中的进程
def kill_server():
    d.xpath('//*[@resource-id="com.android.systemui:id/white"]').click()
    d.xpath('//*[@resource-id="com.android.systemui:id/recent_apps"]').click()
    d.xpath('//*[@resource-id="com.huawei.android.launcher:id/clear_all_recents_image_button"]').click()
    return print("结束运行中的进程")

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
    time.sleep(4.5)

#返回首页
def return_index():
    d.click(0.054, 0.059)
    time.sleep(1)
    d.click(0.054, 0.059)
    time.sleep(2)
    return print("成功返回首页")

#循环购买
def loop(name,buy_goods):
    while True:
        print("是否继续购买：是（1）/ 否（0）")
        num = input("请输入1或0:")
        if num == "1":
            name.return_index()
            buy_goods()
        if num == "0":
            break

#外卖模式
def send():
    # 选择外卖模式
    d(text="外卖").click()
    time.sleep(1)
    # 选择收货地址(列表第一个)
    d.click(0.498, 0.126)
    time.sleep(1)
    return print("切换外卖模式")

#自提模式
def bring():
    d(text="自提").click()
    time.sleep(1)
    d(text="去下单").click()
    time.sleep(1)
    return print("切换自取模式")


#选择配送方式
def change():
    num = input("请输入配送方式：外卖（0）/自取（1）")
    if num =="0":
        send()
    if num == "1":
        bring()
    pass

#领取优惠券，10元代金券
def take_coupon():
    #点击我的页面
    d.click(0.87, 0.886)
    time.sleep(1)
    d(text="领券中心").click()
    time.sleep(1)
    if d(text="10元代金券"):
        d(text="立即领取").click()
        print("成功领取优惠券")
        time.sleep(1)
    else:
        print("没有你想要的优惠券")

