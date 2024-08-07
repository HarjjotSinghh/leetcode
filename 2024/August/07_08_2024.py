# My Solution
class Solution:
    number_to_words_map = {
        1000000000: "Billion", 1000000: "Million", 1000: "Thousand",
        100: "Hundred", 90: "Ninety", 80: "Eighty", 70: "Seventy",
        60: "Sixty", 50: "Fifty", 40: "Forty", 30: "Thirty",
        20: "Twenty", 19: "Nineteen", 18: "Eighteen", 17: "Seventeen",
        16: "Sixteen", 15: "Fifteen", 14: "Fourteen", 13: "Thirteen",
        12: "Twelve", 11: "Eleven", 10: "Ten", 9: "Nine", 8: "Eight",
        7: "Seven", 6: "Six", 5: "Five", 4: "Four", 3: "Three",
        2: "Two", 1: "One"
    }
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        for value, word in self.number_to_words_map.items():
            if num >= value:
                prefix = (self.numberToWords(num // value) + " ") if num >= 100 else ""
                unit = word
                suffix = "" if num % value == 0 else " " + self.numberToWords(num % value)
                return prefix + unit + suffix
        return ""

# Best / Most Optimal Solution
class Solution2:
    def numberToWords(self, num: int) -> str:
        def helper(num):
            if num < 20:
                s = belowTwenty[num]
            elif num < 100:
                s = tens[num // 10] + " " + belowTwenty[num % 10]
            elif num < 1000:
                s = helper(num // 100) + " Hundred " + helper(num % 100)
            elif num < 1000000:
                s = helper(num // 1000) + " Thousand " + helper(num % 1000)
            elif num < 1000000000:
                s = helper(num // 1000000) + " Million " + helper(num % 1000000)
            else:
                s = helper(num // 1000000000) + " Billion " + helper(num % 1000000000)
            return s.strip()

        if num == 0:
            return "Zero"
        belowTwenty = [
            "",
            "One",
            "Two",
            "Three",
            "Four",
            "Five",
            "Six",
            "Seven",
            "Eight",
            "Nine",
            "Ten",
            "Eleven",
            "Twelve",
            "Thirteen",
            "Fourteen",
            "Fifteen",
            "Sixteen",
            "Seventeen",
            "Eighteen",
            "Nineteen",
        ]

        tens = [
            "",
            "Ten",
            "Twenty",
            "Thirty",
            "Forty",
            "Fifty",
            "Sixty",
            "Seventy",
            "Eighty",
            "Ninety",
        ]
        return helper(num)
