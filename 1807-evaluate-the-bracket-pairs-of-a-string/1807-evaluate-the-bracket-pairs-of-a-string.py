import re
class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        knowledge = dict(knowledge)
        def replace_word(match):
            word =match.group(1)
            return knowledge.get(word, "?")
        result = re.sub(r'\((.*?)\)',replace_word,s)
        return result
