import matplotlib.pyplot as plt
import re
import sys

if len(sys.argv) < 2:
    print("Usage: python plot_power.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

try:
    with open(filename, 'r') as f:
        content = f.read()
except FileNotFoundError:
    print(f"Error: couldn't find {filename}")
    sys.exit(1)

# Parse power readings from the file
lines = content.strip().split('\n')
watts = []
for line in lines:
    parts = line.split(',')
    if len(parts) >= 1:
        power_str = parts[0].strip().rstrip('W')
        try:
            watts.append(float(power_str))
        except ValueError:
            continue  # Skip lines that can't be parsed

if not watts:
    print("No power readings found")
    sys.exit(1)

# Plot the data
plt.figure(figsize=(12, 6))
plt.plot(watts, marker='o', markersize=2, linewidth=0.5)
plt.xlabel('Reading Number')
plt.ylabel('Power (W)')
plt.title(f'Power Readings Over Time - {filename} ({len(watts)} measurements)')
plt.grid(True, alpha=0.3)
plt.tight_layout()

# Show statistics
print(f"File: {filename}")
print(f"Total readings: {len(watts)}")
print(f"Average power: {sum(watts)/len(watts):} W")
print(f"Total energy: {(sum(watts)/len(watts))*1800:} J")  # for 30 min run
print(f"Min power: {min(watts):.3f} W")
print(f"Max power: {max(watts):.3f} W")

plt.show()