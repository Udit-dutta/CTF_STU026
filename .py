import pandas as pd
import hashlib

# --- Configuration ---
YOUR_BOOK_ID = '000751834X'
HASH_KEY = '927F09DE' # Confirmed FLAG2

# --- Load Data ---
try:
    books_df = pd.read_csv('books.csv')
except FileNotFoundError:
    print("ERROR: Please ensure 'books.csv' is uploaded and available.")
    exit() 

print(f"Retrieving book details for ID: {YOUR_BOOK_ID}...")

# 1. Identify YOUR BOOK's Title
your_book_data = books_df[books_df['parent_asin'] == YOUR_BOOK_ID]

if your_book_data.empty:
    print(f"FATAL: Book ID '{YOUR_BOOK_ID}' not found in books.csv. Check the 'parent_asin' column.")
    exit()

your_book_title = your_book_data['title'].iloc[0]

print(f"\n✅ YOUR BOOK Title is: '{your_book_title}'")

# 2. Extract FLAG1
# Take first 8 non-space characters of the title
title_clean = ''.join(c for c in your_book_title if not c.isspace())
flag1_input = title_clean[:8]

# Compute SHA256 of that string
flag1_hash = hashlib.sha256(flag1_input.encode('utf-8')).hexdigest()

print("\n--- RESULTS ---")
print(f"Input for FLAG1: \"{flag1_input}\"")
print(f"FLAG1 (SHA256): {flag1_hash}")
print(f"FLAG2 (Your Key): {HASH_KEY}")
print("---------------")