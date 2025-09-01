class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        import heapq

        def gain(p, t):
            return (p + 1) / (t + 1) - (p / t)

        # Crio o heap com o ganho inicial de cada turma -- heapq é um heap minimo, por isso tenho que fazer o gain.
        heap = [(-gain(p, t), p, t) for p, t in classes]
        heapq.heapify(heap)  # transforma em heap válido

        # Enquanto tiver alunos extras
        for _ in range(extraStudents):
            g, p, t = heapq.heappop(heap)  # turma com maior ganho
            p, t = p + 1, t + 1            # adiciona 1 aluno
            heapq.heappush(heap, (-gain(p, t), p, t))

        # Calcula a média final das turmas
        total = sum(p / t for _, p, t in heap)
        return total / len(classes)

        