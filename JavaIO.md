# 牛客Java范例

```java
// 导包
import java.util.Scanner;
// 主类，Main
public Class Main{
    // 主方法
    public static void main(String[] args){
        // Scanner类
        Scanner in = new Scanner(System.in);
        while( in.hasNextInt() ){ // 注意while处理多个int
            int a = in.nextInt();
            int b = in.nextInt();
            System.out.println(a + b);
        }
    }
}
```

