#include <iostream>//头文件
/* int main(){
    std::cout<<"Hello world";
    return 0;
} */
//本例中，行参列表为空，main的返回类型必须为int，即整数类型。
//int 类型是一种内置类型

int main(){
    std :: cout <<"Enter two numbers:" << std::endl;
    //等同于std::cout << :"Enter two numbers";
    //     std :: cout << std::endl
    /*std::cout << "Enter:"; 这一行是给用户打印一条信息，
    std::cout << std::endl 这一行的endl时操纵符的特殊值，作用是结束当前行
                           并且将与设备关联的缓冲区中的内容刷到设备中。
    第一行，不会直接打印出来，而是先放到缓冲区，然后endl是冲刷缓冲区，我们才会看到
    std::endl不仅换行，还会强制刷新缓冲区，把数据立即输出*/
    int v1 = 0, v2 = 0;
    std :: cin >> v1 >> v2;
    std :: cout << "The sum of " << v1 << " and " << v2 << "is" 
    << v1 + v2 << std :: endl;
    return 0;
}