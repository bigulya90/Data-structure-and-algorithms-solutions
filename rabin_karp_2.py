def Rabin_Karp_Matcher(text, pattern, d, q):
    n = len(text)
    m = len(pattern)
    h = pow(d,m-1)%q
    p = 0
    t = 0
    result = []
    for i in range(m): # preprocessing
        p = (d*p+ord(pattern[i]))%q
        t = (d*t+ord(text[i]))%q
    for s in range(n-m+1): # note the +1
        if p == t: # check character by character
            match = True
            for i in range(m):
                if pattern[i] != text[s+i]:
                    match = False
                    break
            if match:
                result = result + [s]
        if s < n-m:
            t = (t-h*ord(text[s]))%q # remove letter s
            t = (t*d+ord(text[s+m]))%q # add letter s+m
            t = (t+q)%q # make sure that t >= 0
    return result
print (Rabin_Karp_Matcher ("3141592653589793", "26", 257, 11))
print (Rabin_Karp_Matcher ("xxxxx", "xx", 40999999, 999999937))




d = 256

def search(pat, txt, q):
    M = len(pat)
    N = len(txt)
    i = 0
    j = 0
    p = 0  # hash value for pattern
    t = 0  # hash value for txt
    h = 1

    for i in xrange(M - 1):
        h = (h * d) % q

    for i in xrange(M):
        p = (d * p + ord(pat[i])) % q
        t = (d * t + ord(txt[i])) % q

    for i in xrange(N - M + 1):
        if p == t:
            for j in xrange(M):
                if txt[i + j] != pat[j]:
                    break

            j += 1
            if j == M:
                print "Pattern found at index " + str(i)

        if i < N - M:
            t = (d * (t - ord(txt[i]) * h) + ord(txt[i + M])) % q

            if t < 0:
                t = t + q


txt = "GEEKS FOR GEEKS"
pat = "GEEK"
q = 101  # A prime number
search(pat, txt, q)

