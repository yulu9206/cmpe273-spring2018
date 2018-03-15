import requests
import grequests

def http_call_sync():
    r1 = requests.get('https://httpbin.org/status/200')
    print(r1)

    r2 = requests.get('https://httpbin.org/status/202')
    print(r2)

    r3 = requests.get('https://httpbin.org/status/204')
    print(r3)

def http_call_async():
	urls = [
	    'https://httpbin.org/status/200',
	    'https://httpbin.org/status/202',
	    'https://httpbin.org/status/204'
	]
	req = (grequests.get(u) for u in urls)

	rsp = grequests.map(req)

	print (rsp)

print ("sync calls: ")
http_call_sync()
print ("************************")
print ("async calls: ")
http_call_async()
