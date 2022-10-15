import pyshark
from packaging import version
from functools import cmp_to_key

def cmp_versions(a, b):
	if (version.parse(a) < version.parse(b)):
		return -1
	elif (version.parse(b) < version.parse(b)):
		return 0
		
	return 1

input_trace = pyshark.FileCapture("project2_part1.pcap", display_filter='http and http.server contains "Apache/"')

server_version = {}


for packet in input_trace:
	server = (packet.http.server).split(' ')[0] 
	server = server.replace('Apache/', '')
	src_ip = packet.ip.src 
	src_ip_set = set()
	if server in server_version:
		src_ip_set = server_version[server]
	
	src_ip_set.add(src_ip)
	server_version[server] = src_ip_set



versionList = [*server_version]
versionList.sort(key=cmp_to_key(cmp_versions))


print("Oldest version:", versionList[0], "HTTP server with this version:", server_version[versionList[0]])