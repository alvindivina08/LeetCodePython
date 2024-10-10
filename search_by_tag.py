class SearchByTag:

    def __init__(self, data, query_tag):
        self._data = data
        self.query = query_tag
    
    def search(self):
        if 'items' in self._data:
            for item in self._data['items']:
                if 'tags' in item and self.query in item['tags']:
                    yield item

    def first(self):
        first_item = next(self.search(), None)

        if first_item is None:
            raise StopIteration("No items found.")

        return first_item


jsonData = {
    "items" : [
    {"name": "The Godfather", "tags": ["70s", "drama", "crime"]},
    {"name": "The Dark Knight", "tags": ["action", "drama", "crime"]},
    {"name": "The Godfather: Part II", "tags": ["70s", "drama", "crime"]},
    ]
}


searchByTag = SearchByTag(jsonData, "drama")

for result in searchByTag.search():
    print(result)