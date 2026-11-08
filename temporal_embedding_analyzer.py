import numpy as np
from gensim.models import Word2Vec
from scipy.spatial.distance import cosine
from scipy.linalg import orthogonal_procrustes

class TemporalEmbeddingAnalyzer:
    def __init__(self, vector_size=100, window=5, min_count=1):
        self.vector_size = vector_size
        self.window = window
        self.min_count = min_count
        self.models = {}
        self.aligned_embeddings = {}

    def train_dynamic_embeddings(self, corpora_by_time):
        for time_window, sentences in corpora_by_time.items():
            print(f"Training model for time window: {time_window}...")
            model = Word2Vec(
                sentences=sentences, 
                vector_size=self.vector_size, 
                window=self.window, 
                min_count=self.min_count,
                sg=1
            )
            self.models[time_window] = model
            self.aligned_embeddings[time_window] = {word: model.wv[word] for word in model.wv.index_to_key}
            
    def align_embeddings(self, base_time, target_time):
        base_model = self.models[base_time]
        target_model = self.models[target_time]
        
        common_words = list(set(base_model.wv.index_to_key) & set(target_model.wv.index_to_key))
        
        if not common_words:
            raise ValueError("No common words found between the two time windows.")
            
        base_matrix = np.array([base_model.wv[word] for word in common_words])
        target_matrix = np.array([target_model.wv[word] for word in common_words])
        
        transformation_matrix, _ = orthogonal_procrustes(target_matrix, base_matrix)
        
        for word in target_model.wv.index_to_key:
            original_vector = target_model.wv[word]
            self.aligned_embeddings[target_time][word] = np.dot(original_vector, transformation_matrix)

    def calculate_semantic_shift(self, concept, time1, time2):
        if concept not in self.aligned_embeddings[time1] or concept not in self.aligned_embeddings[time2]:
            return None
            
        vec1 = self.aligned_embeddings[time1][concept]
        vec2 = self.aligned_embeddings[time2][concept]
        
        shift = np.linalg.norm(vec2 - vec1) 
        return shift

    def calculate_concept_relationship(self, concept1, concept2, time_window):
        if concept1 not in self.models[time_window].wv or concept2 not in self.models[time_window].wv:
            return None
            
        vec1 = self.models[time_window].wv[concept1]
        vec2 = self.models[time_window].wv[concept2]
        
        similarity = 1 - cosine(vec1, vec2)
        return similarity

if __name__ == "__main__":
    dummy_corpora = {
        "t1": [["freedom", "rights", "law"], ["justice", "equality", "law"], ["democracy", "voting", "rights"], ["freedom", "justice", "democracy"]],
        "t2": [["freedom", "market", "economy"], ["justice", "social", "movement"], ["democracy", "internet", "voting"], ["freedom", "equality", "market"]],
        "t3": [["freedom", "data", "privacy"], ["justice", "climate", "action"], ["democracy", "algorithm", "bias"], ["freedom", "justice", "privacy"]]
    }
    
    analyzer = TemporalEmbeddingAnalyzer(vector_size=10, window=2, min_count=1)
    
    analyzer.train_dynamic_embeddings(dummy_corpora)
    
    analyzer.align_embeddings(base_time="t1", target_time="t2")
    analyzer.align_embeddings(base_time="t2", target_time="t3")
    
    print("\n--- Semantic Shifts ---")
    concepts_to_track = ["freedom", "justice", "democracy"]
    for concept in concepts_to_track:
        shift_t1_t2 = analyzer.calculate_semantic_shift(concept, "t1", "t2")
        shift_t2_t3 = analyzer.calculate_semantic_shift(concept, "t2", "t3")
        print(f"Shift for '{concept}' (t1 -> t2): {shift_t1_t2:.4f}")
        print(f"Shift for '{concept}' (t2 -> t3): {shift_t2_t3:.4f}")
        
    print("\n--- Concept Relationships (Cosine Similarity) ---")
    pairs = [("freedom", "justice"), ("freedom", "democracy"), ("justice", "democracy")]
    for t in ["t1", "t2", "t3"]:
        print(f"\nTime Window: {t}")
        for c1, c2 in pairs:
            sim = analyzer.calculate_concept_relationship(c1, c2, t)
            print(f"Similarity ({c1}, {c2}): {sim:.4f}")
