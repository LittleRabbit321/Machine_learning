import pickle
import numpy as np
file_path = './adj_mx.pkl'
try:
    with open(file_path, 'rb') as f:
        adj_mx = pickle.load(f)

    print(f"--- 文件: {file_path} ---")
    print(f"数据类型: {type(adj_mx)}")
    print(f"数据形状 (Shape): {adj_mx.shape}")

    print("\n--- 前 5x5 元素 (局部) ---")
    print(adj_mx[:5, :5])

    non_zero_count = np.count_nonzero(adj_mx)
    total_elements = adj_mx.size

    if non_zero_count > 0:
        sparsity = (1.0 - non_zero_count / total_elements) * 100
        print("\n--- 全局连接信息 ---")
        print(f"非零元素总数 (即边数): {non_zero_count}")
        print(f"非零元素的最小值: {np.min(adj_mx[np.nonzero(adj_mx)])}")
        print(f"非零元素的最大值: {np.max(adj_mx)}")
        print(f"矩阵稀疏度: {sparsity:.2f}% (连接越少，稀疏度越高)")

        first_nonzero = np.argwhere(adj_mx > 0)
        if first_nonzero.size > 0:
            i, j = first_nonzero[0]
            print(f"第一个非零元素位置: ({i}, {j})")
            print(f"该位置的值: {adj_mx[i, j]}")
    else:
        print("\n!!! 警告: 矩阵中没有发现非零元素。请检查文件内容是否正确。")

except Exception as e:
    print(f"读取 {file_path} 时发生错误: {e}")