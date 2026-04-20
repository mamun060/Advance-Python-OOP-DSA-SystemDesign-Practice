import sys

def solve():
    # ইনপুট গ্রহণ
    try:
        line = sys.stdin.read().split()
        if not line:
            return
        n = int(line[0])
        m = int(line[1])
    except EOFError:
        return

    ans = 0
    
    # যতক্ষণ পর্যন্ত রুমের দৈর্ঘ্য বা প্রস্থ থাকে
    while n > 0 and m > 0:
        # যদি n বিজোড় হয়, তবে এক সারি m দৈর্ঘ্যের টাইলস লাগবে
        if n % 2 != 0:
            ans += m
            n -= 1
        
        # যদি m বিজোড় হয়, তবে এক কলাম n দৈর্ঘ্যের টাইলস লাগবে
        if m % 2 != 0:
            ans += n
            m -= 1
        
        # এখন n এবং m উভয়ই জোড়, তাই আমরা বড় টাইলস (2x2) এ চলে যাই
        # n এবং m কে ২ দিয়ে ভাগ করা মানে আমরা টাইলসের সাইজ দ্বিগুণ করছি
        n //= 2
        m //= 2
        
    print(ans)

if __name__ == "__main__":
    solve()