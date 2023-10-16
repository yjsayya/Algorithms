""""""
"""
책 쌓고 -- 힘이 얼마나 드는지 반환하는 문제였음 
"""

def solution(books, target):
    ans = 0
    book_indices = {book: i for i, book in enumerate(books)}

    print(book_indices)

    for book_num in target:
        idx = book_indices[book_num]
        ans += idx

        for key in book_indices:
            if book_indices[key] < idx:
                book_indices[key] += 1

        book_indices[book_num] = 0

    return ans