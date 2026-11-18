from collections import Counter


class DataStatistics:
    def mean(self, data):
        return round(sum(data) / len(data), 2)

    def median(self, data):
        sorted_data = sorted(data)
        n = len(sorted_data)
        middle = n // 2
        if n % 2 == 0:
            return round((sorted_data[middle - 1] + sorted_data[middle]) / 2, 2)
        else:
            return sorted_data[middle]

    def mode(self, data):
        counter = Counter(data)
        mode_count = max(counter.values())
        return [x for x, count in counter.items() if count == mode_count]