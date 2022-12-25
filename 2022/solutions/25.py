# --- Day 25: Full of Hot Air ---
lines = open('../input/25i.txt').read().splitlines()

def deSNAFU(nr):
    num = 0
    l = len(nr) -1
    for n in range(len(nr)):
        if nr[n] == "=":
            num -= 2*5**(l-n)
            continue
        if nr[n] == "-":
            num -= 5**(l-n)
            continue
        num += int(nr[n]) * 5**(l-n)
    return num

snafu_sum = sum(map(deSNAFU, lines))

def reSNAFU(nr):
    out = ""
    while nr:
        rem = nr % 5
        nr //= 5
        print(f"rem: {rem}  out: {out}   nr: {nr}")

        if rem <= 2:
            out = str(rem) + out
        else:
            out = "   =-"[rem] + out
            nr += 1
    return out

print("SNAFU:", reSNAFU(snafu_sum))
