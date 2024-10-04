def neutralise(s1, s2):
    result = ""
    for char1, char2 in zip(s1, s2):
        if char1 == "+" and char2 == "+":
            result += "+"
        elif char1 == "-" and char2 == "-":
            result += "-"
        else:
            result += "0"
    return result

# أمثلة على الاستخدام
print(neutralise("+-+", "+--"))        # ➞ "+-0"
print(neutralise("--++--", "++--++"))   # ➞ "000000"
print(neutralise("-+-+-+", "-+-+-+"))   # ➞ "-+-+-+"
print(neutralise("-++-", "-+-+"))       # ➞ "-+00"

