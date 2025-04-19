import os

# 项目主目录
project_name = "Learn-Cpp"

# 要创建的文件夹结构
folders = [
    "00-基础语法",
    "01-流程控制",
    "02-函数与数组",
    "03-指针与引用",
    "04-类与对象",
    "05-STL标准库",
    "06-进阶专题",
    "notes"
]

# 初始文件内容
readme_content = '''# 📘 Learn-Cpp：我的 C++ 学习记录

这个项目用于记录我从零开始学习 C++ 的全过程，包括基础语法、进阶专题、代码练习和学习笔记等。

---

## 📚 学习路线（大纲）

1. 基础语法
2. 流程控制（条件、循环）
3. 函数与数组
4. 指针与引用
5. 面向对象：类与对象
6. STL 标准模板库
7. 智能指针、异常处理、lambda 表达式等进阶内容

---

## 📂 目录结构

| 文件夹 | 内容说明 |
|--------|----------|
| `00-基础语法/` | 最简单的 Hello World，变量、数据类型、输入输出等 |
| `01-流程控制/` | if、switch、for、while、do-while 等控制语句 |
| `02-函数与数组/` | 函数定义与调用、数组遍历 |
| `03-指针与引用/` | 指针基础、引用传参、指针与数组关系 |
| `04-类与对象/` | 类的定义、构造析构、继承、多态等 |
| `05-STL标准库/` | vector、map、set 等容器及算法 |
| `06-进阶专题/` | 智能指针、lambda 表达式、异常处理等 |
| `notes/` | 笔记和思维导图整理 |

---

## ✍️ 学习进度

- [x] 安装编译器
- [x] 输出 Hello World
- [ ] 熟练掌握流程控制
- [ ] 掌握类与对象
- [ ] 完成 STL 常用容器实践
'''

hello_world_code = '''#include <iostream>
using namespace std;

int main() {
    cout << "Hello, C++!" << endl;
    return 0;
}
'''

gitignore_content = '''# 忽略编译生成的可执行文件
*.exe
*.out
*.o
'''

# 开始创建目录和文件
def create_cpp_learning_repo():
    os.makedirs(project_name, exist_ok=True)

    for folder in folders:
        os.makedirs(os.path.join(project_name, folder), exist_ok=True)

    # 写入 README.md
    with open(os.path.join(project_name, "README.md"), "w", encoding="utf-8") as f:
        f.write(readme_content)

    # 写入 hello world 示例代码
    with open(os.path.join(project_name, "00-基础语法", "helloworld.cpp"), "w", encoding="utf-8") as f:
        f.write(hello_world_code)

    # 写入 .gitignore
    with open(os.path.join(project_name, ".gitignore"), "w", encoding="utf-8") as f:
        f.write(gitignore_content)

    # 创建一个空的学习路线笔记
    with open(os.path.join(project_name, "notes", "学习路线.md"), "w", encoding="utf-8") as f:
        f.write("# 学习路线\n\n- 基础语法\n- 面向对象\n- STL\n- 项目实践\n")

    print(f"✅ 项目“{project_name}”已成功创建！快去开始学习吧～")

# 执行
if __name__ == "__main__":
    create_cpp_learning_repo()
