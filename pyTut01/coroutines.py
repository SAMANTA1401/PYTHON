def searcher():
    import time
    # some 4 seconds time consuming task
    book = "This is a book on harry and code with harry and gold"

    time.sleep(4)
    while True:
        text = (yield)
        if text in book:
            print("Your test is in the book")
        else:
            print("text is not in the book")

search = searcher()
next(search)
search.send("harry")
input("press any key")
search.send("marry and")
