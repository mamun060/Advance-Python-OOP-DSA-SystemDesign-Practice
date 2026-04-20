import sys

def solve():
    # ইনপুট গ্রহণ
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    s = int(input_data[0])
    
    # সূত্র অনুযায়ী ফলাফল বের করা: 2^(S-1)
    # S=1 হলে 2^0 = 1
    # S=3 হলে 2^2 = 4
    ans = 2 ** (s - 1)
    
    print(ans)

if __name__ == "__main__":
    solve()