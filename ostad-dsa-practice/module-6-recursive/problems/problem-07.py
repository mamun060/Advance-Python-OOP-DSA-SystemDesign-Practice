import sys

# হিসাব করা মানগুলো জমা রাখার জন্য ডিকশনারি (Memoization table)
memo = {0: 1}

def f(n):
    # যদি মানটি আগে থেকেই ডিকশনারিতে থাকে, তবে সেটি রিটার্ন করি
    if n in memo:
        return memo[n]
    
    # ফাংশনের সূত্র অনুযায়ী: f(k) = f(k/2) + f(k/3)
    # // চিহ্নটি পূর্ণসংখ্যা ভাগের (floor division) জন্য ব্যবহৃত হয়
    res = f(n // 2) + f(n // 3)
    
    # ফলাফলটি ভবিষ্যতে ব্যবহারের জন্য জমা রাখি
    memo[n] = res
    return res

def solve():
    # ইনপুট গ্রহণ
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    try:
        n = int(input_data[0])
        # f(N) এর মান বের করে প্রিন্ট করি
        print(f(n))
    except ValueError:
        return

if __name__ == "__main__":
    # পাইথনের ডিফল্ট রিকার্সন লিমিট বাড়িয়ে নেওয়া ভালো, যদিও এই সমস্যার জন্য প্রয়োজন না-ও হতে পারে
    sys.setrecursionlimit(2000)
    solve()