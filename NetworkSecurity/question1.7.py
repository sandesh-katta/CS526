import csv

with open('data_tcp_sequences.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    tcp_endpoint_dict = {}

    tcps = set()

    header =0 

    for row in csv_reader:
        if(header==0):
            header = header+1
            continue
        src_ip = row[2]
        dst_ip = row[3]
        seqno = int(row[6])
        seqno_set = set()
        tcps.add(seqno)
        endpoint = src_ip
        if endpoint in tcp_endpoint_dict:
                seqno_set = tcp_endpoint_dict[endpoint]
        seqno_set.add(seqno)
        tcp_endpoint_dict[endpoint] = seqno_set

    endpoint_list=[]
    for endpoint in tcp_endpoint_dict:
            seqno_list = list(tcp_endpoint_dict[endpoint])
            diff = max(seqno_list) - min(seqno_list)
            if (len(seqno_list) >= 5 ):
                    endpoint_list.append((endpoint,diff))

    endpoint_list.sort(key=lambda y: y[1])

    print("TCP endpoint with top two broadest coverage ")
    print(endpoint_list[-1])
    print(endpoint_list[-2])