class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:

        arr1 = sentence1.split(" ")
        arr2 = sentence2.split(" ")

        prefix = 0

        while prefix < len(arr1) and prefix < len(arr2) \
                and arr1[prefix] == arr2[prefix]:
            prefix += 1

        suffix = 0

        while suffix < len(arr1) and suffix < len(arr2) \
                and arr1[len(arr1) - 1 - suffix] == arr2[len(arr2) - 1 - suffix]:
            suffix += 1

        return prefix + suffix >= min(len(arr1), len(arr2))