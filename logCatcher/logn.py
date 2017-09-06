from matplotlib import pyplot as plt 
from sys import argv

logfile = argv[1]
n=int(argv[2])
with open (logfile,"r") as f:
    log=f.readlines()
ip=[i.split()[0] for i in log]
uniq_ip = list()
[uniq_ip.append(i) for i in ip if i not in uniq_ip]
freq = list()
[freq.append(ip.count(i)) for i in uniq_ip if i not in freq]
eq = sorted(zip(freq, uniq_ip), reverse=True)
y_axis  = [i[0] for i in eq]
x_axis  = range(len(y_axis))
x_label = [i[1] for i in eq]
plt.plot(x_axis[:n], y_axis[:n], marker='.')
plt.title(argv[1]+" Dosya Analizi")
plt.ylabel("Toplam İstek")
plt.xlabel("İp Adresleri")
plt.grid(True)
plt.xticks(x_axis[:n], x_label[:n], rotation=90)
plt.yticks(range(0,max(y_axis),50))
plt.show()    