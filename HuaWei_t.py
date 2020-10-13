
password = ''


while True:
    try:
        ori_s = input()

        for c in ori_s:
            if c.isupper():
                if c is not 'Z':
                    password +=chr(ord(i.lower())+1)
                elif c is "Z":
                    password += 'a'

            elif c.islower():
                if c in "abc":
                    password += "2"
                elif c in "def":
                    password += '3'   
                elif c in "ghi":
                    password += '4'
                elif c in "jkl":
                    password += '5'
                elif c in "mno":
                    password += '6'
                elif c in "pqrs":
                    password += '7'
                elif c in "tuv":
                    password += '8':
                elif c in "wxyz":
                    password += '9'
            elif c.isdigit():
                password +=c
    except:
        break
print(pw)     
