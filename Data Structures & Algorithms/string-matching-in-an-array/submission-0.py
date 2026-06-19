class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        
        result = []

        for index in range(len(words)):

            for word in words:
                if words[index] == word:
                    continue

                if words[index] in word:
                    result.append(words[index])

        return list(set(result))