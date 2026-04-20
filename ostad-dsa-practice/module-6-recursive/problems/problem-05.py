import sys

def get_all_subsets(index, current_str, s, result):
    # যদি বর্তমান স্ট্রিংটি খালি না হয়, তবে এটি একটি সাবসেট
    if current_str:
        result.append(current_str)
    
    # ইনপুট স্ট্রিংয়ের ক্রম বজায় রেখে সাবসেট তৈরি
    for i in range(index, len(s)):
        get_all_subsets(i + 1, current_str + s[i], s, result)

def solve():
    # ইনপুট রিড করা
    input_data = sys.stdin.read().strip()
    if not input_data:
        return
    
    # সাবসেটগুলো জমা রাখার জন্য লিস্ট
    subsets = []
    
    # সাবসেট জেনারেট করা (ইনপুট স্ট্রিংয়ের অরিজিনাল সিকুয়েন্স অনুযায়ী)
    get_all_subsets(0, "", input_data, subsets)
    
    # সবগুলো সাবসেটকে বর্ণানুক্রমে সাজানো
    subsets.sort()
    
    # প্রিন্ট করা
    for sub in subsets:
        print(sub)

if __name__ == "__main__":
    solve()