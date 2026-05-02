# Problem: Group Anagrams Together
# Group similar words together in a UI (e.g., tags: ["bat", "tab", "cat", "act"]).

# Output: [["bat", "tab"], ["cat", "act"]]

from collections import defaultdict

def group_anagrams_together(words: list) -> list:
    grouped_anagram = defaultdict(list)

    for word in words:
        sorted_word = ''.join(sorted(word))
        grouped_anagram[sorted_word].append(word)
    
    return list(grouped_anagram.values())


words = ["bat", "tab", "cat", "act"]
print("Input -> ", words)
print("Output -> ", group_anagrams_together(words)) # output: [["bat", "tab"], ["cat", "act"]]]

words = ["bat", "tab", "cat", "act", "atb", "tca"]
print("Input -> ", words)
print("Output -> ", group_anagrams_together(words)) # output: [['bat', 'tab', 'atb'], ['cat', 'act', 'tca']]

words = ["sas"]
print("Input -> ", words)
print("Output -> ", group_anagrams_together(words)) # output: [['sas']]

words = []
print("Input -> ", words)
print("Output -> ", group_anagrams_together(words)) # output: []