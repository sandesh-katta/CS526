import pyshark

# http response code 0 means an unreachable server
filtered_trace = pyshark.FileCapture("project2_part1.pcap", display_filter='http and http.response.code != 0')

http_server_set = set()

for packet in filtered_trace:
	http_server_set.add(packet.ip.src)

print("HTTP servers that were involved in a valid HTTP response:")
print(sorted(http_server_set))
print("no of such servers:", len(http_server_set))