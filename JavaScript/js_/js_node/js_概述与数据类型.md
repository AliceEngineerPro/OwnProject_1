# JavaScript概述和数据类型

## 1. JavaScript概述

### JavaScript历史

- 1992年Nombas开发出C-minus-minus(C--)的嵌入式脚本语言(最初绑定在CEnvi软件中).后将其改名ScriptEase.(客户端执行的语言)
- Netscape(网景)接收Nombas的理念,(Brendan Eich)在其Netscape Navigator 2.0产品中开发出一套livescript的脚本语言.Sun和Netscape共同完成.后改名叫Javascript
- 微软随后模仿在其IE3.0的产品中搭载了一个JavaScript的克隆版叫Jscript.
- 为了统一三家,ECMA(欧洲计算机制造协会)定义了ECMA-262规范.国际标准化组织及国际电工委员会（ISO/IEC）也采纳 ECMAScript 作为标准（ISO/IEC-16262）。从此，Web 浏览器就开始努力（虽然有着不同的程度的成功和失败）将 ECMAScript 作为 JavaScript 实现的基础。EcmaScript是规范.

### ECMAScript

尽管 ECMAScript 是一个重要的标准，但它并不是 JavaScript 唯一的部分，当然，也不是唯一被标准化的部分。实际上，一个完整的 JavaScript 实现是由以下 3 个不同部分组成的：  
- 核心（ECMAScript）
- 文档对象模型（DOM） Document object model (整合js，css，html)
- 浏览器对象模型（BOM） Broswer object model（整合js和浏览器）
- Javascript 在开发中绝大多数情况是基于对象的.也是面向对象的.
![](https://pic.amfc.ltd/learn/python/js/js_1.png)

简单地说，ECMAScript 描述了以下内容：
- 语法
- 类型
- 语句
- 关键字
- 保留字
- 运算符
- 对象 (封装 继承 多态) 基于对象的语言.使用对象.

```javascript
// 直接编写
    <script>
        alert('hello world')
    </script>
// 导入文件
<script src="hello.js"></script>　
```
## 2. JavaScript基础
### 变量
```javascript
x = 1
y = 2
sum = x + y
alert(sum)
```
在代数中，我们使用字母（比如 x）来保存值  
通过上面的表达式 z=x+y，我们能够计算出 z 的值为3  
在 JavaScript 中，这些字母被称为变量  
- 0 变量是弱类型的(很随便)  
- 1 声明变量时不用声明变量类型. 全都使用var关键字  

```javascript
var a;
```
- 2 一行可以声明多个变量.并且可以是不同类型
```javascript
var name="jack", age=20, job="doctor";
```

- 3 (了解) 声明变量时 可以不用var. 如果不用var 那么它是全局变量.
- 4 变量命名,首字符只能是字母,下划线,$美元符 三选一，且区分大小写，x与X是两个变量
- 5 变量还应遵守以下某条著名得命名规则

```javascript
/*Camel 标记法
首字母是小写的，接下来的字母都以大写字符开头。例如：*/
var myTestValue = 0, mySecondValue = "hi";
/*Pascal 标记法
首字母是大写的，接下来的字母都以大写字符开头。例如：*/
var MyTestValue = 0, MySecondValue = "hi";
/*匈牙利类型标记法
在以 Pascal 标记法命名的变量前附加一个小写字母（或小写字母序列），说明该变量的类型。例如，i 表示整数，s 表示字符串，如下所示“*/
var iMyTestValue = 0, sMySecondValue = "hi";
```

### 基础规范
1. 每行结束可以不加分号. 没有分号会以换行符作为每行的结束

```javascript
a=1;b=2;
// a=1 b=2; //错误

a=1
b=2

//推荐
a=1;
b=2;

{
 a=1;
 b=2;
    //推荐加tab
    a=1;
    b=2;
}
```

2. 注释 支持多行注释(块注释)和单行注释(行注释). /* */  //
3. 使用{}来封装代码块

### 常量和标识符

- 常量
    - 直接在程序中出现的数据值

- 标识符
    1. 由不以数字开头的字母、数字、下划线(_)、美元符号($)组成
    2. 常用于表示函数、变量等的名称
    3. 例如：_abc,$abc,abc,abc123是标识符，而1abc不是
    4. JavaScript语言中代表特定含义的词称为保留字，不允许程序再定义为标识符

![](https://pic.amfc.ltd/learn/python/js/js_key_words.png)

![](https://pic.amfc.ltd/learn/python/js/js_%E4%BF%9D%E7%95%99%E5%AD%97.png)

### 数据类型

![](https://pic.amfc.ltd/learn/python/js/js_data_type.png)

![](https://pic.amfc.ltd/learn/python/js/js_data_type2.png)

#### 数字类型(Number)

```shell
简介  
最基本的数据类型  
不区分整型数值和浮点型数值  
所有数字都采用64位浮点格式存储，相当于Java和C语言中的double格式  
能表示的最大值是±1.7976931348623157 x 10308  
能表示的最小值是±5 x 10 -324
整型
    在JavaScript中10进制的整数由数字的序列组成
    精确表达的范围是-9007199254740992(-253)到 9007199254740992 (253)
    超出范围的整数，精确度将受影响
浮点数
    使用小数点记录数据
    例如：3.4，5.6
    使用指数记录数据
    例如：4.3e23 = 4.3 x 1023
16进制和8进制(16-->0x, 8-->0)
    16进制数据前面加上0x，八进制前面加0
    16进制数是由0-9,A-F等16个字符组成
    8进制数由0-7等8个数字组成
    16进制和8进制与2进制的换算
```

#### 字符串(String)

```shell
简介
    是由Unicode字符、数字、标点符号组成的序列
    字符串常量首尾由单引号或双引号括起
    JavaScript中没有字符类型
    常用特殊字符在字符串中的表达
    字符串中部分特殊字符必须加上右划线\
    常用的转义字符 \n:换行  \':单引号   \":双引号  \\:右划线
```

Srting数据类型的使用
- 特殊字符的使用方法和效果
- Unicode的插入方法

```javascript
<script>
        var str="\u4f60\u597d\n欢迎来到\"JavaScript世界\"";
        alert(str);
</script>
```

#### 布尔型(Boolean)

```shell
简介
Boolean类型仅有两个值：true和false，也代表1和0，实际运算中true=1,false=0
布尔值也可以看作on/off、yes/no、1/0对应true/false
Boolean值主要用于JavaScript的控制语句，例如
    if (x==1){
    y=y+1;
    }
    else {
    y=y-1;
    }
```

#### Null & Undefined

```shell
Undefined 类型
Undefined 类型只有一个值，即 undefined。当声明的变量未初始化时，该变量的默认值是 undefined。
当函数无明确返回值时，返回的也是值 "undefined";
```

```shell
Null 类型 -->针对对象
另一种只有一个值的类型是 Null，它只有一个专用值 null，即它的字面量。值 undefined 实际上是从值 null 派生来的，因此 ECMAScript 把它们定义为相等的。
尽管这两个值相等，但它们的含义不同。undefined 是声明了变量但未对其初始化时赋予该变量的值，null 则用于表示尚未存在的对象（在讨论 typeof 运算符时，简单地介绍过这一点）。如果函数或方法要返回的是对象，那么找不到该对象时，返回的通常是 null。

var person=new Person()
var person=null
```

#### 数据类型转换

```shell
JavaScript属于松散类型的程序语言
变量在声明的时候并不需要指定数据类型
变量只有在赋值的时候才会确定数据类型
表达式中包含不同类型数据则在计算过程中会强制进行类别转换
数字 + 字符串：数字转换为字符串
数字 + 布尔值：true转换为1，false转换为0
字符串 + 布尔值：布尔值转换为字符串true或false
```

#### 强制类型转换函数

```shell
函数parseInt：   强制转换成整数   例如parseInt("6.12")=6  ; parseInt(“12a")=12 ; parseInt(“a12")=NaN  ;parseInt(“1a2")=1
函数parseFloat： 强制转换成浮点数  parseFloat("6.12")=6.12
函数eval：       将字符串强制转换为表达式并返回结果 eval("1+1")=2 ; eval("1<2")=true

NAN: not a number 属于number的数据类型一种
console.log(parseInt('abc1234'))
console.log(parseInt('hello'))
```

#### 类型查询函数(typeof)

```shell
函数typeof ：查询数值当前类型(string / number / boolean / object )
例如typeof("test"+3)      "string"
例如typeof(null)          "object "
例如typeof(true+1)        "number"
例如typeof(true-false)    "number"

console.log(typeof 123)---------------->number
console.log(typeof '123')-------------->string
console.log(typeof null)--------------->object
console.log(typeof true)--------------->boolean
console.log(typeof undefined)---------->undefined
console.log(typeof [1, 2, 3])---------->object
console.log(typeof {'name': 'Jack'})--->object
```
