# Agentic-Meta-Analysis-2026
**Supplementary Materials for "The Efficacy of Autonomous AI Agents vs. Standard Large Language Models"**

This repository contains the data extraction datasets and visualization source code for the systematic meta-analysis submitted to *IEEE Transactions on Artificial Intelligence*.

## 📂 Repository Contents

### 1. `data_extraction.csv`
The normalized dataset synthesized from 25 peer-reviewed studies (2023-2026). It includes:
- **Success Rate (SR)**: Comparison between Zero-shot LLM Baselines and Agentic Frameworks.
- **Performance Delta**: The calculated percentage improvement (used in Figure 3).
- **Inference Costs**: USD cost per task execution (used in Figure 4).

### 2. `reproduce_figures.py`
The Python script used to generate the analytical figures presented in the manuscript.
- **Figure 2**: Success Rate Delta (Bar Chart).
- **Figure 3**: Forest Plot of Agentic Performance Delta (Random Effects Model).
- **Figure 4**: Accuracy-Cost Pareto Frontier.
- **Figure 5**: Taxonomy of Failure Modes (Pie Chart).
- **Figure 6**: State-Transition Schematic of "Deterministic Looping".

## 🚀 How to Reproduce Figures

To generate the high-resolution images used in the paper, ensure you have Python installed and run the following:

### Step 1: Install Dependencies
```bash
pip install matplotlib numpy seaborn pandas

###Step 2: Run the Script
python reproduce_figures.py

## 🔗 Citation
If you use this data or code in your research, please cite the original manuscript:

**Plain Text:**
> V. S. Kumar, "The Efficacy of Autonomous AI Agents vs. Standard Large Language Models: A Systematic Meta-Analysis," *IEEE Transactions on Artificial Intelligence* (Under Review), 2026.

**BibTeX:**
```bibtex
@article{kumar2026efficacy,
  title={The Efficacy of Autonomous AI Agents vs. Standard Large Language Models: A Systematic Meta-Analysis},
  author={Kumar, Vinay S.},
  journal={IEEE Transactions on Artificial Intelligence},
  year={2026},
  note={Under Review}
}
