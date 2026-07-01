class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper()

        chunks = []

        for i in range(len(s), 0, -k):
            chunks.append(s[max(0, i - k): i])

        return "-".join(chunks[::-1])
