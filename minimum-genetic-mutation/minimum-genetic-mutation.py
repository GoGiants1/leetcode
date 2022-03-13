class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        b = set(bank)
        if endGene not in b or len(b) == 0:
           return -1

        q = deque()
        q.append((startGene, 0))
        seen = {startGene}
        while q:
            gene_str, mutations = q.popleft()

            if gene_str == endGene:
                return mutations

            for c in "ACGT":
                for i in range(len(gene_str)):
                    after_mut = gene_str[:i] + c + gene_str[i + 1:]
                    if after_mut not in seen and after_mut in b:
                        q.append((after_mut, mutations + 1))
                        seen.add(after_mut)
            
        return -1


         