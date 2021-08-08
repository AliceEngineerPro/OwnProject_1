# JavaScript对象

从传统意义上来说，ECMAScript 并不真正具有类。事实上，除了说明不存在类，在 ECMA-262 中根本没有出现“类”这个词。ECMAScript 定义了“对象定义”，逻辑上等价于其他程序设计语言中的类。

```js
var o = new Object();
```

## 对象对的概念与分类

- 由ECMAScript定义的本地对象.独立于宿主环境的 ECMAScript 实现提供的对象.(native object)
- ECMAScript 实现提供的、独立于宿主环境的所有对象，在 ECMAScript 程序开始执行时出现.这意味着开发者不必明确实例化内置对象，它已被实例化了。ECMA-262 只定义了两个内置对象，即 Global 和 Math （它们也是本地对象，根据定义，每个内置对象都是本地对象）。（built-in object）
- 所有非本地对象都是宿主对象（host object），即由 ECMAScript 实现的宿主环境提供的对象。所有 BOM 和 DOM 对象都是宿主对象。

### object对象

ECMAScript 中的所有对象都由这个对象继承而来；Object 对象中的所有属性和方法都会出现在其他对象中

```shell
ToString() :  返回对象的原始字符串表示。
ValueOf()  : 返回最适合该对象的原始值。对于许多对象，该方法返回的值都与 ToString() 的返回值相同。
```

- <font color=#ff0000>**11种内置对象**</font>
  - Array
  - String 
  - Date
  - Math
  - Boolean
  - Number
  - Function
  - Global
  - Error
  - RegExp 
  - Object

**在JavaScript中除了null和undefined以外其他的数据类型都被定义成了对象，也可以用创建对象的方法定义变量，String、Math、Array、Date、RegExp都是JavaScript中重要的内置对象，在JavaScript程序大多数功能都是通过对象实现的**

```js
var aa=Number.MAX_VALUE; 
//利用数字对象获取可表示最大数
var bb=new String("hello JavaScript"); 
//创建字符串对象
var cc=new Date();
//创建日期对象
var dd=new Array("星期一","星期二","星期三","星期四"); 
//数组对象
```

![Object](https://pic.amfc.ltd/learn/python/js/obj_1.png)

### String对象

- 自动创建字符串对象

```js
var str1="hello world";
alert(str1.length);
alert(str1.substr(1,5));
```

调用字符串的对象属性或方法时自动创建对象，用完就丢弃

- 手工创建字符串对象

```js
var str1= new String("hello word");
alert(str1.length);
alert(str1.substr(1,3));
```

采用new创建字符串对象str1，<font color=#ff0000>全局有效</font>

<font color=#ff0000>**String对象的属性**</font>

```shell
获取字符串长度
length
```

```js
var str1="String对象";
var str2="";
alert("str1长度 "+str1.length);
alert("str2长度 "+str2.length);
```

1. String对象的方法(1)——格式编排方法

```js
var str_11 = 'hello';
console.log(str_11.italics());
console.log(str_11.bold());
console.log(str_11.anchor());
```

2. String对象的方法(2)——大小写转换

```js
var str1="AbcdEfgh"; 

var str2=str1.toLowerCase();
var str3=str1.toUpperCase();
alert(str2);
//结果为"abcdefgh"
alert(str3);
//结果为"ABCDEFGH"
```

3. String对象的方法(3)——获取指定字符

```js
var str1="welcome to the world of JS! Aa";

var str2=str1.charAt(28);
var str3=str1.charCodeAt(28);
alert(str2);
//结果为"A"
alert(str3);
//结果为65
```
4. String对象的方法(4)——查询字符串

```js
//书写格式
//
//x.indexOf(findstr,index)
//x.lastIndexOf(findstr)
//-------------------------------------
var str1="welcome to the world of JS!";

var str2=str1.indexOf("l");
var str3=str1.lastIndexOf("l");
alert(str2);
//结果为2
alert(str3);
//结果为18

//-------*********************************************************-------

//书写格式
//
//x.match(regexp)
//
//x.search(regexp)
//
//使用注解
//
//x代表字符串对象
//
//regexp代表正则表达式或字符串
//
//match返回匹配字符串的数组，如果没有匹配则返回null
//
//search返回匹配字符串的首字符位置索引
//-------------------------------------
var str1="welcome to the world of JS!";

var str2=str1.match("world");
var str3=str1.search("world");
alert(str2[0]);
//结果为"world"
alert(str3);
//结果为15
```
5. String对象的方法(5)——子字符串处理
  - 截取子字符串

```js
//截取子字符串
//
//书写格式
//
//x.substr(start, length)
//
//x.substring(start, end)
//
//使用注解
//
//x代表字符串对象
//
//start表示开始位置
//
//length表示截取长度
//
//end是结束位置加1
//
//第一个字符位置为0


var str1="abcdefgh";
var str2=str1.substr(2,4);
var str3=str1.substring(2,4);
alert(str2);
//结果为"cdef"
alert(str3);
//结果为"cd"

//-------**************************************-------
//x.slice(start, end)


var str1="abcdefgh";
var str2=str1.slice(2,4);
var str3=str1.slice(4);
var str4=str1.slice(2,-1);
var str5=str1.slice(-3,-1);
alert(str2);
//结果为"cd"
alert(str3);
//结果为"efgh"
alert(str4);
//结果为"cdefg"
alert(str5);
//结果为"fg"
```

  - 替换子字符串

```js
//x.replace(findstr,tostr)

var str1="abcdefgh";
var str2=str1.replace("cd","aaa");
alert(str2);
//结果为"abaaaefgh"
```

  - 分割字符串

```js
var str1="一,二,三,四,五,六,日"; 

var strArray=str1.split(",");

alert(strArray[1]);
//结果为"二"
```

  - 连接字符串

```js
//y=x.concat(addstr)
//
//使用注解
//
//x代表字符串对象
//addstr为添加字符串
//返回x+addstr字符串
    
var str1="abcd"; 
var str2=str1.concat("efgh");

alert(str2);
//结果为"abcdefgh"
```

### Array对象

- 创建数组对象

```shell
Array 对象用于在单个的变量中存储多个值。
语法:

创建方式1:
var a=[1,2,3];

创建方式2:
new Array();     //  创建数组时允许指定元素个数也可以不指定元素个数。
new Array(size);//if 1个参数且为数字,即代表size,not content
    初始化数组对象:
    var cnweek=new Array(7);
        cnweek[0]="星期日";
        cnweek[1]="星期一";
        ...
        cnweek[6]="星期六";

new Array(element0, element1, ..., elementn)//也可以直接在建立对象时初始化数组元素，元素类型允许不同

var test=new Array(100,"a",true);
```

- 创建二维数组

```shell
var cnweek=new Array(7);
for (var i=0;i<=6;i++){
    cnweek[i]=new Array(2);
}
cnweek[0][0]="星期日";
cnweek[0][1]="Sunday";
cnweek[1][0]="星期一";
cnweek[1][1]="Monday";
...
cnweek[6][0]="星期六";
cnweek[6][1]="Saturday";
```

- Array对象的属性
  - 获取数组元素的个数：length

```shell
var cnweek=new Array(7);
cnweek[0]="星期日";
cnweek[1]="星期一";
cnweek[2]="星期二";
cnweek[3]="星期三";
cnweek[4]="星期四";
cnweek[5]="星期五";
cnweek[6]="星期六";
for (var i=0;i<cnweek.length;i++){
  document.write(cnweek[i]+" | ");
}
```

- <font color="#ff0000">Array对象的方法</font>

![Array_1](https://pic.amfc.ltd/learn/python/js/Array_1.png)

![Array_2](https://pic.amfc.ltd/learn/python/js/Array_2.png)

- 连接数组-join方法

```js
//书写格式
//x.join(bystr)
//使用注解
//
//x代表数组对象
//bystr作为连接数组中元素的字符串
//返回连接后的字符串
//与字符串的split功能刚好相反
    
var arr1=[1, 2, 3, 4, 5, 6, 7];

var str1=arr1.join("-");

alert(str1);
//结果为"1-2-3-4-5-6-7"
```

- 连接数组-concat方法

```js
//连接数组-concat方法
//
//x.concat(value,...)


var a = [1,2,3];
var a = new Array(1,2,3);
var b=a.concat(4,5) ;


alert(a.toString());
//返回结果为1,2,3
alert(b.toString());
//返回结果为1,2,3,4,5
```

- 数组排序-reverse sort

```js
//x.reverse()
//x.sort()

var arr1=[32, 12, 111, 444];
//var arr1=["a","d","f","c"];

arr1.reverse(); //颠倒数组元素
alert(arr1.toString());
//结果为444,111,12,32

arr1.sort();    //排序数组元素
alert(arr1.toString());
//结果为111,12,32,444

//------------------------------
arr=[1,5,2,100];

//arr.sort();
//alert(arr);
//如果就想按着数字比较呢?

function intSort(a,b){
    if (a>b){
        return 1;//-1
    }
    else if(a<b){
        return -1;//1
    }
    else {
        return 0
    }
}

arr.sort(intSort);

alert(arr);

function IntSort(a,b){
    return a-b;
}
```

- 数组切片-slice

```js
//x.slice(start, end)
//
//使用注解
//
//x代表数组对象
//start表示开始位置索引
//end是结束位置下一数组元素索引编号
//第一个数组元素索引为0
//start、end可为负数，-1代表最后一个数组元素
//end省略则相当于从start位置截取以后所有数组元素

var arr1=['a','b','c','d','e','f','g','h'];
var arr2=arr1.slice(2,4);
var arr3=arr1.slice(4);
var arr4=arr1.slice(2,-1);

alert(arr2.toString());
//结果为"c,d" 
alert(arr3.toString());
//结果为"e,f,g,h"
alert(arr4.toString());
//结果为"c,d,e,f,g"
```

- 删除子数组

```js
//x. splice(start, deleteCount, value, ...)
//
//使用注解
//
//x代表数组对象
//splice的主要用途是对数组指定位置进行删除和插入
//start表示开始位置索引
//deleteCount删除数组元素的个数
//value表示在删除位置插入的数组元素
//value参数可以省略


var a = [1,2,3,4,5,6,7,8];
a.splice(1,2);
//a变为 [1,4,5,6,7,8]
alert(a.toString());
a.splice(1,1);
 //a变为[1,5,6,7,8]
alert(a.toString());
a.splice(1,0,2,3);
 //a变为[1,2,3,5,6,7,8]
alert(a.toString());
```

- 数组的进出栈操作(1)

```js
//push pop这两个方法模拟的是一个栈操作

//x.push(value, ...)  压栈
//x.pop()             弹栈      
//使用注解
//
//x代表数组对象
//value可以为字符串、数字、数组等任何值
//push是将value值添加到数组x的结尾
//pop是将数组x的最后一个元素删除


var arr1=[1,2,3];
arr1.push(4,5);
alert(arr1);
//结果为"1,2,3,4,5"
arr1.push([6,7]);
alert(arr1)
//结果为"1,2,3,4,5,6,7"
arr1.pop();
alert(arr1);
//结果为"1,2,3,4,5"
```

- 数组的进出栈操作(2)

```js
// unshift shift 
//x.unshift(value,...)
//x.shift()
//使用注解
//
//x代表数组对象
//value可以为字符串、数字、数组等任何值
//unshift是将value值插入到数组x的开始
//shift是将数组x的第一个元素删除

var arr1=[1,2,3];
arr1.unshift(4,5);
alert(arr1);
//结果为"4,5,1,2,3"
arr1. unshift([6,7]);
alert(arr1);
//结果为"6,7,4,5,1,2,3"
arr1.shift();
alert(arr1);
//结果为"4,5,1,2,3"
```

- <font color=#ff0000>总结js的数组特性</font>

```js
//  js中数组的特性
//  java中数组的特性,  规定是什么类型的数组,就只能装什么类型.只有一种类型.
//  js中的数组特性1: js中的数组可以装任意类型,没有任何限制.
//  js中的数组特性2: js中的数组,长度是随着下标变化的.用到多长就有多长.
var arr5 = ['abc',123,1.14,true,null,undefined,new String('1213'),new Function('a','b','alert(a+b)')];
/*  
alert(arr5.length);//8
arr5[10] = "hahaha";
alert(arr5.length); //11
alert(arr5[9]);// undefined 
*/
```