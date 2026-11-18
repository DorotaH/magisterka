class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        pointers = dict()
        status = dict()
        max_len = 0
        for num in nums:
            if num in pointers:
                continue
            is_begin = (num + 1) in pointers and status[num + 1] in ["begin", "single"]
            is_end = (num - 1) in pointers and status[num - 1] in ["single", "end"]
            if is_begin and not is_end:
                li = pointers[num + 1]
                max_len = max(max_len, len(li) + 1)
                li.insert(0, num)
                pointers[num] = li
                status[num] = "begin"
                status[num + 1] = "end" if status[num + 1] == "single" else "middle"
            elif not is_begin and is_end:
                li = pointers[num - 1]
                max_len = max(max_len, len(li) + 1)
                li.append(num)
                pointers[num] = li
                status[num] = "end"
                status[num - 1] = "begin" if status[num - 1] == "single" else "middle"
            elif is_begin and is_end:
                li1 = pointers[num - 1]
                li2 = pointers[num + 1]
                max_len = max(max_len, len(li1) + len(li2) + 1)
                new_li = li1 + [num] + li2
                pointers[num] = new_li
                pointers[num - len(li1)] = new_li
                pointers[num + len(li2)] = new_li
                status[num] = "middle"
                status[num - 1] = "begin" if status[num - 1] == "single" else "middle"
                status[num + 1] = "end" if status[num + 1] == "single" else "middle"
            else:
                max_len = max(max_len, 1)
                pointers[num] = [num]
                status[num] = "single"
        return max_len
