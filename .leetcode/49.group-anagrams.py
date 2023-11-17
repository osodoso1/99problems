#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
# https://leetcode.com/problems/group-anagrams/description/
#
# algorithms
# Medium (67.16%)
# Likes:    17609
# Dislikes: 525
# Total Accepted:    2.3M
# Total Submissions: 3.5M
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# Given an array of strings strs, group the anagrams together. You can return
# the answer in any order.
# 
# An Anagram is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters exactly
# once.
# 
# 
# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:
# Input: strs = [""]
# Output: [[""]]
# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]
# 
# 
# Constraints:
# 
# 
# 1 <= strs.length <= 10^4
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.
# ####################NOTES
#  #two strings are anagrams of eachother and sort them. 
#one way to group them is to take the strings in the stings and sort them
#time is m * nlogn
#at most we have 26 uique charactres
#use an array count, to count a-z, 1E, 1A, 1T if we use hasmaps
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      res = defaultdict(list)  # Mapping character count of each string to list of anagrams
      for s in strs:
            count = [0] * 26  # From 'a' to 'z'

            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)
      return list(res.values())
# @lc code=end

