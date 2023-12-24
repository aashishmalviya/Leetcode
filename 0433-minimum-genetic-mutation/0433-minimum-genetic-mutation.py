#https://leetcode.com/problems/minimum-genetic-mutation/discuss/3271728/433%3A-Solution-with-step-by-step-explanation

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        
        bank_set = set(bank)

        options = ['A', 'C', 'G', 'T']


        q = deque()
        q.append(startGene)

        visited = set()
        visited.add(startGene)

        mutation_count = 0

        while q:
            qLen = len(q)

            for i in range(qLen):
                current_gene = q.popleft()

                if current_gene == endGene:
                    return mutation_count

                for j in range(8):
                    for current_option in options:
                        new_gene = current_gene[:j] + current_option + current_gene[j+1:]

                        if new_gene in bank_set and new_gene not in visited:
                            visited.add(new_gene)
                            q.append(new_gene)

            mutation_count += 1

        return -1