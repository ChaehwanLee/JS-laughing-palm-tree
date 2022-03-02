import random
import time
import urllib.request

def send():
    for i in range(1,10):
        id = 'h01';
        temp = random.randint(1,30);
        el = random.randint(1,100);
        # id=h01&temp=10&el=100
        url = 'http://127.0.0.1:8088/iot?id='+id+'&temp='+str(temp)+'&el='+str(el);
        urllib.request.urlopen(url);
        time.sleep(3);


if __name__ == '__main__':
    send();

