import sys

def generate_strings(n, current_string):
    # যদি স্ট্রিংয়ের দৈর্ঘ্য N হয়ে যায়, তবে সেটি প্রিন্ট করি
    if len(current_string) == n:
        print(current_string)
        return

    # 'a', 'b', 'c' অক্ষরগুলোর জন্য লুপ
    for char in ['a', 'b', 'c']:
        # যদি স্ট্রিং খালি হয় অথবা নতুন অক্ষরটি আগের অক্ষরের সাথে না মিলে
        if not current_string or current_string[-1] != char:
            generate_strings(n, current_string + char)

def solve():
    # ইনপুট গ্রহণ
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    
    # রিকার্সিভ ফাংশন কল
    generate_strings(n, "")

if __name__ == "__main__":
    solve()