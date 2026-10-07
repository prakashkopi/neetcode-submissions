class TrieNode:
    def __init__(self):
        # dict mapping chars(strings) to their respective child TrieNodes
        # Example: {'a': TrieNode, 'b': TrieNode}
        self.children = {}

        # flag to indicate whether a complete word ends at this node
        self.endOfWord = False

class PrefixTree:
    def __init__(self):
        # all prefix tree start with empty root node that acts as entry point
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # Start at the top (root) of the tree
        curr = self.root
        
        # Process each character in the word one by one
        for c in word:
            # If the character path doesn't exist yet, create a new node for it
            if c not in curr.children:
                curr.children[c] = TrieNode()
            # Move our pointer down to the child node corresponding to this character
            curr = curr.children[c]
            
        # Once the loop finishes, we are at the last character's node.
        # Mark this node to show a full word ends here.
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        # Start at the root node
        curr = self.root
        
        # Follow the path of the word's characters down the tree
        for c in word:
            # If any character in the word is missing from the tree, the word doesn't exist
            if c not in curr.children:
                return False
            # Move our pointer to the next character's node
            curr = curr.children[c]
            
        # We successfully matched every letter! 
        # Return True only if this node marks the actual completion of a stored word.
        return curr.endOfWord

    def startsWith(self, prefix: str) -> bool:
        # Start at the root node
        curr = self.root
        
        # Follow the path of the prefix characters down the tree
        for c in prefix:
            # If any character in the prefix is missing, no words start with this prefix
            if c not in curr.children:
                return False
            # Move our pointer to the next character's node
            curr = curr.children[c]
            
        # We matched the entire prefix successfully. 
        # We don't care if it's a full word or not, so we can immediately return True.
        return True