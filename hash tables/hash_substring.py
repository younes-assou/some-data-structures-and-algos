# python3
_multiplier = 2633
_prime = 1000000007

def poly_hash(s):
    ans = 0
    for c in reversed(s):
        ans = (ans *_multiplier + ord(c)) % _prime
    return ans % _prime

def precompute_hashes(T,len_P):
    H = [0]*(len(T)-len_P+1)
    S = T[len(T)-len_P:]
    H[len(T)-len_P] = poly_hash(S)
    y = 1
    for i in range(0,len_P):
        y = (y*_multiplier) % _prime
    for i in reversed(range(0, len(T)-len_P)):
        H[i] = (_multiplier*H[i+1] + ord(T[i]) - y*ord(T[i+len_P])) % _prime
    return H

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    matchs = []
    phash = poly_hash(pattern)
    H = precompute_hashes(text, len(pattern))
    for i in range(len(H)):
        if phash != H[i]:
            continue
        if text[i:i+len(pattern)] == pattern:
            matchs.append(i)
    return matchs

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))