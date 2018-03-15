"""
Question:
Pick one IP from each region, find network latency from via the below code snippet
(ping 3 times), and finally sort the average latency by region.
http://ec2-reachability.amazonaws.com/
"""

from __future__ import print_function
import subprocess
import math

hosts = [{"region":"us-east-1","ip":"23.23.255.255"}, {"region":"us-east-2","ip":"13.58.0.253"}, {"region":"us-west-1","ip":"13.52.0.2"}, {"region":"us-west-2","ip":"34.208.63.251"},{"region":"us-gov-west-1","ip":"52.61.0.254"},{"region":"ca-central-1","ip":"35.182.0.251"},{"region":"sa-east-1","ip":"18.231.0.252"},{"region":"eu-west-1","ip":"34.240.0.253"},{"region":"eu-central-1","ip":"18.194.0.252"},{"region":"eu-west-2","ip":"35.176.0.252"},{"region":"eu-west-3","ip":"35.180.0.253"},{"region":"ap-northeast-1","ip":"13.112.63.251"},{"region":"ap-northeast-2","ip":"13.124.63.251"},{"region":"ap-southeast-1","ip":"13.228.0.251"},{"region":"ap-southeast-2","ip":"13.54.63.252"},{"region":"cn-northwest-1","ip":"52.83.214.0"},{"region":"cn-north-1","ip":"52.80.5.207"},{"region":"ap-south-1","ip":"13.126.0.252"}]
results = []

for host in hosts:
	ping = subprocess.Popen(["ping", "-c", "3", host["ip"]], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
	for outputline in ping.stdout.readlines():
		if "avg" in outputline.decode():
			avg = outputline.decode().split("/")[4]
			results.append({"region":host["region"], "ip": host["ip"], "latency": math.ceil(float(avg))})

results = sorted(results, key= lambda k: k["latency"])

i = 1
for result in results:
	output = str(i) + ". " + result["region"] + " [" + result["ip"] + "] - " + str(result["latency"]) + "ms"
	i += 1
	print (output)







