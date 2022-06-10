s = "catsanddog"
wordDict = ['cats','dog','sand','and','cat']

class Solution(object):
    def wordBreak(self, s, wordDict):
        if not s:
            return[]

        return self.tester(s, wordDict, {})

    def tester(self, s, wordDict, memo):
        if s in memo:
            return memo[s]
        
        if not s:
            return

        res = []

        for w in wordDict:
            if s.startwith(w):
                if len(s) == len(w):
                    res.append(w)
                else:
                    ans = self.tester(s[len(w):], wordDict, memo)
                    for gym in ans:
                        res.append(w+' '+gym)

        memo[s] = res
        # return res
        print(res)
