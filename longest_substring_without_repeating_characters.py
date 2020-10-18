class Solution:
    #Longest Substring Without Repeating Characters (medium)
    
    def invalidateChars(self, substringContents: dict, slowPointer: int, firstOccurancePosition: int, s: str):
        for index in range(slowPointer, firstOccurancePosition + 1):
            substringContents.pop(s[index])
            
            
    def lengthOfLongestSubstring(self, s: str) -> int:

        fastPointer = 1
        slowPointer = 0
        longestSubstring = 0

        #character key and its position in the big string as value
        substringContents = dict()

        for index in range(0, len(s)):
            if (s[index] in substringContents):
                
                if (longestSubstring < len(substringContents)):
                    longestSubstring = len(substringContents)
                
                #remove everything from slowPointer up to and including the first duplicate occurance
                firstOccuranceIndex = substringContents[s[index]]
                self.invalidateChars(substringContents, slowPointer, firstOccuranceIndex, s)
            
                #slowpointer moved to element after the duplicate
                slowPointer = firstOccuranceIndex + 1;
            
            substringContents[s[index]] = index
        
        #in case the length of the dict has never been checked
        if (longestSubstring < len(substringContents)):
            longestSubstring = len(substringContents)
        return longestSubstring

