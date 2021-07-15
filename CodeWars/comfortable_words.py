"""A comfortable word is a word which you can type always alternating the hand you type with (assuming you type using a
QWERTY keyboard and use fingers as shown in the image below).

That being said, create a function which receives a word and returns true/True if it's a comfortable word and
 false/False otherwise.

The word will always be a string consisting of only ascii letters from a to z.

To avoid problems with image availability, here's the lists of letters for each hand:

    Left: q, w, e, r, t, a, s, d, f, g, z, x, c, v, b
    Right: y, u, i, o, p, h, j, k, l, n, m

"""


def comfortable_word(x):
    left = ["q", "w", "e", "r", "t", "a", "s", "d", "f", "g", "z", "x", "c", "v", "b"]
    right = ["y", "u", "ı", "o", "p", "ğ", "ü", "h", "j", "k", "l", "ş", "i", "n", "m", "ö", "ç"]
    y = list(x)
    z = len(y)
    tek = y[1:z+1:2]
    print(tek)
    len_tek = len(tek)
    cift = y[0:z+1:2]
    len_cift = len(cift)
    print(cift)
    t = 0
    p = 0
    y = 0
    u = 0
    for i in tek:
        if i in left:
            t +=1
    if t == len_tek:
        for o in cift:
            if o in right:
                p += 1
        if p == len_cift:
            return True
    for b in tek:
        if b in right:
            y += 1
    if y == len_tek:
        for m in cift:
            if m in left:
                u += 1
        if u == len_cift:
            return True
        else:
            return False
    else:
        return False


