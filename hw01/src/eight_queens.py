"""
八皇后问题求解器
使用回溯法实现
"""

def solve_n_queens(n: int):
    """
    解决N皇后问题，返回所有解
    
    参数:
        n: 棋盘大小
    
    返回:
        list: 所有解的列表，每个解是一个列表，表示每行皇后所在的列
    """
    def is_safe(board, row, col):
        """检查在(row, col)位置放置皇后是否安全"""
        for i in range(row):
            # 检查列冲突和对角线冲突
            if board[i] == col or \
               abs(board[i] - col) == abs(i - row):
                return False
        return True
    
    def backtrack(board, row):
        """回溯搜索"""
        if row == n:
            # 找到一个解，保存副本
            result.append(board[:])
            return
        
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(board, row + 1)
                board[row] = -1  # 回溯
    
    result = []
    backtrack([-1] * n, 0)
    return result


def print_solution(solution):
    """
    将解打印成棋盘格式
    
    参数:
        solution: 每行皇后所在的列列表
    """
    n = len(solution)
    for col in solution:
        row_str = ['.'] * n
        row_str[col] = 'Q'
        print(' '.join(row_str))
    print()


def format_solution(solution):
    """
    将解格式化为字符串列表
    
    参数:
        solution: 每行皇后所在的列列表
    
    返回:
        list: 每个字符串代表一行棋盘
    """
    n = len(solution)
    board = []
    for col in solution:
        row_str = ['.'] * n
        row_str[col] = 'Q'
        board.append(''.join(row_str))
    return board


def is_valid_solution(solution):
    """
    验证一个解是否合法
    
    参数:
        solution: 每行皇后所在的列列表
    
    返回:
        bool: 是否合法
    """
    n = len(solution)
    for i in range(n):
        for j in range(i + 1, n):
            # 检查同一列
            if solution[i] == solution[j]:
                return False
            # 检查对角线
            if abs(solution[i] - solution[j]) == abs(i - j):
                return False
    return True


if __name__ == "__main__":
    # 测试4皇后
    print("4皇后问题：")
    solutions_4 = solve_n_queens(4)
    print(f"共有 {len(solutions_4)} 个解")
    print("第一个解：")
    print_solution(solutions_4[0])
    
    # 测试8皇后
    print("8皇后问题：")
    solutions_8 = solve_n_queens(8)
    print(f"共有 {len(solutions_8)} 个解")
