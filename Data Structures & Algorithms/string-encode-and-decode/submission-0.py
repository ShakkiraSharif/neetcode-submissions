class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = []
        for s in strs:
            enc.append(str(len(s)))
            enc.append("#")
            enc.append(s)
        return "".join(enc)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            length = ""

            while s[i] != "#":
                length += s[i]
                i += 1

            length = int(length)
            i += 1  # Skip the '#'

            result.append(s[i:i + length])

            i = i + length

        return result