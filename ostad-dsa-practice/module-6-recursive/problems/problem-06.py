import sys

def generate_permutations(current_str, sorted_chars, used, n):
    # যদি বর্তমান স্ট্রিংয়ের দৈর্ঘ্য N হয়, তবে একটি বিন্যাস পাওয়া গেছে
    if len(current_str) == n:
        print(current_str)
        return

    for i in range(n):
        # যদি অক্ষরটি ইতিমধ্যে ব্যবহার না হয়ে থাকে
        if not used[i]:
            used[i] = True
            generate_permutations(current_str + sorted_chars[i], sorted_chars, used, n)
            # ব্যাকট্র্যাক: পরবর্তী বিন্যাসের জন্য অক্ষরটিকে আবার ফ্রি করে দেওয়া
            used[i] = False

def solve():
    # ইনপুট গ্রহণ
    input_data = sys.stdin.read().strip()
    if not input_data:
        return
    
    # অক্ষরগুলোকে বর্ণানুক্রমে সাজানো
    sorted_chars = sorted(list(input_data))
    n = len(sorted_chars)
    used = [False] * n
    
    # রিকার্সিভ ফাংশন কল
    generate_permutations("", sorted_chars, used, n)

if __name__ == "__main__":
    solve()