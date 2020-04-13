'''要连接的设备信息'''
import uiautomator2 as u2
d = u2.connect_usb('79URX19315008342')
# 清空正在运行中的进程
def kill_server():
    d.xpath('//*[@resource-id="com.android.systemui:id/white"]').click()
    d.xpath('//*[@resource-id="com.android.systemui:id/recent_apps"]').click()
    d.xpath('//*[@resource-id="com.huawei.android.launcher:id/clear_all_recents_image_button"]').click()
    return print("结束运行中的进程")
