Analyzing the Evolution of Social Concepts Using Temporal Embedding Models 📈

🚧 Status: Code is currently unavailable / Pending reconstruction. This repository serves as a placeholder for the paper's methodology and findings. 🚧

This repository contains the overview and theoretical framework for the paper "Analyzing the Evolution of Social Concepts Using Temporal Embedding Models", presented at the 4th International Conference on New Research & Achievements in Science, Engineering & Technologies (13 July 2025).

📖 Abstract

The meanings of social concepts (e.g., freedom, identity, equality) are not fixed; they evolve in response to cultural, political, and technological changes. Traditional static word embeddings (like standard Word2Vec) fail to capture these temporal variations.

This project introduces a dynamic embedding-based framework to trace the semantic trajectories of key social concepts across multiple decades. By training time-aware embeddings on temporally segmented text corpora, we can visualize and quantify changes in meaning over time.

⚙️ Methodology

The proposed framework calculates the evolution of concepts in three main steps:

Dynamic Embedding Training: The text corpus is divided into multiple time windows. For each time period, we learn word representations that capture their contextual meanings specific to that era.

Semantic Shift Calculation: We measure how much a concept's meaning has changed between two consecutive time periods by calculating the distance between their aligned vectors.

Concept Relationship Measurement: To track how different social concepts relate to one another over time, we compute the similarity between their embeddings within the same time window.

🔗 Read the Full Paper: For the complete mathematical framework, equations, and detailed methodology, please read the full paper here: https://bit.ly/4BOeBEX

📊 Key Findings

The simulation analyzed concepts like freedom, justice, and democracy across three distinct time windows: 2000-2010, 2010-2020, and 2020-2025.

Significant Semantic Drift: The largest semantic shift occurred for the concept of freedom between the first and second time windows, showing rapid evolution in its societal meaning.

Stable yet Evolving Relationships: While the core relationships between freedom, justice, and democracy remained strong, there was a subtle, gradual decline in their similarity over time, indicating nuanced divergence in how these concepts interact in modern discourse.

📝 Citation

@inproceedings{rabinataj2025socialconcepts,
  title={Analyzing the Evolution of Social Concepts Using Temporal Embedding Models},
  author={Rabinataj, Seyedeh Samira},
  booktitle={4th International Conference on New Research \& Achievements in Science, Engineering \& Technologies},
  year={2025},
  month={July},
  organization={University of Turin}
}
