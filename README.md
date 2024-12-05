│data/
│
├── raw/ # Dữ liệu chưa qua xử lý
│ ├── sports/ # Dữ liệu thể thao
│ ├──├─ abcd.txt #example
│ ├── politics/ # Dữ liệu chính trị
│ ├── economy/ # Dữ liệu kinh tế
│ ├── technology/ # Dữ liệu công nghệ
│ ├── education/ # Dữ liệu giáo dục
│ ├── health/ # Dữ liệu y tế & sức khỏe
│ ├── entertainment/ # Dữ liệu giải trí
│ ├── lifestyle/ # Dữ liệu đời sống & xã hội
│ ├── law/ # Dữ liệu pháp luật
│
├── processed/ # Dữ liệu đã qua tiền xử lý
│ ├── sports.csv # Dữ liệu thể thao đã xử lý
│ ├── politics.csv # Dữ liệu chính trị đã xử lý
│ ├── economy.csv # Dữ liệu kinh tế đã xử lý
│ ├── technology.csv # Dữ liệu công nghệ đã xử lý
│ ├── education.csv # Dữ liệu giáo dục đã xử lý
│ ├── health.csv # Dữ liệu y tế & sức khỏe đã xử lý
│ ├── entertainment.csv # Dữ liệu giải trí đã xử lý
│ ├── lifestyle.csv # Dữ liệu đời sống & xã hội đã xử lý
│ ├── law.csv # Dữ liệu pháp luật đã xử lý
│ └── environment.csv # Dữ liệu môi trường đã xử lý
│
├── notebooks/ # Các notebook Jupyter (nếu có)
│ ├── data_exploration.ipynb # Khám phá và phân tích dữ liệu
│ ├── model_training.ipynb # Huấn luyện mô hình
│ ├── evaluation.ipynb # Đánh giá mô hình
│
├── models/ # Mô hình đã huấn luyện và các kết quả
│ ├── model.pkl # Mô hình đã huấn luyện (saved model)
│ ├── vectorizer.pkl # Bộ vector hóa (nếu có)
│ ├── evaluation_results.csv # Kết quả đánh giá (accuracy, confusion matrix, etc.)
│
├── src/ # Mã nguồn chính của dự án
│ ├── **init**.py # Khởi tạo thư mục src
│ ├── preprocessing.py # Mã tiền xử lý dữ liệu
│ ├── model.py # Mã huấn luyện và đánh giá mô hình
│ ├── evaluate.py # Mã đánh giá mô hình
│ ├── utils.py # Các hàm tiện ích chung (chẳng hạn như lưu mô hình, v.v.)
│
├── logs/ # Các file log về quá trình huấn luyện và kết quả mô hình
│
├── requirements.txt # Các thư viện Python cần thiết cho dự án
├── README.md # Hướng dẫn và mô tả dự án
