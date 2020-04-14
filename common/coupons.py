'''领取优惠券'''

from wechat_small_programs.common import devices
#结束运行进程
devices.kill_server()
#打开微信，小程序
devices.open()
#领取10张卡券
for i in range(0,10):
    if i < 10:
        devices.take_coupon()
print("成功领取10张优惠券")
devices.return_index()

