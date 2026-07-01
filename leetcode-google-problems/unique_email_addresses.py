class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        sent = set()

        for email in emails:

            mid = -1
            processed = ""
            for i in range(len(email)):
                if email[i] == "@":
                    mid = i
                    break
                elif email[i] == ".":
                    continue
                elif email[i] == "+":
                    while email[i + 1] != "@":
                        i += 1
                else:
                    processed += email[i]

            if len(processed) == 0:
                continue

            processed += email[mid:]