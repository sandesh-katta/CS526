import pyshark

input_trace = pyshark.FileCapture("project2_part1.pcap", display_filter='ftp and ftp.response.code == 530')

malicious_host_ip = {}

for packet in input_trace:
	dest_ip = packet.ip.dst
	if dest_ip in malicious_host_ip:
		malicious_host_ip[dest_ip] = malicious_host_ip[dest_ip] + 1
	else:
		malicious_host_ip[dest_ip] = 1

print("Potentially malicious Host(s):")

for key in malicious_host_ip:
	if malicious_host_ip[key] > 3:
		print (key)