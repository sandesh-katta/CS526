import pyshark

input_trace = pyshark.FileCapture("project2_part1.pcap", display_filter='ftp and ftp.response.code == 230')


tcp_streams = set()

for packets in input_trace:
	tcp_streams.add(int(packets.tcp.stream))
	

print("List of tcp streams")
print(sorted(tcp_streams))