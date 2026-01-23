# 🧮 ITUFP

Khai thác Top-K các mẫu tiện ích cao từ dữ liệu không chắc chắn (Top-K High-Utility Pattern Mining from Uncertain Data) là một lĩnh vực quan trọng trong khai thác dữ liệu.

Sự xuất hiện của thuật toán TUFP đã hỗ trợ việc khai thác tĩnh Top-K. Tuy nhiên, trong thực tế thì người dùng cần thường xuyên điều chỉnh ngưỡng k để phù hợp với yêu cầu của ứng dụng. Trong môi trường tương tác, việc sử dụng thuật toán TUFP đòi hỏi phải quét lại cơ sở dữ liệu nhiều lần.

Để khắc phục hạn chế này, phương pháp `ITUFP` (Interactive Top-K Uncertain Frequent Pattern mining algorithm) đã được đề xuất để khai thác các UFP Top-K trong môi trường tương tác, tuân theo nguyên tắc **xây dựng một lần, khai thác nhiều lần**.

## Cấu trúc dự án

```

├── data/                   // Chứa dữ liệu đầu vào
│   ├── example.txt         // Dữ liệu kiểm thử
│   └── foodmart.txt        // Dữ liệu chính thức
├── output/                 // Chứa kết quả Top-K UFP theo ngưỡng k tương ứng
│   ├── example.txt
│   └── foodmart.txt
├── papers/                 // Tài liệu tham khảo
├── brute_force.py          // Giải thuật đơn giản để kiểm thử
├── ITUFP.ipynb             // Giải thuật chính
└── README.md

```

## Bộ dữ liệu

Bộ dữ liệu sử dụng trong thực nghiệm này được tham khảo từ bộ [Foodmart](https://www.philippe-fournier-viger.com/spmf/index.php?link=datasets.php#d3).

## Hướng dẫn chạy dự án

### 1. Điều kiện

- [Git](https://git-scm.com/)

### 2. Sao chép kho lưu trữ

```bash
git clone https://github.com/Thanh-Binhhh/ITUFP.git
```

### 3. Khởi động dự án

Tiến hành chạy file `ITUFP.ipynb`

# 📝 Tác giả

- **Thanh Bình** - [Github](https://github.com/Thanh-Binhhh) | [Github Student](https://github.com/Thanh-Binhh)
