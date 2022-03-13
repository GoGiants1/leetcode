class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        # candidates = []
        # cnt = Counter(words)
        # curr_cnt = defaultdict(int)
        # w_sz = len(words[0])
        # wdw_sz = len(words) * w_sz
        # for i in range(len(s) - w_sz + 1):
        #     if s[i:i+w_sz] in cnt:
        #         candidates.append(i)

        # out = []
        # for start in candidates:
        #     while q:
        #         _, prev = q.popleft()
        #         cnt[prev] += 1
        #     for end in range(start, start + wdw_sz, w_sz):
        #         wd = s[end:end+w_sz]
        #         if wd in cnt and cnt[wd] > 0:
        #             q.append((end, wd))
        #             cnt[wd] -= 1
        #         else:
        #             while q:
        #                 _, prev = q.popleft()
        #                 cnt[prev] += 1
        #             break
        #     if len(q) == len(words):
        #         out.append(start)
        # return out

        ans = []
        s_size = len(s)
        word_len = len(words[0])
        word_count = collections.Counter(words)

        def sliding_window(left):
            found_count = collections.defaultdict(lambda: 0)
            total_matched = 0

            for right in range(left, len(s), word_len):
                if right + word_len > s_size:
                    break
                
                new_word = s[right: right + word_len]
                if new_word not in word_count:
                    found_count = collections.defaultdict(lambda: 0)
                    total_matched = 0
                    left = right + word_len
                else:
                    found_count[new_word] += 1
                    if found_count[new_word] > word_count[new_word]:
                        while found_count[new_word] > word_count[new_word]:
                            left_most = s[left: left + word_len]
                            found_count[left_most] -= 1
                            left += word_len
                            if left_most != new_word:
                                total_matched -= 1
                    else:
                        total_matched += 1

                if total_matched == len(words):
                    ans.append(left)

        for i in range(word_len):
            sliding_window(i)

        return ans

