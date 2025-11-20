# Unsupervised Topic Modelling & Trend Analysis on Citizen Reports Using a Self-Supervised Learning Approach

## 📌 Project Background

In modern *Smart City* systems, thousands of citizen reports are submitted daily. These reports are currently grouped into static categories (e.g., “Road”, “Tree”, “Disturbance”). However, such categories are often too broad and fail to capture specific emerging issues (for example, a spike in “cable theft” cases that all fall under the generic “Disturbance” label).

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

* **Model:** `intfloat/multilingual-e5-base`
* **Why SSL?** The E5 model is trained using *weakly-supervised contrastive pre-training* on billions of text pairs. It understands that phrases like “jalan bolong” and “damaged asphalt” express similar meaning without explicit labels.

#### 3. Semantic Graph Construction

Build a graph representing semantic relationships between reports.

* **Pairwise Cosine Similarity:** Compute similarity between all report embeddings:
  [
  \cos(\theta)=\frac{A\cdot B}{|A||B|}
  ]
* **Thresholding:** If similarity exceeds a chosen threshold (e.g., >0.85), connect the reports with an *edge*.
* **Output:** A graph where **nodes** = individual reports and **edges** = semantic similarity connections.

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
