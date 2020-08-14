import http.client

conn = http.client.HTTPSConnection("secure.smslink.ro")
 
#
#  Get your SMSLink / SMS Gateway Connection ID and Password from 
#  https://www.smslink.ro/get-api-key/
#

conn.request("GET", "/sms/gateway/communicate/index.php?connection_id=MyConnectionID&password=MyConnectionPassword&to=07xyzzzzzz&message=MyMessage")

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))