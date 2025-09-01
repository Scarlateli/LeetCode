class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        import heapq

        def gain(p, t):
            return (p + 1) / (t + 1) - p / t

        # Criar heap (max-heap usando ganho negativo)
        heap = [(-gain(p, t), p, t) for p, t in classes]
        heapq.heapify(heap)

        # Distribuir alunos extras
        for _ in range(extraStudents):
            g, p, t = heapq.heappop(heap)  # turma com maior ganho
            p, t = p + 1, t + 1            # adiciona 1 aluno
            heapq.heappush(heap, (-gain(p, t), p, t))

        # Calcular média final
        return sum(p / t for _, p, t in heap) / len(classes)

        