import matplotlib.pyplot as plt

def get_throughput_values(input_file, throughput_values):
    line_num = 0
    with open(input_file, "r") as file:
        for line in file:
            if "[  5]" not in line or "sec" not in line:
                continue
                
            throughput = float(line.split("Bytes")[1].split()[0])
            throughput_values.append(throughput)

input_cubic = "data_cubic.txt"
input_bbr = "data_bbr.txt"
throughput_cubic = []
throughput_bbr = []

get_throughput_values(input_cubic, throughput_cubic)
get_throughput_values(input_bbr, throughput_bbr)

time_cubic = []
for i, _ in enumerate(throughput_cubic):
    time_cubic.append(i)

time_bbr = []
for i, _ in enumerate(throughput_bbr):
    time_bbr.append(i)

plt.figure(figsize=(10, 6))
plt.plot(time_cubic, throughput_cubic, label="Cubic")
plt.plot(time_bbr, throughput_bbr, label="BBR")
# plt.yscale('log')
plt.xlabel("Time (seconds)")
plt.ylabel("Throughput (kbps)")
plt.title("Throughput vs Time")
plt.legend()
plt.savefig("plots/plot_3_2.png")
# plt.show()
