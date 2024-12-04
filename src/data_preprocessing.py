import os
import string
import pandas as pd
import re  # Import the re module
from vncorenlp import VnCoreNLP
from pyvi import ViTokenizer

# Khởi tạo VnCoreNLP (đảm bảo đã tải VnCoreNLP từ GitHub hoặc đường dẫn đúng)
vncorenlp = VnCoreNLP('D:/Code/VnCoreNLP/VnCoreNLP-1.1.1.jar', annotators="wseg,pos,ner,parse", max_heap_size='-Xmx2g')

# Hàm tải stopwords tiếng Việt từ file
def load_vietnamese_stopwords():
    stopwords = []
    with open('../data/stopwords.txt', 'r', encoding='utf-8') as f:
        stopwords = [line.strip() for line in f.readlines()]
    return stopwords

# Tải stopwords từ file
stop_words = load_vietnamese_stopwords()

def preprocess_text(text):
    # 1. Chuyển về chữ thường
    text = text.lower()

    # 2. Loại bỏ từ "dân trí" (bất kể hoa hay thường)
    text = text.replace("dân trí", "")

    # 3. Loại bỏ số
    text = ''.join([i for i in text if not i.isdigit()])

    # 4. Loại bỏ ký tự đặc biệt (ngoặc, dấu @, #, <>, v.v.)
    text = re.sub(r'[^\w\s]', '', text)

    # 5. Tokenization: Dùng pyvi để tách từ tiếng Việt
    tokens = ViTokenizer.tokenize(text).split()

    # 6. Loại bỏ stopwords
    tokens = [word for word in tokens if word not in stop_words]

    # 7. Loại bỏ dấu câu và ký tự đặc biệt
    tokens = [word for word in tokens if word not in string.punctuation]

    # 8. Loại bỏ khoảng trắng thừa
    tokens = [word.strip() for word in tokens if word.strip()]

    return " ".join(tokens)

# Hàm đọc và tiền xử lý dữ liệu từ file
def process_files_in_directory(directory_path):
    data = []
    # Duyệt qua các thư mục trong thư mục dữ liệu (ví dụ: sports, entertainment, etc.)
    for category in os.listdir(directory_path):
        category_path = os.path.join(directory_path, category)
        if os.path.isdir(category_path):
            # Duyệt qua các file văn bản trong thư mục mỗi category
            for filename in os.listdir(category_path):
                file_path = os.path.join(category_path, filename)
                if file_path.endswith('.txt'):
                    # Đọc nội dung file
                    try:
                        with open(file_path, 'r', encoding='utf-8-sig') as file:  # Thử đọc với utf-8-sig
                            text = file.read()
                            # Tiền xử lý văn bản
                            processed_text = preprocess_text(text)
                            # Thêm vào danh sách với nhãn category
                            data.append({'Text': processed_text, 'Label': category})
                    except UnicodeDecodeError:
                        print(f"Không thể đọc file {file_path}. Đảm bảo file có mã hóa UTF-8.")
                        continue
    
    # Chuyển thành DataFrame
    df = pd.DataFrame(data)
    return df

# Hàm lưu dữ liệu đã xử lý vào file CSV
def save_to_csv(df, output_path):
    df.to_csv(output_path, index=False)
    print(f"Dữ liệu đã được lưu vào {output_path}")

# Main function
if __name__ == "__main__":
    # Thư mục chứa dữ liệu gốc (raw data)
    input_directory = '../data/raw'  # Đã sửa đường dẫn
    # Đường dẫn lưu file CSV đã tiền xử lý
    output_file = '../data/processed/training_data.csv'  # Đường dẫn lưu file CSV

    # Tiền xử lý và lưu dữ liệu
    processed_data = process_files_in_directory(input_directory)
    save_to_csv(processed_data, output_file)
