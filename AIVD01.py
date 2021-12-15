# --- Word value ---


words = ['EMIR', 'ERKER', 'GELS', 'IEDER', 'REST', 'RIBBEL', 'STAD', 'TALK']
let = set()
for word in words:
    w = [ord(l)-64 for l in word]
    wsum = sum(w)
    print(f"{word}:\t {wsum} \t{w}")
    for l in word:
        let.add(l)
print(f"all letters in wordlist: {let}, that is {len(let)} letters")

for word in words:
    print([chr(ord(l)-1) for l in word])
# -------
opgave6 = [4.5, 0.5, 2, 18, 0.5625, 20.25, 10.125, 364.5, 182.25, 6561, 2916, 1458, 648, 324, 144]