
import matplotlib.pyplot as plt

# Noise voltage values tested in GNU Radio
noise_voltage = [0.0, 0.2, 0.5, 0.8, 1.0]

# Measured Bit Error Rate values
ber = [0.0, 0.0, 0.0015012, 0.0426341, 0.0773619]

# Plot BER against noise voltage
plt.plot(noise_voltage, ber, marker='o')

# Add labels and title
plt.xlabel("Noise Voltage")
plt.ylabel("Bit Error Rate (BER)")
plt.title("BPSK BER vs Noise Voltage")

# Add grid
plt.grid(True)

# Save graph as PNG
plt.savefig("bpsk_ber_vs_noise.png", dpi=300)

# Display graph
plt.show()
