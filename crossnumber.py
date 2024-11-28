ones = ['εἱς','δυο','τρεις','τεσσαρες','πεντε','ἑξ','ἑπτα','ὀκτω','ἐννεα']
teens = ['ἑν','δω','τρεις','τεσσαρες','πεντε','ἑκ','ἑπτα','ὀκτω','ἐννεα']
tens = ['δεκα','εἰκοσι','τρια','τεσσαρα','πεντη','ἑκη','ἑβδομη','ὀγδοη','ἐνενη']
hundreds = ['ἑκατον','δι','τρι','τετρ','πεντ','ἑξ','ἑπτ','ὀκτ','ἐν']

def convert(num):
    if num < 10:
        return ones[num-1]      
    elif num == 10:
        return 'δεκα'

    elif num < 20:
        if num <= 12:
            return teens[int(str(num)[-1])-1]+'δεκα'
        elif num <= 14:
            return teens[int(str(num)[-1])-1]+' και δεκα'
        else:
            return teens[int(str(num)[-1])-1]+'καιδεκα'

    elif num < 100:
        s = ''
        ten = num//10
        if ten <= 2:
            s +=  tens[ten-1]
        else:
            s += tens[ten-1]+'κοντα'
        if ten != num/10:
            return s + ' και ' + ones[int(str(num)[-1])-1]
        else:
            return s

    elif num == 1000:
        return 'χιλιοι'

    elif num >= 100:
        hundred = num//100
        if hundred == 1:
            s = hundreds[0]
        else:
            s = hundreds[(num//100)-1]+'ακοσιοι'
        if hundred == num/100:
            return s
        else:
            return s + ' και ' + convert(int(str(num)[-2:]))

squares = []
for i in range(1,32):
    squares.append(convert(i**2))

cubes = []
for i in range(1,11):
    cubes.append(convert(i**3))

def row2col(text):
    for i in text:
        print(i)

limit = 1000
nums = [True] * (limit+1)
primes = []
i = 2
while i**2 <= limit:
    if nums[i]:
        primes.append(i)
        for j in range(i**2, limit+1, i):
            nums[j] = False
    i += 1
for j in range(i, limit+1):
    if nums[j]:
        primes.append(j)

primes_o = primes.copy()
primes = [convert(i) for i in primes]

fibonacci = []
n1 = n2 = 1
while n2 < 1000:
    fibonacci += [n2]
    on2 = n2
    n2 += n1
    n1 = on2
fibonacci = [convert(i) for i in fibonacci]

factorial = []
c = 1
for i in range(1,7):
    c *= i
    factorial += [c]
factorial = [convert(i) for i in factorial]

semiprimes_o = []
for i in primes_o:
    for j in primes_o:
        if i*j not in semiprimes_o and i*j <= 1000:
            semiprimes_o.append(i*j)

t = 0
c = 1
triangles = []
while t < 1000:
    t += c
    c += 1
    triangles += [t]
triangles = [convert(i) for i in triangles[0:-1]]

fourths = []
for i in range(1,6):
    fourths.append(convert(i**4))