import requests
from bs4 import BeautifulSoup
import os
import re

# Hàm crawl và lưu bài viết
def crawl_and_save_articles(url, category):
    # Tạo thư mục lưu trữ nếu chưa có
    output_dir = f"data/raw/{category}/"
    os.makedirs(output_dir, exist_ok=True)

    # Gửi yêu cầu GET đến trang chính
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Tìm tất cả các bài viết dựa trên cấu trúc mới
    articles = soup.find_all('h3', {'class': 'title-news'})

    # Duyệt qua các bài viết và lưu
    for i, article in enumerate(articles):
        # Lấy tiêu đề bài viết
        title = article.find('a').get_text().strip()

        # Mở liên kết bài viết để lấy nội dung chi tiết
        link = article.find('a').get('href')
        if link.startswith('/'):
            link = "https://vnexpress.net" + link  # Đảm bảo liên kết tuyệt đối

        try:
            article_response = requests.get(link)
            article_soup = BeautifulSoup(article_response.content, 'html.parser')

            # Loại bỏ các thẻ ảnh để tránh lưu dữ liệu ảnh
            for img_tag in article_soup.find_all(['picture', 'img']):
                img_tag.decompose()

            # Lấy nội dung bài viết
            content = article_soup.find('article')
            if content:
                # Lấy nội dung và loại bỏ các khoảng trắng dư thừa
                text = content.get_text().strip()

                # Loại bỏ các dòng trống dư thừa
                text = re.sub(r'\n\s*\n', '\n', text)  # Thay thế các dòng trống bằng một dòng trống duy nhất

                # Lưu bài viết vào tệp .txt theo đường dẫn tương đối
                file_path = os.path.join(output_dir, f"{category}_{i + 1}.txt")
                
                # Ghi tiêu đề và nội dung vào tệp (Không ghi "Title: ")
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(f"{title}\n")  # Lưu tiêu đề bài viết
                    f.write(f"{text}\n")  # Lưu nội dung bài viết
                print(f"Đã lưu bài viết {i + 1}: {title}")
            else:
                print(f"Không tìm thấy nội dung trong bài viết {i + 1}: {title}")
        except requests.exceptions.RequestException as e:
            print(f"Lỗi khi lấy bài viết {i + 1}: {title}. Lỗi: {e}")

# Hàm chính để truyền thể loại và URL
def main(category, url):
    crawl_and_save_articles(url, category)

# Ví dụ gọi hàm main cho thể loại 'economy'
main("entertaiment", "https://vnexpress.net/giai-tri")

# Ví dụ gọi hàm main cho thể loại 'sports'
# main("sports", "https://vnexpress.net/the-thao")
