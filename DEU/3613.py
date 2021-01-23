"""
if contains "_" -> C++ , _+첫 글자 -> 대문자 변환
else -> Java, 대문자 -> 대문자 첫 글자 -> _+소문자변환
"""
M = list(input())

def translate(N):
    try:
        if(N[0]=="_" or N[0].isupper()):
            return "Error!"
        if("_" in N):
            while ("_" in N):
                idx = N.index("_")
                if(N[idx+1]=="_"):
                    return "Error!"
                N[idx+1] = N[idx+1].upper()
                N.remove("_")
        else:
            for i in range(len(N)):
                if(N[i].isupper()):
                    N[i] = "_"+N[i].lower()

        return N
    except Exception :
        return "Error!"

print(''.join(translate(M)))