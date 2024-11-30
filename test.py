import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# Data from the table
pdf_counts = np.array([1, 3, 5, 30, 40, 64, 80, 100])  # Number of PDFs
non_hadoop = np.array([5, 12, 35, 588, 610, 727,790, 847])  # Non-Hadoop-based times
hadoop = np.array([10, 20, 45, 420, 435, 470, 500, 546])  # Hadoop-based times

# Generate smooth curves using interpolation
x_smooth = np.linspace(pdf_counts.min(), pdf_counts.max(), 500)
non_hadoop_smooth = make_interp_spline(pdf_counts, non_hadoop)(x_smooth)
hadoop_smooth = make_interp_spline(pdf_counts, hadoop)(x_smooth)

# Plotting the graph
plt.figure(figsize=(8, 5))
plt.plot(x_smooth, non_hadoop_smooth, label="Non-Hadoop Based", color="red", linewidth=2)
plt.plot(x_smooth, hadoop_smooth, label="Hadoop Based", color="blue", linewidth=2)

# Adding labels, title, and legend
plt.title("Comparison of Time Taken: Non-Hadoop vs Hadoop Based", fontsize=14)
plt.xlabel("Number of PDFs", fontsize=12)
plt.ylabel("Time Taken (seconds)", fontsize=12)
plt.legend(fontsize=12)
plt.grid(True, linestyle="--", alpha=0.7)

# Show the plot
plt.show()
