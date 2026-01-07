# a trie / prefix tree is a tree data structure used to store and retrive
# keys in a dataset of strings
#
# Trie class
#
# Trie() is the constructor, intitializes the object
# insert: inserts the string word into the trie
# search: returns true if the string word is in the trie
# startsWith: returns treu if theres is a previously isnerted strting word
# that has the prefix prefix, false otherwise
#
#
#
# prefix is a tree, where you nodes, and then the edges represent
# the values
#
# so I have some root node, and its children
# then I also have some flag to indicate whether this is the end of a word
#
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.word = True
    def search(self, word: str) -> bool:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return curr.word
    def startsWith(self, prefix:str) -> bool:
        curr = self.root
        for ch in prefix:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return True

def main():
    trie = Trie()
    trie.insert("apple")
    found_apple = trie.search("apple")
    print(found_apple)

    found_banana = trie.search("banana")
    print(found_banana)
    
    pref = trie.startsWith("app")
    print(pref)


    # None, True, "True", False, "False", True

if __name__ == "__main__":
    main()
