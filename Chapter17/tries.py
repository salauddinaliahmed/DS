# Trying out Trie data structure.

class TrieNode:
    """Just has a single attribute for children."""
    def __init__(self) -> None:
        self.children = {}


class Trie:
    def __init__(self) -> None:
        """Creates an empty TrieNode and saves it as root."""
        self.root = TrieNode()
    
    def __str__(self):
        return f'Roots children: {self.root.children.keys()}'

    def search(self, word):
        """We iterate through the word and check for each character in the trie
            each character is a key with the value as another trie node with the next set of characters.
            level 1 c
            level 2 a 
            level 3 t 
        """
        pass
    
    def insert(self, word):
        current_node = self.root
        for each_letter in word:
            if n := current_node.children.get(each_letter, False):
                current_node = n
            else:
                current_node.children[each_letter] = current_node =  TrieNode()
        
        current_node.children['*'] = None

    def collect_all_words(self, node=None, word="", words_list=[]):
        if not node:
            node = self.root.children

        for each_key, obj in node.items():
            if each_key == "*":
                words_list.append(word)
            else:
                self.collect_all_words(obj.children, word=word+each_key, words_list=words_list)
    
        """Should print a list of all the words in the trie or words starting from the supplied node."""
        return words_list


if __name__ == '__main__':
    tr = Trie()
    tr.insert('cat')
    tr.insert('bat')
    print(tr)
    print(tr.collect_all_words())