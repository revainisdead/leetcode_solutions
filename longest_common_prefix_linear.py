class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Goal here is to try and solve the problem in linear time.

        The main idea is to find the shortest word, and just guess
        that it is the longest common prefix, and if not, keep
        chopping off the last character in the word.
        """
        shortest_i
        shortest = strs[0]

        for i, s in enumerate(strs):
            if len(s) < len(shortest):
                shortest_i = i
                shortest = s

        # small optimization: take shortest word out of the list first
        new_strs = strs[:shortest_i] + strs[shortest_i + 1:]

        while True:
            passes = []
            for word in new_strs:
                passes.append(word.startswith(shortest))

                #if word.startswith(shortest):
                    #passes.append(True)
                #else:
                    #passes.append(False)

            if all(passes):
                return shortest

            # chop off last character
            shortest = shortest[:len(shortest) - 1]
                
