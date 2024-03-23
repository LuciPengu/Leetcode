class Trie:
    def __init__(self):
        self.childs = {}
        self.cnt = 0

class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.map = {k:v for k, v in zip(keys, values)}
        self.root = Trie()
        def insert(word):
            if not word: return
            cur = self.root
            for ch in word:
                if ch not in cur.childs: cur.childs[ch] = Trie()
                cur = cur.childs[ch]
            cur.cnt += 1

        for word in dictionary:
            insert(self.encrypt(word))

    def encrypt(self, word1: str) -> str:
        string = []
        for ch in word1:
            if ch not in self.map: return ''
            string.append(self.map[ch])
        return ''.join(string)
        
    def decrypt(self, word2: str) -> int:
        cur = self.root
        for idx, ch in enumerate(word2):
            if ch not in cur.childs: return 0
            cur = cur.childs[ch]
        return cur.cnt
