
import numpy as np
from pathlib import Path

# Folder containing the GNU Radio recordings
folder = Path.home() / "OneDrive" / "Desktop" / "SDR_Projects"

# Read transmitted and received bits
tx = np.fromfile(folder / "tx_bits.bin", dtype=np.uint8)
rx = np.fromfile(folder / "rx_bits.bin", dtype=np.uint8)

# Display information
print("Transmitted bits:", len(tx))
print("Received bits:", len(rx))

print("First 20 transmitted bits:", tx[:20])
print("First 20 received bits:", rx[:20])

print("TX unique values:", np.unique(tx))
print("RX unique values:", np.unique(rx))


# Find the alignment between transmitted and received bits

best_offset = None
best_errors = len(rx) + 1
best_count = 0

for offset in range(-100, 101):

    if offset >= 0:
        # Received sequence starts later than transmitted sequence
        tx_start = offset
        rx_start = 0
    else:
        # Received sequence starts earlier than transmitted sequence
        tx_start = 0
        rx_start = -offset

    count = min(len(tx) - tx_start, len(rx) - rx_start)

    if count <= 0:
        continue

    tx_aligned = tx[tx_start:tx_start + count]
    rx_aligned = rx[rx_start:rx_start + count]

    errors = np.count_nonzero(tx_aligned != rx_aligned)

    if errors / count < best_errors / max(best_count, 1):
        best_errors = errors
        best_offset = offset
        best_count = count

print("\nAlignment results")
print("Best offset:", best_offset)
print("Compared bits:", best_count)
print("Bit errors:", best_errors)
print("BER:", best_errors / best_count)


# Calculate BER using the fixed alignment offset

offset = 3

count = min(len(tx) - offset, len(rx))

tx_aligned = tx[offset:offset + count]
rx_aligned = rx[:count]

errors = np.count_nonzero(tx_aligned != rx_aligned)

ber = errors / count

print("\nBPSK BER Results (Noise Voltage = 1.0)")
print("Compared bits:", count)
print("Bit errors:", errors)
print("BER:", ber)
