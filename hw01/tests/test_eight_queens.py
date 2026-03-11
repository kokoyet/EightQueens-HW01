"""
八皇后问题的单元测试
"""
import pytest
from src.eight_queens import solve_n_queens, is_valid_solution

def test_four_queens_count():
    """测试4皇后解的个数是否为2"""
    solutions = solve_n_queens(4)
    assert len(solutions) == 2, f"4皇后应该有2个解，但得到了{len(solutions)}个"

def test_eight_queens_count():
    """测试8皇后解的个数是否为92"""
    solutions = solve_n_queens(8)
    assert len(solutions) == 92, f"8皇后应该有92个解，但得到了{len(solutions)}个"

def test_one_queen():
    """测试1皇后"""
    solutions = solve_n_queens(1)
    assert len(solutions) == 1, "1皇后应该有1个解"

def test_two_queens():
    """测试2皇后（无解）"""
    solutions = solve_n_queens(2)
    assert len(solutions) == 0, "2皇后应该有0个解"

def test_three_queens():
    """测试3皇后（无解）"""
    solutions = solve_n_queens(3)
    assert len(solutions) == 0, "3皇后应该有0个解"

def test_solution_validity():
    """测试所有解是否真的合法"""
    for n in [4, 8]:
        solutions = solve_n_queens(n)
        for i, sol in enumerate(solutions):
            assert is_valid_solution(sol), f"{n}皇后的第{i+1}个解不合法: {sol}"

def test_solution_format():
    """测试解的长度是否正确"""
    for n in [4, 8]:
        solutions = solve_n_queens(n)
        for sol in solutions:
            assert len(sol) == n, f"解的长度应该是{n}，但得到{len(sol)}"
