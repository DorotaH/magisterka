class PageUtil:
    def __init__(self, data, page_size):
        self.data = data
        self.page_size = page_size
        self.total_items = len(data)
        self.total_pages = (page_size + self.total_items - 1) // page_size

    def get_page(self, page_number):
        if 1 > page_number or self.total_pages < page_number:
            return []

        start_index = self.page_size * (page_number - 1)
        end_index = self.page_size + start_index
        return self.data[start_index:end_index]

    def get_page_info(self, page_number):
        if 1 > page_number or self.total_pages < page_number:
            return {}

        start_index = self.page_size * (page_number - 1)
        end_index = min(self.page_size + start_index, self.total_items)
        page_data = self.data[start_index:end_index]

        return {
            "current_page": page_number,
            "per_page": self.page_size,
            "total_pages": self.total_pages,
            "total_items": self.total_items,
            "has_previous": 1 < page_number,
            "has_next": self.total_pages > page_number,
            "data": page_data,
        }

    def search(self, keyword):
        results = [item for item in self.data if keyword in str(item)]
        num_results = len(results)
        num_pages = (self.page_size + num_results - 1) // self.page_size

        return {
            "keyword": keyword,
            "total_results": num_results,
            "total_pages": num_pages,
            "results": results,
        }