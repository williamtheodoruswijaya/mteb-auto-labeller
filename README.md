# Unsupervised Topic Modelling & Trend Analysis on Citizen Reports Using a Self-Supervised Learning Approach

## 📌 Project Background

In modern *Smart City* systems, thousands of citizen reports are submitted daily. These reports are currently grouped into static categories (e.g., "Road", "Tree", "Disturbance"). However, such categories are often too broad and fail to capture specific emerging issues (for example, a spike in “cable theft” cases that all fall under the generic "Disturbance" label).

This project aims to automatically discover **latent topics** without manual labels (*unsupervised*). The approach adapts concepts from **Lexical Mutations Network** and **Self-Supervised Learning** to detect clusters of semantically similar issues, even when they use different word choices.

## 🎯 Objectives

1. **Granular Topic Discovery:** Break down broad categories into more specific subtopics (e.g., *Tree* → *Fallen Tree* vs *Tree Obstructing Road*).
2. **Unsupervised Labeling:** Generate topic labels automatically through *Community Detection* algorithms.
3. **Trend Analysis:** Track how specific issues evolve over time.

## 🧠 Methodology & Theoretical Approach

The workflow converts textual reports into vector representations using **Self-Supervised Learning**, builds a semantic similarity graph, and identifies topic communities.

### Pipeline Architecture

#### 1. Data Preprocessing

Cleaning and preparing the textual content (`content` column) to reduce noise:

* **Cleaning:** Remove non-alphanumeric characters, URLs, and irrelevant symbols.
* **Filtering:** (Optional) Keep only reports with a minimum text length to ensure meaningful context.

#### 2. Text Embedding (Self-Supervised Learning Stage)

Transform the text into numerical vectors (embeddings) that represent semantic meaning.

* **Model:** `indobenchmark/indobert-base-p1`
* **Why IndoBERT?** IndoBERT is a language model trained specifically on large-scale Indonesian corpora. It is capable of understanding both formal and informal language variations, including everyday expressions commonly found in citizen reports. Through fine-tuning with a **self-supervised** learning approach (TSDAE), IndoBERT produces contextual sentence embeddings that effectively capture semantic meaning. As a result, reports describing similar issues—despite differences in wording or sentence structure—are mapped to nearby representations in the vector space, enabling semantic grouping without requiring explicit labeled data.

#### 3. Semantic Graph Construction

Build a graph representing semantic relationships between reports using a k-Nearest Neighbors (k-NN) graph.

* **Pairwise Cosine Similarity:** Compute similarity between all report embeddings:
    
  $$ \cos(\theta)=\frac{A\cdot B}{|A||B|} $$

* **k-Nearest Neighbors Selection:** For each report, identify its top-k most similar reports based on cosine similarity.
* **Graph Construction:** Create an undirected graph where `Nodes` represent individual reports, `Edges` connect each report to its k nearest neighbors, and `Edge weights` correspond to cosine similarity scores
* **Thresholding:** If similarity exceeds a chosen threshold (e.g., >0.85), connect the reports with an *edge*.
* **Output:** A semantic similarity graph that preserves local neighborhood structure and ensures each report is meaningfully connected, forming a robust basis for downstream community detection.

#### 4. Unsupervised Clustering (Community Detection)

Group tightly connected reports.

* **Algorithm:** **Louvain Algorithm**, which maximizes graph modularity to identify dense communities.
* **Intuition:** Reports with high similarity create tightly knit groups, forming **latent topic communities**.

#### 5. Topic Extraction & Labeling

Convert numerical clusters into readable topic labels.

* Extract dominant keywords using **TF-IDF** or **Class-based TF-IDF (c-TF-IDF)**.
* Use these keywords to generate topic labels (e.g., Cluster 0 → keywords “lamp, off, dark, pju” → Topic: *Street Light Outage*).

## 🛠️ Technologies & Tools

* **Python 3.10+**
* **Sentence-Transformers** (E5 / IndoBERT for embeddings)
* **NetworkX / python-louvain** for graph building & community detection
* **Pandas & NumPy** for data manipulation
* **Scikit-Learn** for cosine similarity & TF-IDF
* **Matplotlib / Seaborn** for visualization

## 📂 Dataset Structure

The dataset consists of citizen complaint records (CRM) with key fields:

* `id` — unique report ID
* `content` — textual description (main input)
* `category` — initial coarse category (baseline)
* `created_at` — timestamp for trend analysis
* `latitude` & `longitude` — event location

## ▶️ How to Run the Notebook

Follow these steps to reproduce the experiments and results in this project:

### 1. Clone the repository
```bash
git clone https://github.com/williamtheodoruswijaya/mteb-auto-labeller.git
cd mteb-auto-labeller
```

### 2. Install required dependencies
```bash
pip install -r requirements.txt
```

### Run the notebook
```bash
jupyter notebook
```

Or type `code .` in the terminal to open the notebook in Visual Studio Code
The notebook file is located at `./workflow/mteb_autolabeller_V2.ipynb`
The output files are located at `./workflow/output` folder
