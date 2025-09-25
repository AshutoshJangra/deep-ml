import math
def k_means_clustering(points: list[tuple[float, float]], k: int, initial_centroids: list[tuple[float, float]], max_iterations: int) -> list[tuple[float, float]]:
	# Your code here
    def e_distance(p , c):
        #zip(p , c) -> for pairs a,b from two points - (1,2)(3,4) -> (1,3)(2,4)
        # (1,3) are a.b -> so sub for distnace and square -> a-b ** 2 for all a,b
        # sqrt
        return math.sqrt(sum((a-b)**2 for a,b in zip(p,c)))

    def mean_cluster(cluster):
        if not cluster:  # Avoid division by zero
            return None
        dim = len(cluster[0])
        return tuple(sum(p[i] for p in cluster) / len(cluster) for i in range(dim))


    centroids = initial_centroids[ : ] # [:] to make shallow copy not to point directly
    for _ in range(max_iterations):
        clusters = [[] for _ in range(k)]
        for p in points:
            # calculate distance - euclidean distance - pythagorus
            distances = [e_distance(p,c) for c in centroids]
  