import urllib.request
class Node :
    def __init__(self,word : str) :
        self.word = word
        self.left = None
        self.right = None
class BST:
    def __init__(self, source: str, **kwargs):
        self.root = None

        is_url = kwargs.get("url", False)
        is_file = kwargs.get("file", False)

        if is_url and is_file:
            raise ValueError("Both url and file cannot be True at the same time.")
        if not is_url and not is_file:
            raise ValueError("You must specify either url=True or file=True.")

        words = []
        if is_url:
            try:
                with urllib.request.urlopen(source) as response:
                    data = response.read().decode("utf-8")
                    words = [line.strip() for line in data.splitlines() if line.strip()]
            except Exception as e:
                raise ConnectionError(f"Failed to fetch data from URL: {e}")
        elif is_file:
            try:
                with open(source, "r", encoding="utf-8") as f:
                    words = [line.strip() for line in f if line.strip()]
            except Exception as e:
                raise FileNotFoundError(f"Failed to read file: {e}")

        def build_balanced_tree(word_list):
            if not word_list:
                return None
            mid = len(word_list) // 2
            node = Node(word_list[mid])
            node.left = build_balanced_tree(word_list[:mid])
            node.right = build_balanced_tree(word_list[mid+1:])
            return node

        self.root = build_balanced_tree(words)


    def autocomplete(self, prefix: str):
        results = []
        self._collect(self.root, prefix.lower(), results)
        return results
    
    def _collect(self, node:Node, prefix : str, results):
        if node is None:
            return
        #in order -> left node right
        self._collect(node.left, prefix, results)

        if node.word.lower().startswith(prefix):
            results.append(node.word)

        self._collect(node.right, prefix, results)
