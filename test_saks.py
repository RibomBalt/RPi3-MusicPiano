from sakshat import SAKSHAT
import time
saks = SAKSHAT()
# 测试led灯
for i in range(8):
    saks.ledrow.on_for_index(i)
    time.sleep(0.5)
    saks.ledrow.off_for_index(i)
# 测试数码管
for x in ('6.6.6.6', '23.33', '8888', '8#8#.','####'):
    saks.digital_display.show(x)
    time.sleep(0.5)
    
# 测试蜂鸣器
saks.buzzer.beep(0.02)
print('测试完成')
