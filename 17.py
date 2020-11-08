class Trie:
    def __init__(self):
        self.root = {"*": "*"}

    def insert(self, word: str) -> None:
        curr_node = self.root
        for letter in word:
            if letter not in curr_node:
                curr_node[letter] = {}
            curr_node = curr_node[letter]
        curr_node["*"] = "*"

    def search(self, word: str) -> bool:
        curr_node = self.root
        for letter in word:
            if letter not in curr_node:
                return False
            else:
                curr_node = curr_node[letter]
        return "*" in curr_node

    def startsWith(self, prefix: str) -> bool:
        curr_node = self.root
        for letter in prefix:
            if letter not in curr_node:
                return False
            else:
                curr_node = curr_node[letter]
        return True

    def __str__(self):
        return "{}".format(self.root)


"""
「時間/空間複雜度？」
(插入：O(N)/空間全新的話O(N)
搜尋：O(N)/O(1)
前綴：O(N)/O(1)
當中N代表字串長。)
「如果要支援刪除呢？」
(要實作刪除函式時，不是使用TrieNode的話，
就要留意去處理自己製造的結束標記。
一般使用TrieNode很簡單，使用search找到該字，
並將isWord設成false/False即可。
記得詢問找不到該字要怎麼回傳。)
"""

# Using TrieNode

# class TrieNode:
#     def __init__(self, letter):
#         self.letter = letter
#         self.children = {}
#         self.is_end_of_word = False
#
#
# class Trie:
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.root = TrieNode("*")
#
#     def insert(self, word: str) -> None:
#         """
#         Inserts a word into the trie.
#         """
#         curr_node = self.root
#         for letter in word:
#             if letter not in curr_node.children:
#                 curr_node.children[letter] = TrieNode(letter)
#             curr_node = curr_node.children[letter]
#         curr_node.is_end_of_word = True
#
#     def search(self, word: str) -> bool:
#         """
#         Returns if the word is in the trie.
#         """
#         if word == "":
#             return True
#         curr_node = self.root
#         for letter in word:
#             if letter not in curr_node.children:
#                 return False
#             curr_node = curr_node.children[letter]
#         return curr_node.is_end_of_word
#
#     def startsWith(self, prefix: str) -> bool:
#         """
#         Returns if there is any word in the trie that starts with the given prefix.
#         """
#         curr_node = self.root
#         for letter in prefix:
#             if letter not in curr_node.children:
#                 return False
#             else:
#                 curr_node = curr_node.children[letter]
#         return True


trie = Trie()
words = ["wait", "waiter", "shop", "shopper"]
for word in words:
    trie.insert(word)

# print(trie.search("wait"))
# print(trie.search(""))
# print(trie.search("waiters"))
print(trie.search("w"))
# print(trie.startsWith("ab"))


# https://www.youtube.com/watch?v=hjUJFjcrbR4
# https://desolve.medium.com/%E5%BE%9Eleetcode%E5%AD%B8%E6%BC%94%E7%AE%97%E6%B3%95-73-trie-2-827573a72653
# https://towardsdatascience.com/implementing-a-trie-data-structure-in-python-in-less-than-100-lines-of-code-a877ea23c1a1
# https://www.youtube.com/watch?v=myuSbEHFLBA