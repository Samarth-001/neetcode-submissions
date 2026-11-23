class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()

        output = []
        search = ""

        for ch in searchWord:
            search += ch

            l, r = 0, len(products) - 1

            while l <= r:
                mid = l + (r - l) // 2

                if products[mid] >= search:
                    r = mid - 1
                else:
                    l = mid + 1

            suggestions = []

            # Start from the first possible matching product
            while l < len(products) and len(suggestions) < 3:
                if products[l].startswith(search):
                    suggestions.append(products[l])
                    l += 1
                else:
                    break

            output.append(suggestions)

        return output