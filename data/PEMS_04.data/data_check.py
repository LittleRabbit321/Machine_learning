import numpy as np


def check_npz_file(file_path):
    try:
        npz_data = np.load(file_path)

        print(f"--- 成功加载文件: {file_path} ---")

        print(f"\n[1] 文件中包含 {len(npz_data.files)} 个数组，键名如下:")
        for key in npz_data.files:
            print(f"  - {key}")

        print("\n[2] 数组详细信息:")
        print("---------------------------------")

        for key in npz_data.files:
            array = npz_data[key]
            print(f"键 (Key): '{key}'")
            print(f"  形状 (Shape): {array.shape}")
            print(f"  数据类型 (Dtype): {array.dtype}")

            if array.ndim >= 2:

                print(f"  前 5x5 元素 (或前 5 行):\n{array[:5, :5] if array.ndim == 2 else array[0, :5, :]}")
            elif array.ndim == 1:
                print(f"  前 5 个元素:\n{array[:5]}")

            print("-" * 35)

    except FileNotFoundError:
        print(f"错误: 文件未找到。请检查路径: {file_path}")
    except Exception as e:
        print(f"读取文件时发生错误: {e}")

check_npz_file('pems04.npz')