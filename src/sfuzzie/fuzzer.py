from typing import List,  Type


class Entry:
    
    def __init__(self, char: str):
        self.char = char
        self.entries = {}
        self.end = False

    def list_words(self, prefix='') -> List[str]:
        """list all possibilities from current entry"""
        suggestions = []

        for entry in self.entries.values():
            entry_prefix = f"{prefix}{entry.char}"

            if entry.end:
                suggestions.append(entry_prefix)
            suggestions.extend(entry.list_words(entry_prefix))
        return suggestions


class Fuzzer:
    
    def __init__(self):
        self.entries = {}

    def add(self, line: str) -> None:
        """
        add a line to the Fuzzer, each word in the line is a seperate enty
        so: hello world
        
        will create 2 entries, 1 for hello and one for world, this helps reduce the depth
        of the fuzzer, and make more enteries
        """
        for word in line.split():
            wlen = len(word) - 1
            entry = self
            
            for i, c in enumerate(word):
                if c not in entry.entries:
                    entry.entries[c] = Entry(c)
                entry = entry.entries[c]

                if i == wlen:
                    entry.end = True
    
    def suggest(self, fuzz_line: str) -> List[List[str]]:
        """
        returns a list of suggestions for each word find in the given string
        """
        fuzz_words = fuzz_line.split()
        suggestions = []

        for i, fuzz_word in enumerate(fuzz_words):
            entry = self
            record = ''

            if i <= len(suggestions):
                suggestions.append([])

            for c in fuzz_word:
                if c not in entry.entries:
                    break
                
                entry  = entry.entries[c]
                record = record + c

                if entry.end:
                    suggestions[i].append(record)
            suggestions[i].extend(entry.list_words(prefix=record))
        return suggestions


def fuzz(words: List[str]) -> Type[Fuzzer]:
    fuzzer = Fuzzer()

    for w in words:
        fuzzer.add(w)
    return fuzzer

