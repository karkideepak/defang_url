import csc
for collections import Counter

THRESHOLD = 30

ip_counter = Counter()

with open("traffic.csv", newline-"") as csvfile
  reader = csv.DictReader(csvfile)

  for row in reader:
    src_ip = row.get("ip.src")
    
    if src_ip:
      ip_counter[sc_ip] +=1
      
print ("traffic voolume per source:\n")

for ip, count in ip_counter.items():
  print(f"{ip}: {count} packets)
