import matplotlib.pyplot as plt




# Create figure and axis
fig, ax = plt.subplots(figsize=(12, 10))

# Define boxes for the flowchart
boxes = {
    "Start": (0.5, 0.95),
    "Initialize particles and MLP weights": (0.5, 0.85),
    "Evaluate fitness of each particle (MLP with current weights)": (0.5, 0.75),
    "Update personal and global best": (0.5, 0.65),
    "Update velocity": (0.3, 0.55),
    "Update position (MLP weights)": (0.7, 0.55),
    "Stopping criterion met?": (0.5, 0.4),
    "Predict ROP using trained MLP": (0.5, 0.25),
    "End": (0.5, 0.1),
}

# Draw the boxes
for text, (x, y) in boxes.items():
    ax.text(x, y, text, ha='center', va='center',
            bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgray"))

# Define arrows for the flowchart
arrows = [
    ("Start", "Initialize particles and MLP weights"),
    ("Initialize particles and MLP weights", "Evaluate fitness of each particle (MLP with current weights)"),
    ("Evaluate fitness of each particle (MLP with current weights)", "Update personal and global best"),
    ("Update personal and global best", "Update velocity"),
    ("Update personal and global best", "Update position (MLP weights)"),
    ("Update velocity", "Update position (MLP weights)"),
    ("Update position (MLP weights)", "Stopping criterion met?"),
    ("Stopping criterion met?", "Predict ROP using trained MLP"),
    ("Predict ROP using trained MLP", "End"),
]

# Draw the arrows
for start, end in arrows:
    start_x, start_y = boxes[start]
    end_x, end_y = boxes[end]
    ax.annotate("", xy=(end_x, end_y + 0.03), xytext=(start_x, start_y - 0.03),
                arrowprops=dict(arrowstyle="->", lw=1.5))

# Decision arrow (Stopping criterion met?)
ax.annotate("", xy=(0.5, 0.38), xytext=(0.5, 0.23), arrowprops=dict(arrowstyle="->", lw=1.5))
ax.annotate("", xy=(0.5, 0.38), xytext=(0.5, 0.52), arrowprops=dict(arrowstyle="->", lw=1.5))
ax.text(0.52, 0.45, "No", ha='left', va='center')
ax.text(0.52, 0.3, "Yes", ha='left', va='center')

# Set axis limits and remove axis
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Display the flowchart
plt.title("Flowchart of MLP-PSO for ROP Prediction")
plt.show()

