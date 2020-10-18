# https://leetcode.com/problems/generate-parentheses/


class Solution:
    def addParenthesis(
        self,
        prefix: str,
        totalAllowed: int,
        parenthesisOpened: int,
        parenthesisClosed: int,
    ):
        if totalAllowed is parenthesisOpened:
            prefix += (parenthesisOpened - parenthesisClosed) * ")"
            self.result.append(prefix)
            return

        self.addParenthesis(
            prefix + "(", totalAllowed, parenthesisOpened + 1, parenthesisClosed
        )
        if parenthesisOpened > parenthesisClosed:
            self.addParenthesis(
                prefix + ")", totalAllowed, parenthesisOpened, parenthesisClosed + 1
            )
        return

    def generateParenthesis(self, n: int) -> List[str]:
        self.result = []

        self.addParenthesis("", n, 0, 0)
        return self.result
