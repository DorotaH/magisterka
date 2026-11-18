class Solution:
    def __init__(self):

        self.p_groups = list()
        self.p_wildcards = list()
        self.p_dict_wc = dict()
        self.p_wc_index = set()
        self.p_closest_match = 0

    def isMatch(self, s: str, p: str) -> bool:

        l_group_count, l_substring = 0, ""
        l_prev_wc = ""

        for i, j in enumerate(p, 0):
            if 1 + i < len(p) and p[1 + i] == "*":
                if l_substring:
                    self.p_groups.append(l_substring)
                    l_substring = ""
                    l_group_count += 1
                    l_prev_wc = ""

                if l_prev_wc != p[i]:
                    self.p_groups.append("")
                    self.p_wildcards.append([l_group_count, p[i]])
                    l_group_count += 1
                    l_prev_wc = p[i]

            elif p[i] != "*":
                l_substring += p[i]
        if l_substring:
            self.p_groups.append(l_substring)

        # quick wins
        if len("".join(self.p_groups)) > len(s):
            return False
        elif not self.p_wildcards and len("".join(self.p_groups)) != len(s):
            return False
        elif not self.p_wildcards:
            return self.checkSubstring("".join(self.p_groups), s)

        if self.p_groups[0]:  # First group is not wildcard
            if not self.checkSubstring(self.p_groups[0], s[0 : len(self.p_groups[0])]):
                return False
            else:
                s = s[len(self.p_groups[0]) :]
                self.p_groups.pop(0)
                for x in self.p_wildcards:
                    x[0] -= 1

        if self.p_groups[-1]:  # Lastgroup is not wildcard
            if not self.checkSubstring(self.p_groups[-1], s[-len(self.p_groups[-1]) :]):
                return False
            else:
                s = s[: -len(self.p_groups[-1])]
                self.p_groups.pop(-1)

        for x in self.p_wildcards:
            self.p_dict_wc[x[0]] = x[1]
            self.p_wc_index.add(x[0])

        return self.recursiveCheck(len(s) - len("".join(self.p_groups)), 0, s)

    def recursiveCheck(self, i_remaining, i_level: int, s: str) -> bool:

        if i_level not in self.p_wc_index:  # non-wild card group
            l_substring = ""
            for i, j in enumerate(self.p_groups, 0):
                if i <= i_level:
                    l_substring += j
                else:
                    break

            if not self.checkSubstring(l_substring, s[0 : len(l_substring)]):
                return False
            else:
                return self.recursiveCheck(i_remaining, i_level + 1, s)

        elif i_level == len(self.p_groups) - 1:  # last level
            self.p_groups[i_level] = (
                self.p_dict_wc[i_level] * i_remaining
            )  # fill all remaining space with WC symbol

            l_substring = "".join(x for x in self.p_groups)

            return self.checkSubstring(l_substring, s)

        else:
            self.p_groups[i_level] = ""

            for l_slot in range(0, i_remaining + 1):
                if self.recursiveCheck(
                    i_remaining - len(self.p_groups[i_level]), i_level + 1, s
                ):
                    return True
                if i_remaining != l_slot:
                    self.p_groups[i_level] += self.p_dict_wc[i_level]

            return False

    def checkSubstring(self, p: str, s: str) -> bool:  # expecting len(p) = len(s)

        for i, j in enumerate(p, 0):
            if j != "." and s[i] != j:
                # if i > self.p_closest_match:
                # self.p_closest_match = i
                # print(f'New closest match ({i}):  {p} - {s}')
                return False
        return True
