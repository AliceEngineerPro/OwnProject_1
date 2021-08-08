# JavaScript运算符

## 算术运算符

```shell
加(＋)、 减(－)、 乘(*) 、除(/) 、余数(% )  加、减、乘、除、余数和数学中的运算方法一样  例如：9/2=4.5，4*5=20，9%2=1

-除了可以表示减号还可以表示负号  例如：x=-y

+除了可以表示加法运算还可以用于字符串的连接  例如："abc"+"def"="abcdef"
```

### 递增(＋＋) 、递减(－－)

```shell
假如x=2，那么x++表达式执行后的值为3，x--表达式执行后的值为1
i++相当于i=i+1，i--相当于i=i-1
递增和递减运算符可以放在变量前也可以放在变量后：--i
```

```javascript
var i=1;
console.log(i++);
console.log(++i);
console.log(i--);
console.log(--i);
```

### 一元加减法

```javascript
var a=1;
var b=1;
a=-a;  // a=-1
var c="10";
alert(typeof (c));
c=+c;  //类型转换
alert(typeof (c));
//------------------- 
var d="jack";
d=+d;
alert(d);  //NaN:属于Number类型的一个特殊值,当遇到将字符串转成数字无效时,就会得到一个NaN数据
alert(typeof(d));  //Number
// NaN特点:
var n=NaN;
alert(n>3);
alert(n<3);
alert(n==3);
alert(n==NaN);
alert(n!=NaN);  //NaN参与的所有的运算都是false,除了!=
```

## 逻辑运算符

```shell
等于(==) 不等于(!=) 大于(>) 小于(<) 大于等于(>=) 小于等于(<=)
与 (&&) 或(||) 非(!)
1 && 1 = 1
1 || 1 = 1
1 && 0 = 0
1 || 0 = 1
0 && 0 = 0
0 || 0 = 0

!0=1
!1=0
```

### 逻辑 AND 运算符(&&)

```shell
逻辑 AND 运算的运算数可以是任何类型的，不止是 Boolean 值。
如果某个运算数不是原始的 Boolean 型值，逻辑 AND 运算并不一定返回 Boolean 值：
    如果某个运算数是 null，返回 null。 
    如果某个运算数是 NaN，返回 NaN。 
    如果某个运算数是 undefined，返回 undefined。
```

### 逻辑 OR 运算符(||)

```shell
与逻辑 AND 运算符相似，如果某个运算数不是 Boolean 值，逻辑 OR 运算并不一定返回 Boolean 值
```

## 赋值运算符

```shell
赋值 = 
JavaScript中=代表赋值，两个等号==表示判断是否相等
例如，x=1表示给x赋值为1
if (x==1){...}程序表示当x与1相等时
if(x==“on”){…}程序表示当x与“on”相等时
配合其他运算符形成的简化表达式
例如i+=1相当于i=i+1，x&=y相当于x=x&y
```

## 等性运算符

```shell
执行类型转换的规则如下：

如果一个运算数是 Boolean 值，在检查相等性之前，把它转换成数字值。false 转换成 0，true 为 1。 
如果一个运算数是字符串，另一个是数字，在检查相等性之前，要尝试把字符串转换成数字。 
如果一个运算数是对象，另一个是字符串，在检查相等性之前，要尝试把对象转换成字符串。 
如果一个运算数是对象，另一个是数字，在检查相等性之前，要尝试把对象转换成数字。 
```

```shell
在比较时，该运算符还遵守下列规则：

值 null 和 undefined 相等。 
在检查相等性时，不能把 null 和 undefined 转换成其他值。 
如果某个运算数是 NaN，等号将返回 false，非等号将返回 true。 
如果两个运算数都是对象，那么比较的是它们的引用值。如果两个运算数指向同一对象，那么等号返回 true，否则两个运算数不等。 
```

![](https://pic.amfc.ltd/learn/python/js/%E7%AD%89%E6%80%A7%E8%BF%90%E7%AE%97%E7%AC%A6.png)

## <font color=##ff0000>关系运算符</font>

```javascript
var bResult = "Blue" < "alpha";
alert(bResult); //输出 true　
```

在上面的例子中，字符串 "Blue" 小于 "alpha"，因为字母 B 的字符代码是 66，字母 a 的字符代码是 97。

### 比较数字和字符串

另一种棘手的状况发生在比较两个字符串形式的数字时，比如：

```javascript
var bResult = "25" < "3";
alert(bResult); //输出 "true"
```

上面这段代码比较的是字符串 "25" 和 "3"。两个运算数都是字符串，所以比较的是它们的字符代码（"2" 的字符代码是 50，"3" 的字符代码是 51）。

不过，如果把某个运算数该为数字，那么结果就有趣了：

```javascript
var bResult = "25" < 3;
alert(bResult); //输出 "false"
```

这里，字符串 "25" 将被转换成数字 25，然后与数字 3 进行比较，结果不出所料。

**总结**:
>比较运算符两侧如果一个是数字类型,一个是其他类型,会将其类型转换成数字类型

> 比较运算符两侧如果都是字符串类型,比较的是最高位的asc码,如果最高位相等,继续取第二位比较.

## Boolean运算符

```javascript
var temp=new Object();// false;[];0; null; undefined;object(new Object();)

    if(temp){
        console.log("yuan")
    }
    else {
        console.log("alex")
    }
```

## 全等号和非全等号

等号和非等号的同类运算符是全等号和非全等号。这两个运算符所做的与等号和非等号相同，只是它们在检查相等性前，不执行类型转换。

