# Neutralisation

## Task Description
This task involves returning a new string based on the interaction of two strings composed of the symbols `+` and `-`. The interactions are processed according to the following rules:

1. When `+` interacts with `+`, the result remains `+`.
2. When `-` interacts with `-`, the result remains `-`.
3. When `+` interacts with `-`, the result becomes `0`.

## Examples
- `neutralise("+-+", "+--")` ➞ `"+-0"`
- `neutralise("--++--", "++--++")` ➞ `"000000"`
- `neutralise("-+-+-+", "-+-+-+")` ➞ `"-+-+-+"`
- `neutralise("-++-", "-+-+")` ➞ `"-+00"`

## How to Use
You can use the `neutralise` function as follows:

```python
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

# Examples of usage
print(neutralise("+-+", "+--"))        # ➞ "+-0"
print(neutralise("--++--", "++--++"))   # ➞ "000000"
print(neutralise("-+-+-+", "-+-+-+")   # ➞ "-+-+-+"
print(neutralise("-++-", "-+-+"))       # ➞ "-+00"
Notes
The two strings will be of the same length.
You can modify the function to suit your specific needs


### How to Use the `README.md` File

1. Open your preferred text editor.
2. Create a new file and name it `README.md`.
3. Copy the content provided above and paste it into the new file.
4. Save the file.

Feel free to modify the content as needed for your project!



# Neutralisation


## وصف المهمة
تقوم هذه المهمة بإرجاع سلسلة جديدة بناءً على تفاعل سلسلتين من الرموز `+` و `-`. تتم معالجة التفاعلات بين الرموز وفقًا للقواعد التالية:

1. عندما تتفاعل رموز `+` مع `+`، تبقى النتيجة `+`.
2. عندما تتفاعل رموز `-` مع `-`، تبقى النتيجة `-`.
3. عند تفاعل `+` مع `-`، تصبح النتيجة `0`.

## أمثلة
- `neutralise("+-+", "+--")` ➞ `"+-0"`
- `neutralise("--++--", "++--++")` ➞ `"000000"`
- `neutralise("-+-+-+", "-+-+-+")` ➞ `"-+-+-+"`
- `neutralise("-++-", "-+-+")` ➞ `"-+00"`

## كيفية الاستخدام
يمكنك استخدام الدالة `neutralise` كما يلي:

```python
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
ملاحظات
السلسلتان ستكونان بنفس الطول.
يمكنك تعديل الدالة لتناسب احتياجاتك الخاصة.

### كيفية استخدام ملف `README.md`

1. افتح محرر النصوص المفضل لديك.
2. أنشئ ملفًا جديدًا وسمه `README.md`.
3. انسخ محتوى ملف `README.md` أعلاه والصقه في الملف الجديد.
4. احفظ الملف.

يمكنك تعديل المحتوى كما تشاء حسب احتياجات مشروعك!
