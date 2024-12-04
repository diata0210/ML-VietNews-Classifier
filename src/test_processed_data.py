import pandas as pd
import os
import logging
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Thiết lập logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Hàm kiểm tra tệp CSV đã xử lý
def test_processed_file(file_path):
    """
    Kiểm tra dữ liệu đã xử lý trong tệp CSV và kiểm tra độ chính xác của mô hình phân loại.
    """
    if not os.path.exists(file_path):
        logging.error(f"Tệp {file_path} không tồn tại.")
        return

    # Đọc dữ liệu từ tệp CSV
    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        logging.error(f"Lỗi khi đọc tệp {file_path}: {e}")
        return

    # Kiểm tra xem tệp có cột 'cleaned_text' và 'label'
    if 'cleaned_text' not in df.columns or 'label' not in df.columns:
        logging.error(f"Tệp {file_path} không chứa cột 'cleaned_text' hoặc 'label'.")
        return

    # Kiểm tra xem có giá trị nào rỗng trong cột 'cleaned_text'
    empty_rows = df[df['cleaned_text'].isnull() | (df['cleaned_text'].str.strip() == '')]
    if not empty_rows.empty:
        logging.warning(f"Tệp {file_path} có {len(empty_rows)} dòng trống trong 'cleaned_text'.")

    # Kiểm tra dữ liệu trong một vài dòng
    sample_data = df.head(5)  # Lấy 5 dòng đầu tiên để kiểm tra
    logging.info(f"Một số dữ liệu trong tệp {file_path}:")
    logging.info(sample_data)

    # Kiểm tra số lượng dòng trong tệp
    total_rows = len(df)
    logging.info(f"Tệp {file_path} có tổng cộng {total_rows} dòng dữ liệu.")
    
    # Kiểm tra độ chính xác của mô hình phân loại
    check_accuracy(df)

# Hàm kiểm tra độ chính xác của mô hình phân loại
def check_accuracy(df):
    """
    Kiểm tra độ chính xác của mô hình phân loại với dữ liệu đã xử lý.
    """
    # Tách dữ liệu thành X (văn bản) và y (nhãn)
    X = df['cleaned_text']
    y = df['label']
    
    # Chia dữ liệu thành tập huấn luyện và kiểm tra
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # Biến đổi văn bản thành dạng vector (TF-IDF)
    vectorizer = TfidfVectorizer(stop_words='english')
    X_train_tfidf = vectorizer.fit_transform(X_train)
    X_test_tfidf = vectorizer.transform(X_test)
    
    # Huấn luyện mô hình Naive Bayes
    model = MultinomialNB()
    model.fit(X_train_tfidf, y_train)
    
    # Dự đoán và đánh giá mô hình
    y_pred = model.predict(X_test_tfidf)
    accuracy = accuracy_score(y_test, y_pred)
    
    # In ra độ chính xác và báo cáo phân loại
    logging.info(f"Độ chính xác của mô hình là: {accuracy * 100:.2f}%")
    logging.info(f"Báo cáo phân loại:\n{classification_report(y_test, y_pred)}")

# Kiểm tra tất cả các tệp CSV trong thư mục processed
def test_all_processed_files():
    categories = ['sports', 'politics', 'technology', 'health', 'lifestyle', 'law', 'entertaiment']
    
    for category in categories:
        file_path = f"data/processed/{category}.csv"
        test_processed_file(file_path)

if __name__ == "__main__":
    test_all_processed_files()
