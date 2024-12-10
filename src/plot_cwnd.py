import matplotlib.pyplot as plt

def get_cwnd_and_ssthresh_values(input_file, cwnd_values, ssthresh_values, offset):
    line_num = 0
    with open(input_file, "r") as file:
        for line in file:
            if "RTT:" not in line:
                continue

            if line_num % 2 != offset:
                line_num += 1
                continue

            line_num += 1
            cwnd = int(line.split("CWND:")[1].split()[0])
            cwnd_values.append(cwnd)
            ssthresh = int(line.split("SSTHRESH:")[1].split()[0])
            ssthresh_values.append(ssthresh)

# time_seconds = []
# base_h, base_m, base_s = map(float, times[0].split(":"))
# for t in times:
#     h, m, s = map(float, t.split(":"))
#     time_seconds.append((h * 3600 + m * 60 + s) - (base_h * 3600 + base_m * 60 + base_s))

input_cubic = "data_cubic.txt"
input_bbr = "data_bbr.txt"
cwnd_cubic = []
cwnd_bbr = []
ssthresh_cubic = []
ssthresh_bbr = []

get_cwnd_and_ssthresh_values(input_cubic, cwnd_cubic, ssthresh_cubic, 1)
get_cwnd_and_ssthresh_values(input_bbr, cwnd_bbr, ssthresh_bbr, 1)
# min_len = min(len(cwnd_cubic), len(cwnd_bbr))
# cwnd_cubic = cwnd_cubic[:min_len]
# cwnd_bbr = cwnd_bbr[:min_len]
# ssthresh_cubic = ssthresh_cubic[:min_len]
# ssthresh_bbr = ssthresh_bbr[:min_len]

# times = []
# for i, _ in enumerate(cwnd_cubic):
#     times.append(i * 0.1)

time_cubic = []
for i, _ in enumerate(cwnd_cubic):
    time_cubic.append(i * 0.1)

time_bbr = []
for i, _ in enumerate(cwnd_bbr):
    time_bbr.append(i * 0.1)

plt.figure(figsize=(10, 6))
# plt.plot(time_cubic, cwnd_cubic, marker="o", label="Cubic")
# plt.plot(time_bbr, cwnd_bbr, marker="o", label="BBR")
# plt.plot(time_cubic, ssthresh_cubic, marker="o", linestyle='--', label="Cubic Slow Start Threshold") 
# plt.plot(time_bbr, ssthresh_bbr, marker="o", linestyle='--', label="BBR Slow Start Threshold")
plt.plot(time_cubic, cwnd_cubic, label="Cubic")
plt.plot(time_bbr, cwnd_bbr, label="BBR")
plt.plot(time_cubic, ssthresh_cubic, linestyle='--', label="Cubic Slow Start Threshold") 
plt.plot(time_bbr, ssthresh_bbr, linestyle='--', label="BBR Slow Start Threshold")
plt.yscale('log')
plt.xlabel("Time (seconds)")
plt.ylabel("Logarithmic CWND Size (segments)")
plt.title("Congestion Window (CWND) Size vs Time")
plt.legend()
plt.savefig("plots/plot_2_3.png")
# plt.show()
