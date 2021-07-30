import requests
import time
# ดึงค่า API Json จาก เป้าหมาย
ip_user = input('IP Server : ')
response = requests.get('http://'+ip_user+':30120/players.json')
data = response.json() 


# ทำการแสดงค่าต่างๆที่ดึงมา ตัวอย่าง ชื่อผู้เล่น กับ Ping ของผู้เล่น
while True:
     for get_data in data:
          print (('ชื่อผู้เล่น :'),get_data['name'] , (' ||||| ') ,('Ping :'),get_data['ping'])
          print('=============================================')
     time.sleep(5)