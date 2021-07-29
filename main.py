import requests
import json

# ดึงค่า API Json จาก เป้าหมาย
response = requests.get('http://103.167.193.24:30120/players.json')
data = response.json() 

# ทำการแสดงค่าต่างๆที่ดึงมา ตัวอย่าง ชื่อผู้เล่น กับ Ping ของผู้เล่น
for get_data in data:
     print (('ชื่อผู้เล่น :'),get_data['name'] , (' ||||| ') ,('Ping :'),get_data['ping'])
