import urllib, json
from time import sleep
import os

#Dependencies:
#sudo gem install terminal-notifier

#Running in background:
#python zebpay_bitcoin_price_notifier.py > /dev/null &

#Output:
#Generates on-screen notifications for Mac, for changes in Bitcoin prices on Zebpay portal.

# The notifier function
def notify(title, subtitle, message):
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    os.system('terminal-notifier {}'.format(' '.join([m, t, s])))

# Calling the function
def buy_notify(previous,new):
        notify(title    = 'Buy Bitcoin',subtitle = 'Great Deal',message  = 'Price slashed from '+str(previous)+' to '+str(new))


# Calling the function
def just_notify(previous,new):
        notify(title    = 'Bitcoin status',subtitle = ''+str(new) ,message  = 'Previous '+str(previous))

if __name__ == '__main__':
        url = "https://www.zebapi.com/api/v1/market/ticker/btc/inr"
        response = urllib.urlopen(url)
        data = json.loads(response.read())
        new =  int(data['buy'])
        while True:
                previous=new
                url = "https://www.zebapi.com/api/v1/market/ticker/btc/inr"
                response = urllib.urlopen(url)
                data = json.loads(response.read())
                new =  int(data['buy'])
                if previous < new :
                                print("RISE!")
                                just_notify(previous,new)
                if previous > new :
                                print("FALL!")
                                just_notify(previous,new)
                if previous - new > 5000:
                                print("BUY!")
                                buy_notify(previous,new)
    
                print(new)
                sleep(20)
