SEARCH_MODE = "basic"


def search_by_title(title):
    return "按照书名查询：" + title


def search_by_author(author):
    return "按照作者查询：" + author


def describe_search_mode():
    return "当前查询模式：" + SEARCH_MODE