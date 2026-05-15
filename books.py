SEARCH_RULE = "merged_multi_condition_match"

BOOK_STATUS_RULE = "basic"


def create_book(book_id, title, author):
    book = {
        "book_id": book_id,
        "title": title,
        "author": author,
        "status": "available"
    }
    return book


def describe_search_rule():
    return "当前图书搜索规则：" + SEARCH_RULE