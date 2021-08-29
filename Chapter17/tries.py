# Trying out Trie data structure.

class TrieNode:
    """Just has a single attribute for children."""
    def __init__(self) -> None:
        self.children = {}


class Trie:
    def __init__(self) -> None:
        """Creates an empty TrieNode and saves it as root."""
        self.root = TrieNode()
    

