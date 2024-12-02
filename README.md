│data/
│
├── raw/ # Dữ liệu chưa qua xử lý
│ ├── sports/ # Dữ liệu thể thao
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
└── train_test_split/ # Dữ liệu đã chia thành tập huấn luyện và kiểm tra
| ├── train/ # Tập huấn luyện
| ├── test/ # Tập kiểm tra
| └── validation/ # Tập xác thực (nếu có)
|
│
├── notebooks/ # Jupyter notebooks cho các thử nghiệm và phân tích
│ ├── data_preprocessing.ipynb # Tiền xử lý dữ liệu
│ ├── exploratory_analysis.ipynb # Phân tích dữ liệu sơ bộ
│ └── model_training.ipynb # Huấn luyện mô hình
│
├── src/ # Mã nguồn chính
│ ├── **init**.py # Để biến thư mục thành một package Python
│
├── models/ # Các mô hình đã huấn luyện
│ ├── model_v1.pkl # Mô hình 1 (ví dụ Naive Bayes hoặc SVM)
│ └── model_v2.pkl # Mô hình 2 (ví dụ LSTM hoặc BERT)
│
├── logs/ # Các file log về quá trình huấn luyện và kết quả mô hình
│
├── requirements.txt # Các thư viện Python cần thiết cho dự án
├── README.md # Hướng dẫn và mô tả dự án
