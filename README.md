# 🧮 ITUFP

TUFP (Top-K Uncertain Frequent Pattern Mining) là thuật toán khai thác K tập hợp mục thường xuyên nhất / K tập hợp mục có **Độ hỗ trợ kỳ vọng (expected support) cao nhất** từ CSDL giao dịch. Trong bài toán này, mỗi mục trong từng giao dịch được gắn với một xác suất xuất hiện, phản ánh mức độ không chắc chắn của dữ liệu.

Tuy nhiên, TUFP chủ yếu hỗ trợ việc khai thác tĩnh các Top-K UFP. Trong thực tế, người dùng có thể thường xuyên thay đổi giá trị K để đáp ứng các yêu cầu khác nhau của ứng dụng. Khi giá trị K thay đổi, TUFP phải quét lại cơ sở dữ liệu và thực hiện lại quá trình xây dựng các cấu trúc cần thiết, điều này làm gia tăng thời gian xử lý và chi phí truy xuất dữ liệu.

Để khắc phục hạn chế này, thuật toán **ITUFP** (Interactive Top-K Uncertain Frequent Pattern Mining) được đề xuất nhằm khai thác Top-K UFP trong môi trường tương tác.

ITUFP sử dụng cấu trúc dữ liệu IMCUP-List để lưu trữ thông tin của các mục được khai thác, nhằm đảm bảo nguyên tắc **“xây dựng một lần, khai thác nhiều lần” (build once, mine many)**. Khi giá trị K thay đổi, thuật toán có thể cập nhật và tái sử dụng các cấu trúc đã xây dựng thay vì thực hiện lại toàn bộ quá trình từ đầu.

## Mô tả dữ liệu

#### 1. Dữ liệu đầu vào

Đầu vào là tệp văn bản. Một dòng trong tệp là một giao dịch. Mỗi giao dịch bao gồm một tập hợp các mặt hàng (được biểu diễn bằng các số nguyên dương), với giả định rằng mỗi mặt hàng được gán một xác suất tồn tại (được biểu diễn bằng các số thực trong khoảng [0,1]):

```
item1 item2 ... itemm : p1 p2 ... pm
```

Trong đó:

- `item1, item2, ..., itemm` là các mặt hàng xuất hiện trong giao dịch.
- `p1, p2, ..., pm` là xác suất tồn tại tương ứng của các mặt hàng theo thứ tự.
- Các mặt hàng không xuất hiện trong giao dịch được hiểu là có xác suất bằng 0.

Trong quá trình thực nghiệm, dự án sử dụng bộ dữ liệu [Retail](https://u-aizu.ac.jp/~udayrage/datasets.html?utm_source=chatgpt.com) thuộc nhóm Real-world uncertain transaction databases được cung cấp bởi University of Aizu Dataset Repository.

#### 2. Dữ liệu đầu ra

Tệp đầu ra cung cấp danh sách K tập hợp mục thường xuyên nhất trong CSDL giao dịch không chắc chắn, được sắp xếp theo độ hỗ trợ kỳ vọng giảm dần. Mỗi dòng trong tệp đại diện cho một tập hợp mục.

Kết quả được biểu diễn dưới hai dạng:

**Mẫu gồm một mặt hàng - `UP_List`**

Ví dụ:

    UP_List(item=39, expSup=25345.58, max=1.0, transaction={4: 0.66, 5: 0.48, 6: 0.49, ...})

Trong đó:

- `item=39`: mẫu chỉ chứa mặt hàng `39`.
- `expSup=25345.58`: độ hỗ trợ kỳ vọng của mặt hàng `39` trên toàn bộ cơ sở dữ liệu.
- `max=1.0`: xác suất tồn tại lớn nhất của mặt hàng `39` trong một giao dịch.
- `transaction={...}`: xác suất tồn tại của mặt hàng trong từng giao dịch tương ứng.

**Mẫu gồm nhiều mặt hàng - `IMCUP_List`**

Ví dụ:

    IMCUP_List(name=39, 48, expSup=7308.7, max=1.0, transaction={5: 0.4176, 6: 0.2058, 13: 0.1197, ...})

Trong đó:

- `name=39, 48`: mẫu gồm hai mặt hàng `{39, 48}`.
- `expSup=7308.7`: độ hỗ trợ kỳ vọng của mẫu `{39, 48}`.
- `max=1.0`: xác suất xuất hiện lớn nhất của mẫu trong một giao dịch.
- `transaction={...}`: xác suất xuất hiện đồng thời của mẫu trong từng giao dịch.

## Cấu trúc dự án

```

├── data/ // Chứa dữ liệu đầu vào
│ ├── example.txt   // Dữ liệu kiểm thử
│ └── retail.csv    // Dữ liệu chính thức
├── output/         // Chứa kết quả
│ ├── example.txt
│ └── retail.txt
├── papers/         // Tài liệu tham khảo
├── brute_force.py  // Giải thuật đơn giản để kiểm thử
├── ITUFP.ipynb     // Giải thuật chính
└── README.md

```

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
