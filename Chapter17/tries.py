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
        current_node = self.root
        for each_letter in word:
            if current_node.children.get(each_letter, False):
                current_node = current_node.children[each_letter]
            else:
                return None
        return current_node.children

    @staticmethod
    def calculate_popularity(word):
        return len(word)

    
    def insert(self, word):
        current_node = self.root
        for each_letter in word:
            if n := current_node.children.get(each_letter, False):
                current_node = n
            else:
                current_node.children[each_letter] = current_node =  TrieNode()
        current_node.children['*'] = Trie.calculate_popularity(word)

    def most_common_words(foo):
        def _inner(self, *args, **kwargs):
            word_tup_list = foo(self, *args, **kwargs)
            sorted_words = sorted(word_tup_list)            

            return [_[-1] for _ in sorted_words]

        return _inner

    @most_common_words
    def collect_all_words(self, node=None, word="", words_list=[]):
        if not node:
            node = self.root.children

        for each_key, obj in node.items():
            if each_key == "*":
                # Updates popularity along with word.
                words_list.append((obj, word))
            else:
                self.collect_all_words(obj.children, word=word+each_key, words_list=words_list)
    
        """Should print a list of all the words in the trie or words starting from the supplied node."""

        return words_list

    def autocomplete(self, prefix):
        current_node = self.search(prefix)
        if not current_node:
            return None
        return self.collect_all_words(current_node)

if __name__ == '__main__':
    tr = Trie()
    tr.insert('cat')
    tr.insert('call')
    tr.insert('captain')
    tr.insert('battle')
    print(tr)
    print(tr.autocomplete('ca'))