# Trying out Trie data structure.

class TrieNode:
    """Just has a single attribute for children."""
    def __init__(self) -> None:
        self.children = {}


class Trie:
    def __init__(self) -> None:
        """Creates an empty TrieNode and saves it as root."""
        self.root = TrieNode()
    
    def search(self, word):
        """We iterate through the word and check for each character in the trie
            each character is a key with the value as another trie node with the next set of characters.
            level 1 c
            level 2 a 
            level 3 t 
        """
        pass
    

