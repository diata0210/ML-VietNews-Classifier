# Lấy tất cả các thẻ <p> trong nội dung
                p_tags = content.find_all('p')

                # Lấy nội dung của từng thẻ <p> và lưu vào danh sách
                paragraphs = [p.get_text(separator=' ').strip() for p in p_tags]

                # Ghép các đoạn văn với dấu xuống dòng giữa các thẻ <p>
                text = '\n'.join(paragraphs)
