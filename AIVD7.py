# -- DEZE VROUW --
words = ['WE','EBGXAIOFULXXEECFXASWEXVBQNCXBVEBEWEKFU', 'DSFWWENHESFWKFXWKVWALDZKES']

let = set()
for word in words:
    w = [ord(l)-64 for l in word]
    wsum = sum(w)
    print(f"{word}:\t {wsum} \t{w}")
    for l in word:
        let.add(l)
print(f"all letters in wordlist: {sorted(let)}, that is {len(let)} letters")

for word in words:
    print([chr(ord(l)-1) for l in word])