# 八皇后问题求解器 - 人工智能导论作业01

本项目为《人工智能导论》课程作业，实现 N 皇后问题的回溯算法求解器，并通过 AI 协作完成代码编写、测试和调试。

## 实现思路

- **算法选择**：使用回溯法（Backtracking）逐行放置皇后
- **冲突检测**：检查列冲突和对角线冲突（通过斜率判断）
- **递归搜索**：遍历所有可能的放置位置，找到所有有效解

## 项目结构

```

hw01/
├── src/
│   ├── init.py
│   └── eight_queens.py
├── tests/
│   ├── init.py
│   └── test_eight_queens.py
├── README.md
└── prompt_log.md

```

## 运行方式

### 安装依赖
```bash
pip install pytest
```

运行求解器示例

```python
from src.eight_queens import solve_n_queens, print_solution

# 求解8皇后
solutions = solve_n_queens(8)
print(f"8皇后共有 {len(solutions)} 个解")

# 打印第一个解
print("\n第一个解：")
print_solution(solutions[0])
```

运行测试

```bash
# 在 hw01 目录下执行
pytest tests/ -v
```

测试结果验证

N 预期解的数量 实际解的数量 测试结果
4 2 2 ✅ 通过
8 92 92 ✅ 通过

AI协作过程

详细的AI交互记录请参考 prompt_log.md

作者

· 姓名：周子粤
· 学号：2025311872
· 日期：2026-03-10
