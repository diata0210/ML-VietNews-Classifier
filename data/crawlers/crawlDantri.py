import requests
from bs4 import BeautifulSoup
import os
import re

# Hàm crawl và lưu bài viết
def crawl_and_save_articles(url, category, start_index, seen_titles):
    # Tạo thư mục lưu trữ nếu chưa có
    output_dir = f"data/raw/{category}/"
    os.makedirs(output_dir, exist_ok=True)

    # Gửi yêu cầu GET đến trang chính
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Tìm tất cả các bài viết dựa trên cấu trúc mới
    articles = soup.find_all('h3', {'class': 'article-title'})

    # Kiểm tra xem có bài viết nào không
    if not articles:
        print(f"Không có bài viết nào trên trang {url}. Dừng crawl.")
        return False  # Trả về False nếu không có bài viết

    # Đọc số lượng các bài viết đã có trong thư mục để xác định chỉ số tiếp theo
    existing_files = os.listdir(output_dir)
    existing_files = [f for f in existing_files if f.endswith('.txt')]  # Chỉ lấy các file .txt
    
    # Lấy tất cả chỉ số file đã tồn tại
    existing_indices = set()
    for file in existing_files:
        match = re.search(rf'{category}_(\d+)\.txt', file)
        if match:
            existing_indices.add(int(match.group(1)))

    # Tìm chỉ số tiếp theo mà không trùng
    next_index = 1
    while next_index in existing_indices:
        next_index += 1

    # Duyệt qua các bài viết và lưu
    for i, article in enumerate(articles, start=next_index):
        # Lấy tiêu đề bài viết
        title = article.find('a').get_text().strip()

        # Kiểm tra nếu tiêu đề đã tồn tại, bỏ qua bài viết này
        if title in seen_titles:
            print(f"Bài viết '{title}' đã tồn tại, bỏ qua.")
            continue  # Bỏ qua bài viết nếu tiêu đề đã tồn tại

        # Mở liên kết bài viết để lấy nội dung chi tiết
        link = article.find('a').get('href')
        if link.startswith('/'):
            link = "https://dantri.com.vn" + link  # Đảm bảo liên kết tuyệt đối

        try:
            article_response = requests.get(link)
            article_soup = BeautifulSoup(article_response.content, 'html.parser')

            # Loại bỏ các thẻ ảnh, caption và thẻ <p> có class "Normal" và style "text-align:right"
            for tag in article_soup.find_all(['picture', 'img', 'figcaption','figure']):
                tag.decompose()

            # Loại bỏ thẻ <p> có class "Normal" và style "text-align:right"
            for p_tag in article_soup.find_all('p', {'class': 'Normal', 'style': 'text-align:right;'}):
                p_tag.decompose()

            # Loại bỏ thẻ <div> chứa tên tác giả 
            for author_tag in article_soup.find_all('div',{'class': 'author-wrap'}):
                author_tag.decompose()
            
            # Loại bỏ thẻ <h1> chứa tiêu đề tránh bị lặp 
            for title_tag in article_soup.find_all('h1',{'class': 'title-page'}):
                title_tag.decompose()
            # Lấy nội dung bài viết
            content = article_soup.find('article')
            if content:
                # Lấy nội dung và loại bỏ các khoảng trắng dư thừa
                text = content.get_text().strip()

                # Kiểm tra xem nội dung có rỗng hay không
                if text:
                    # Loại bỏ các dòng trống dư thừa
                    text = re.sub(r'\n\s*\n', '\n', text)  # Thay thế các dòng trống bằng một dòng trống duy nhất

                    # Lưu bài viết vào tệp .txt theo đường dẫn tương đối
                    file_path = os.path.join(output_dir, f"{category}_{i}.txt")
                    
                    # Ghi nội dung vào file
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(f"{title}\n")  # Lưu tiêu đề bài viết
                        f.write(f"{text}\n")  # Lưu nội dung bài viết
                    print(f"Đã lưu bài viết {i}: {title}")
                else:
                    print(f"Bài viết {i} không có nội dung, bỏ qua: {title}")
            else:
                print(f"Không tìm thấy nội dung trong bài viết {i}: {title}")
        except requests.exceptions.RequestException as e:
            print(f"Lỗi khi lấy bài viết {i}: {title}. Lỗi: {e}")

    return True  # Nếu có bài viết, trả về True để tiếp tục crawl

# Hàm chính để truyền thể loại và URL
def main(category, base_url, start_page, end_page):
    seen_titles = set()  # Tạo tập hợp để theo dõi các tiêu đề đã gặp
    # Duyệt qua các trang từ start_page đến end_page
    for page in range(start_page, end_page + 1):
        # Tạo URL cho mỗi trang
        url = f"{base_url}/trang-{page}.htm"
        print(f"Đang crawl trang {page}: {url}")
        
        # Gọi hàm crawl_and_save_articles
        should_continue = crawl_and_save_articles(url, category, start_page, seen_titles)
        
        # Nếu không còn bài viết, dừng crawl
        if not should_continue:
            break

# Ví dụ gọi hàm main cho thể loại 'technology', từ trang 6 đến trang 36
main("health", "https://dantri.com.vn/suc-khoe", 2, 30)