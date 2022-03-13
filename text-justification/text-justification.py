class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        q = deque()
        n_acc = 0
        def check_length(acc:int, curr: int, cnt: int):
            remain = maxWidth - acc - curr
            if remain >= cnt:
                return True
            else:
                return False
    
        def make_sentence(acc: int):
            if len(q) > 1:
                s, r = divmod(maxWidth - acc, len(q) - 1)
            else:
                return q.popleft() + " " * (maxWidth - acc)
            out = ""
            while q:
                w = q.popleft()
                if r:
                    out += w + " " * (s + 1)
                    r -= 1
                elif q:
                    out += w + " " * (s)
                else:
                    out += w
            return out
        sentences = []

        for word in words:
            if q and not check_length(n_acc, len(word), len(q)):
                sentences.append(make_sentence(n_acc))
                n_acc = 0
            q.append(word)
            n_acc += len(word)
        
        if q:
            sentences.append(" ".join(q) + " " * (maxWidth - len(q) - n_acc + 1))
        
        return sentences

                

            

