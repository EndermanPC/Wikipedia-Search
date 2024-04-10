import wikipedia

def get_wikipedia_excerpt(keyword, sentences=2):
    try:
        # Set language
        wikipedia.set_lang("vi") # Chọn ngôn ngữ bạn muốn lấy dữ liệu

        # Search for the keyword
        search_results = wikipedia.search(keyword)

        if not search_results:
            return "Không tìm thấy thông tin liên quan đến từ khóa này trên Wikipedia."

        # Get page summary from the first search result
        page_summary = wikipedia.summary(search_results[0], sentences=sentences)

        return page_summary
    except wikipedia.exceptions.WikipediaException as e:
        return "Có lỗi xảy ra: {}".format(str(e))

# Test function
keyword = input("Nhập từ khóa bạn muốn tìm trên Wikipedia: ")
excerpt = get_wikipedia_excerpt(keyword)
print("Đoạn trích từ Wikipedia:")
print(excerpt)
