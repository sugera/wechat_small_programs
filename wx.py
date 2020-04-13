# coding: utf-8
import time
import uiautomator2 as u2

d = u2.connect_usb('79URX19315008342')

print("打开微信--")
d.app_start('com.tencent.mm')
# d.click(0.152, 0.902)
time.sleep(2)
#点击发现
d.xpath('//*[@resource-id="com.tencent.mm:id/cwx"]').click()
print("打开小程序--")
time.sleep(2)

#使用优惠券下单流程
#点击小程序
d.xpath('//*[@text="小程序"]').click()
#点击列表中第一个小程序
d.xpath('//android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]').click()
time.sleep(5)
#选择首页商品，加入购物车
d.xpath('//*[@text="wxa2d1f79fd1f0c5d7:pages/index/index.html:VISIBLE"]/android.view.View[3]/android.view.View[1]').click()
time.sleep(1)
d.xpath('//*[@text="加入购物车"]').click()
d.xpath('//*[@text="结算"]').click()
time.sleep(2)
#选择优惠券
# d.xpath('//*[@text="wxa2d1f79fd1f0c5d7:pages/orderConfirm/orderConfirm.html:VISIBLE"]/android.view.View[13]/android.widget.Button[1]/android.widget.Image[2]').click()
# d.xpath('//*[@text="wxa2d1f79fd1f0c5d7:pages/couponSelect/couponSelect.html:VISIBLE"]/android.view.View[1]/android.view.View[2]/android.view.View[6]/android.widget.Image[1]').click()
d.click(0.893, 0.479)
time.sleep(1)
d.click(0.815, 0.155)
d.xpath('//*[@text="确定"]').click()
#付款
d.xpath('//*[@text="wxa2d1f79fd1f0c5d7:pages/orderConfirm/orderConfirm.html:VISIBLE"]/android.view.View[17]/android.view.View[2]').click()
# d.click(0.864, 0.901)
# d.xpath('//*[@resource-id="com.tencent.mm:id/dm3"]').click()
d.click(0.741, 0.532)








# print('打开支付宝')
# d.app_start('com.eg.android.AlipayGphone')
# print('点击蚂蚁森林')
# d.xpath('//*[@text="蚂蚁森林"]').click()
# n = d(descriptionContains='收集').count
# for i in range(n):
#     d.xpath('//*[contains(@content-desc,"收集能量")]').click()
#     print('收集能量成功')
# print('收集能量结束！')