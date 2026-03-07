# Question-1-Password Strength Validator
class Solution:
    def strong_passwords(self, passwords):
        strong = []
        ##Write your code here
        for pwd in passwords:
            if len(pwd)<8:
                continue
            has_upper=False
            has_digit=False
            has_special=False
            for ch in pwd:
                if ch.isupper():
                    has_upper=True
                elif ch.isdigit():
                    has_digit=True
                elif ch in "@#$":
                    has_special=True
            
            if has_upper and has_digit and has_special:
                strong.append(pwd)
       
        return strong