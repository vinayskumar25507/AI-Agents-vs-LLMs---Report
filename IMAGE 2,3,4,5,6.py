import matplotlib.pyplot as plt
import numpy as np

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Set a professional style for academic publication
plt.style.use('seaborn-v0_8-paper')
sns.set_context("paper", font_scale=1.5)

# ---------------------------------------------------------
# CHART 2: FOREST PLOT (AGENTIC BOOST)
# ---------------------------------------------------------
studies = ["Agent Q (WebShop)", "M3Builder (Medical)", "Agent-Judge (DevAI)", "SWE-bench (Repair)"]
baseline_sr = [18.6, 44.0, 70.0, 5.0]
agentic_sr = [95.4, 94.3, 90.0, 58.0]

fig, ax1 = plt.subplots(figsize=(10, 6))
y_pos = np.arange(len(studies))

# Horizontal Bar for Agentic Boost
ax1.barh(y_pos + 0.2, agentic_sr, height=0.4, label='Agentic Framework', color='#3498db', alpha=0.8)
ax1.barh(y_pos - 0.2, baseline_sr, height=0.4, label='Baseline LLM', color='#e74c3c', alpha=0.8)

ax1.set_yticks(y_pos)
ax1.set_yticklabels(studies)
ax1.set_xlabel('Success Rate (%)')
ax1.set_title('Figure 2: Success Rate Delta Across Primary Benchmarks')
ax1.legend(loc='lower right')
plt.tight_layout()
plt.savefig('forest_plot.png', dpi=300)

# --- FIGURE 3: FOREST PLOT ---
studies = [
    "Agent Q (2024)", "M3Builder (2025)", "AutoAgent (2025)", "LATS (2024)",
    "Clinician Agent (2025)", "SWE-agent (2024)", "OpenDevin (2024)",
    "MetaGPT (2023)", "ChemCrow (2023)", "Voyager (2023)"
]
# Improvement over baseline (Mean % Delta)
effect_sizes = [340, 210, 180, 165, 150, 140, 130, 110, 95, 80]
# Confidence Intervals (Error bars)
errors = [20, 15, 18, 12, 10, 14, 12, 10, 8, 15]

plt.figure(figsize=(10, 6))
plt.errorbar(effect_sizes, range(len(studies)), xerr=errors, fmt='o', color='black', ecolor='gray', capsize=5, label='Mean Effect Size (95% CI)')
plt.axvline(x=0, color='red', linestyle='--', label='No Improvement (Baseline)')
plt.yticks(range(len(studies)), studies)
plt.xlabel('Success Rate Improvement over Zero-Shot LLM (%)')
plt.title('Fig. 3. Forest Plot of Agentic Performance Delta (Random Effects Model)')
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('Fig6_ForestPlot.png', dpi=300)
plt.show()

# ---------------------------------------------------------
# CHART 4: ACCURACY-COST PARETO FRONTIER
# ---------------------------------------------------------
# Data from the meta-analysis
systems = [
    "Llama-3 70B (Zero-Shot)", 
    "Agent Q", 
    "Standard Open-Source", 
    "Claude 3.5 Sonnet Agent", 
    "ReAct Scaffold", 
    "AutoAgent", 
    "M3Builder", 
    "HAL Average Baseline", 
    "HAL Frontier Agent"
]

# X-Axis: Estimated Inference Cost (USD)
x_cost = [0.01, 1.85, 0.02, 3.50, 0.85, 1.40, 2.10, 0.01, 4.00]
# Y-Axis: Task Success Rate (SR%)
y_success = [18.6, 81.7, 0.0, 58.0, 33.5, 68.2, 94.3, 22.0, 78.2]

# Categories for coloring and legend
categories = [
    "Monolithic Baseline",
    "MCTS / Tree-Search",
    "Monolithic Baseline",
    "Multi-Agent System",
    "Single-Agent Loop",
    "Self-Evolving Agent",
    "Multi-Agent System",
    "Monolithic Baseline",
    "Complex Scaffold"
]

# Set up the figure with high resolution (600 DPI for IEEE print standards)
plt.figure(figsize=(10, 6), dpi=600)

# Define specific colors and markers for each architecture category
cat_styles = {
    "Monolithic Baseline": {"color": "gray", "marker": "o"},
    "MCTS / Tree-Search": {"color": "blue", "marker": "^"},
    "Multi-Agent System": {"color": "green", "marker": "s"},
    "Single-Agent Loop": {"color": "orange", "marker": "D"},
    "Self-Evolving Agent": {"color": "purple", "marker": "P"},
    "Complex Scaffold": {"color": "red", "marker": "*"}
}

# Plot scatter points and add labels next to each point
for i in range(len(systems)):
    cat = categories[i]
    style = cat_styles[cat]
    plt.scatter(x_cost[i], y_success[i], color=style["color"], marker=style["marker"], s=100, zorder=3)
    # Offset the text slightly so it doesn't overlap the marker
    plt.annotate(systems[i], (x_cost[i], y_success[i]), textcoords="offset points", xytext=(5,-10), ha='left', fontsize=8)

# Create dummy scatter plots just to populate the Legend properly
for cat, style in cat_styles.items():
    plt.scatter([], [], color=style["color"], marker=style["marker"], label=cat)

# Draw the Pareto Frontier line connecting the non-dominated points
pareto_points = [
    (0.01, 22.0), # HAL Baseline
    (1.40, 68.2), # AutoAgent
    (1.85, 81.7), # Agent Q
    (2.10, 94.3)  # M3Builder
]
px, py = zip(*pareto_points)
plt.plot(px, py, linestyle='--', color='black', alpha=0.7, label='Pareto Frontier', zorder=2)

# Format the Axes (Logarithmic scale for X-axis is crucial here)
plt.xscale('log')
plt.xlabel('Inference-Time Compute Cost (USD, Log Scale)', fontsize=10)
plt.ylabel('Task Success Rate (SR%)', fontsize=10)
plt.title('Agentic ROI: Cost vs. Accuracy Pareto Frontier', fontsize=12, pad=15)

# Add gridlines and the Legend
plt.grid(True, which="both", ls="-", alpha=0.2)
plt.legend(loc='lower right', fontsize=8)

# Adjust layout to prevent clipping and save the image
plt.tight_layout()
plt.savefig('pareto_frontier_chart.png', dpi=600, bbox_inches='tight')
# ---------------------------------------------------------
# CHART 5: FAILURE MODE DISTRIBUTION (PIE CHART)
# ---------------------------------------------------------
# Based on the Taxonomy in Exploring Autonomous Agents & AgenTracer
failure_labels = ['Planning Errors', 'Tool/API Misuse', 'Hallucinated Success', 'Benchmark Hacking']
failure_sizes = [42, 31, 20, 7] # Percentages from failure mode metadata
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']

plt.figure(figsize=(8, 8))
plt.pie(failure_sizes, labels=failure_labels, autopct='%1.1f%%', startangle=140, colors=colors, explode=(0.05, 0, 0, 0))
plt.title('Figure 5: Taxonomy of Autonomous Agent Failures')
plt.tight_layout()
plt.savefig('failure_modes.png', dpi=300)

# --- FIGURE 6: FAILURE SCHEMATIC ---
# (Simple box representation logic for the schematic)
fig, ax = plt.subplots(figsize=(8, 5))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')

# Draw Boxes
def draw_box(x, y, text, color='#E0F7FA'):
    ax.add_patch(plt.Rectangle((x, y), 2.5, 1, facecolor=color, edgecolor='black'))
    ax.text(x+1.25, y+0.5, text, ha='center', va='center', fontsize=10, fontweight='bold')

draw_box(1, 4, "LLM Planner\n(Input)", '#BBDEFB')
draw_box(4, 4, "Action\n(Tool Use)", '#C8E6C9')
draw_box(7, 4, "Environment\n(Observation)", '#FFE0B2')
draw_box(4, 1, "Failure State:\nDeterministic Loop", '#FFCDD2')

# Draw Arrows
ax.annotate("", xy=(4, 4.5), xytext=(3.5, 4.5), arrowprops=dict(arrowstyle="->", lw=1.5))
ax.annotate("", xy=(7, 4.5), xytext=(6.5, 4.5), arrowprops=dict(arrowstyle="->", lw=1.5))
# Feedback Loop (The "Infinite Loop")
ax.annotate("", xy=(2.25, 4), xytext=(8.25, 4), arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=-0.4", lw=1.5, color='red'))
ax.text(5.4, 3, "Identical Observation\n(Loop Trigger)", ha='center', color='darkblue', fontsize=9, fontweight='bold')
# Failure Drop
ax.annotate("", xy=(5.25, 2), xytext=(5.25, 4), arrowprops=dict(arrowstyle="->", lw=1.5, linestyle="--"))

plt.title('Fig. 6. State-Transition of "Deterministic Looping" Failure Mode', fontsize=12)
plt.tight_layout()
plt.savefig('Fig7_FailureSchematic.png', dpi=300)
plt.show()
