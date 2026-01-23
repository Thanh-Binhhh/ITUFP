from itertools import chain, combinations

# Hàm tạo các tập con từ tập hợp các mục
def generate_subsets(items):
    return chain.from_iterable(combinations(items, r) for r in range(1, len(items) + 1))

# Hàm tính xác suất xuất hiện của một tập mẫu trong giao dịch
def calculate_pattern_probability(pattern, transaction_items, transaction_probs):
    prob = 1.0
    for item in pattern:
        if item in transaction_items:
            prob *= transaction_probs[transaction_items.index(item)]
        else:
            return 0  # Nếu một mục không tồn tại trong giao dịch => xác suất là 0
    return prob

# Brute force tìm Top-k UFPs
def brute_force_top_k_UFPs(matrix, headers, k):
    transactions = []
    # Chuyển ma trận thành danh sách giao dịch uncertain
    for row in matrix:
        items = [headers[i] for i in range(len(row)) if row[i] > 0]
        probabilities = [row[i] for i in range(len(row)) if row[i] > 0]
        transactions.append({'items': items, 'probabilities': probabilities})
    
    # Tạo tất cả các tập con từ các mục
    all_items = headers
    subsets = list(generate_subsets(all_items))
    pattern_frequencies = {}

    for subset in subsets:
        pattern_freq = 0
        for transaction in transactions:
            pattern_freq += calculate_pattern_probability(subset, transaction['items'], transaction['probabilities'])
        pattern_frequencies[frozenset(subset)] = pattern_freq

    # Sắp xếp theo tần suất giảm dần và lấy Top-k
    sorted_patterns = sorted(pattern_frequencies.items(), key=lambda x: x[1], reverse=True)

    # Trả về Top-k
    return sorted_patterns[:k]

# Dữ liệu
matrix = [
    [1.0, 0, 0.9, 0.6, 0, 0, 0, 0],
    [0.9, 0.9, 0.7, 0.6, 0.4, 0, 0, 0],
    [0, 0.5, 0.8, 0.9, 0, 0.2, 0.4, 0],
    [0, 0, 0.9, 0, 0.1, 0.5, 0, 0.8],
    [0.4, 0.5, 0.9, 0.3, 0, 0, 0.3, 0.3],
    [0, 0, 0, 0.9, 0.1, 0.6, 0, 0.3],
    [0.9, 0.7, 0.4, 0.6, 0, 0.9, 0, 0]
]
headers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# Tìm Top-3 UFPs
k = 50
result = brute_force_top_k_UFPs(matrix, headers, k)

# In kết quả
i = 1
for pattern, freq in result:
    print(f"{i}.  Pattern: {set(pattern)}, Frequency: {freq:.4f}")
    i += 1
