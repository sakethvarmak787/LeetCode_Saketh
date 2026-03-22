class Solution:
    def fullJustify(self, words, maxWidth):
        res = []
        i = 0

        while i < len(words):
            line = []
            length = 0

            # Step 1: pack words
            while i < len(words) and length + len(words[i]) + len(line) <= maxWidth:
                line.append(words[i])
                length += len(words[i])
                i += 1

            # Step 2: calculate spaces
            spaces = maxWidth - length
            gaps = len(line) - 1

            # Case A: last line or single word
            if i == len(words) or gaps == 0:
                temp = " ".join(line)
                temp += " " * (maxWidth - len(temp))
                res.append(temp)

            else:
                # Case B: normal line
                space_each = spaces // gaps
                extra = spaces % gaps

                temp = ""

                for j in range(gaps):
                    temp += line[j]
                    temp += " " * (space_each + (1 if j < extra else 0))

                temp += line[-1]
                res.append(temp)

        return res