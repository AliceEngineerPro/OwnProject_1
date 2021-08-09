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

### Date对象

- 创建Date对象

```js
//方法1：不指定参数
var nowd1=new Date();
alert(nowd1.toLocaleString( ));
//方法2：参数为日期字符串
var nowd2=new Date("2004/3/20 11:12");
alert(nowd2.toLocaleString( ));
var nowd3=new Date("04/03/20 11:12");
alert(nowd3.toLocaleString( ));
//方法3：参数为毫秒数
var nowd3=new Date(5000);
alert(nowd3.toLocaleString( ));
alert(nowd3.toUTCString());

//方法4：参数为年月日小时分钟秒毫秒
var nowd4=new Date(2004,2,20,11,12,0,300);
alert(nowd4.toLocaleString( ));
//毫秒并不直接显示
```

- Date对象的方法—获取日期和时间

```shell
获取日期和时间
getDate()                 获取日
getDay ()                 获取星期
getMonth ()               获取月（0-11）
getFullYear ()            获取完整年份
getYear ()                获取年
getHours ()               获取小时
getMinutes ()             获取分钟
getSeconds ()             获取秒
getMilliseconds ()        获取毫秒
getTime ()                返回累计毫秒数(从1970/1/1午夜)
```

- 练习实例

```js
function getCurrentDate(){
        //1. 创建Date对象
        var date = new Date(); //没有填入任何参数那么就是当前时间
        //2. 获得当前年份
        var year = date.getFullYear();
        //3. 获得当前月份 js中月份是从0到11.
        var month = date.getMonth()+1;
        //4. 获得当前日
        var day = date.getDate();
        //5. 获得当前小时
        var hour = date.getHours();
        //6. 获得当前分钟
        var min = date.getMinutes();
        //7. 获得当前秒
        var sec = date.getSeconds();
        //8. 获得当前星期
        var week = date.getDay(); //没有getWeek
        // 2014年06月18日 15:40:30 星期三
        return year+"年"+changeNum(month)+"月"+day+"日 "+hour+":"+min+":"+sec+" "+parseWeek(week);
    }

alert(getCurrentDate());

//解决 自动补齐成两位数字的方法
    function changeNum(num){
    if(num < 10){
        return "0"+num;
    }else{
        return num;
    }

}
//将数字 0~6 转换成 星期日到星期六
    function parseWeek(week){
    var arr = ["星期日","星期一","星期二","星期三","星期四","星期五","星期六"];
    //             0      1      2      3 .............
    return arr[week];
}
```

- Date对象的方法—设置日期和时间

```js
//设置日期和时间
//setDate(day_of_month)       设置日
//setMonth (month)                 设置月
//setFullYear (year)               设置年
//setHours (hour)         设置小时
//setMinutes (minute)     设置分钟
//setSeconds (second)     设置秒
//setMillliseconds (ms)       设置毫秒(0-999)
//setTime (allms)     设置累计毫秒(从1970/1/1午夜)
    
var x=new Date();
x.setFullYear (1997);    //设置年1997
x.setMonth(7);        //设置月7
x.setDate(1);        //设置日1
x.setHours(5);        //设置小时5
x.setMinutes(12);    //设置分钟12
x.setSeconds(54);    //设置秒54
x.setMilliseconds(230);        //设置毫秒230
document.write(x.toLocaleString( )+"<br>");
//返回1997年8月1日5点12分54秒

x.setTime(870409430000); //设置累计毫秒数
document.write(x.toLocaleString( )+"<br>");
//返回1997年8月1日12点23分50秒
```

- Date对象的方法—日期和时间的转换

```shell
日期和时间的转换:

getTimezoneOffset():8个时区×15度×4分/度=480;
返回本地时间与GMT的时间差，以分钟为单位
toUTCString()
返回国际标准时间字符串
toLocalString()
返回本地格式时间字符串
Date.parse(x)
返回累计毫秒数(从1970/1/1午夜到本地时间)
Date.UTC(x)
返回累计毫秒数(从1970/1/1午夜到国际时间)
```

### RegExp对象

```js
//RegExp对象
    // 在表单验证时使用该对象验证用户填入的字符串是否符合规则.
    //创建正则对象方式1  参数1 正则表达式  参数2 验证模式  g global / i 忽略大小写. //参数2一般填写g就可以，也有“gi”.
    // 用户名 首字母必须是英文, 除了第一位其他只能是英文数字和_ . 长度最短不能少于6位 最长不能超过12位
    //----------------------------创建方式1
    /* var reg1 = new RegExp("^[a-zA-Z][a-zA-Z0-9_]{5,11}$","g");
    //
    //验证字符串
    var str = "bc123";
    alert(reg1.test(str));// true
    
    //----------------------------创建方式2  /填写正则表达式/匹配模式;
    var reg2 = /^[a-zA-Z][a-zA-Z0-9_]{5,11}$/g;
    
    alert(reg2.test(str));// true
     */
    //-------------------------------正则对象的方法-------------------
        //test方法  ==>  测试一个字符串是否复合 正则规则. 返回值是true 和false.
    
    //-------------------------String 中与正则结合的4个方法------------------.
    // macth search split replace
    var str = "hello world";
    
    //alert(str.match(/o/g)); //查找字符串中 复合正则的 内容.
    //alert(str.search(/h/g));// 0  查找字符串中符合正则表达式的内容位置
    //alert(str.split(/o/g)); // 按照正则表达式对字符串进行切割. 返回数组;
    alert(str.replace(/o/g, "s")); // hells wsrld  对字符串按照正则进行替换.
```

### Math对象

```js
//Math对象
    //该对象中的属性方法 和数学有关.
    //Math是内置对象 , 与Global的不同之处是, 在调用时 需要打出 "Math."前缀.
    //属性学习:
    //alert(Math.PI);
    //方法学习:
        //alert(Math.random()); // 获得随机数 0~1 不包括1.
        //alert(Math.round(1.5)); // 四舍五入
        //练习：获取1-100的随机整数，包括1和100
             //var num=Math.random();
            //num=num*10;
            //num=Math.round(num);
            // alert(num)
        //============max  min=========================
        /* alert(Math.max(1,2));// 2
        alert(Math.min(1,2));// 1 */
        //-------------pow--------------------------------
        alert(Math.pow(2,4));// pow 计算参数1 的参数2 次方.
        

```

```shell
abs(x)    返回数的绝对值。
exp(x)    返回 e 的指数。
floor(x)对数进行下舍入。
log(x)    返回数的自然对数（底为e）。
max(x,y)    返回 x 和 y 中的最高值。
min(x,y)    返回 x 和 y 中的最低值。
pow(x,y)    返回 x 的 y 次幂。
random()    返回 0 ~ 1 之间的随机数。
round(x)    把数四舍五入为最接近的整数。
sin(x)    返回数的正弦。
sqrt(x)    返回数的平方根。
tan(x)    返回角的正切。
```

### <font color=#ff000>Function 对象</font>

- 函数的定义

```shell
function 函数名 (参数){函数体;
    return 返回值;
}
```

- 功能说明
  - 可以使用变量、常量或表达式作为函数调用的参数
  - 函数由关键字function定义
  - 函数名的定义规则与标识符一致，大小写是敏感的
  - 返回值必须使用return

Function 类可以表示开发者定义的任何函数。用 Function 类直接创建函数的语法如下：

```shell
function 函数名 (参数){
    函数体;
   return 返回值;
}
//another way:
var 函数名 = new Function("参数1","参数n","function_body");
```

虽然由于字符串的关系，第二种形式写起来有些困难，但有助于理解函数只不过是一种引用类型，它们的行为与用 Function 类明确创建的函数行为是相同的。

```js
alert(1);
function func1(){
    alert('hello Jack!');
    return 8
}
 
    ret=func1();
    alert(ret);
 
var func1=new Function("name","alert(\"hello\"+name);")
func1("Jack")
```

#### Function 对象的 length 属性

如前所述，函数属于引用类型，所以它们也有属性和方法。

比如，ECMAScript 定义的属性 length 声明了函数期望的参数个数。

```js
alert(func1.length)
```

#### Function 对象的方法

Function 对象也有与所有对象共享的 valueOf() 方法和 toString() 方法。这两个方法返回的都是函数的源代码，在调试时尤其有用。

```js
alert(void(fun1(1,2)))
```

运算符void()作用：拦截方法的返回值　

#### 函数的调用

```js
function func1(a,b){

    alert(a+b);
}

    func1(1,2);  //3
    func1(1,2,3);//3
    func1(1);    //NaN
    func1();     //NaN

    //只要函数名写对即可,参数怎么填都不报错.


 function a(a,b){
    alert(a+b);
}

   var a=1;
   var b=2;
   a(a,b)
```

#### 函数的内置对象arguments

```js
function add(a,b){

        console.log(a+b);//3
        console.log(arguments.length);//2
        console.log(arguments);//[1,2]

    }
    add(1,2)

//  ------------------arguments的用处1 ------------------
    function nxAdd(){
        var result=0;
        for (var num in arguments){
            result+=arguments[num]
        }
        alert(result)

    }

    nxAdd(1,2,3,4,5)

//  ------------------arguments的用处2 ------------------

    function f(a,b,c){
        if (arguments.length!=3){
            throw new Error("function f called with "+arguments.length+" arguments,but it just need 3 arguments")
        }
        else {
            alert("success!")
        }
    }

    f(1,2,3,4,5)
```

#### 匿名函数

```js
// 匿名函数
    var func = function(arg){
        return "tony";
    }

// 匿名函数的应用
    (function(){
        alert("tony");
    } )()

    (function(arg){
        console.log(arg);
    })('123')
```

### <font color=ff0000>函数的作用域链和闭包</font>

#### 作用域

js的作用域和py相似，if while等控制语句并没有自己作用域；而函数是有自己的作用域的；

```js
if(1==1){
        var s=12;
    }
    console.log(s);//12

   // ----------------------
    function f(){
        var temp=666;
    }
    f();
    console.log(temp);//Uncaught ReferenceError: temp is not defined
```

#### 嵌套函数的作用域

```js
var city = 'beijing';

    function func(){
        var city = 'shanghai';
        function inner(){
            var city = 'shenzhen';
            console.log(city);
        }
        inner();
    }
    func();
```

```js
var city = 'beijing';
function Bar(){
    console.log(city);
}
function func(){

    var city = 'shanghai';
    return Bar;
}
var ret = func();
ret();    //beijing
```

#### 闭包

```js
var city = 'beijing';

function func(){
    var city = "shanghai";
    function inner(){
        // var city = "langfang";
        console.log(city);
    }
    return inner;
}
var ret = func();
ret();
```

#### 作用域链(Scope Chain)

在JavaScript中，函数也是对象，实际上，JavaScript里一切都是对象。函数对象和其它对象一样，拥有可以通过代码访问的属性和一系列仅供JavaScript引擎访问的内部属性。其中一个内部属性是[[Scope]]，由ECMA-262标准第三版定义，该内部属性包含了函数被创建的作用域中对象的集合，这个集合被称为函数的作用域链，它决定了哪些数据能被函数访问。

```js
var x=1;
function foo() {
    var y = 2;
    
    function bar() {
        var z = 3;
    }
}

// bar的作用域链： barScopeChain=[bar.AO, foo.AO, global.VO];
// foo的作用域链： fooScopeChain=[foo.Ao, global.VO];
```

- 什么是AO,VO?
  - 在函数创建时，每个函数都会创建一个活动对象Active Object(AO)，全局对象为Global Object(VO)，创建函数的过程也就是为这个对象添加属性的过程，作用域链就是由这些绑定了属性的活动对象构成的。例如：找x变量；bar函数在搜寻变量x的过程中，先从自身AO对象上找，如果bar.AO存在这个属性，那么会直接使用这个属性的值，如果不存在，则会转到父级函数的AO对象，也就是foo.AO如果找到x属性则使用，找不到继续 在global.VO对象查找，找到x的属性，返回属性值。如果在global.VO中没有找到，则会抛出异常ReferenceError

- 执行上下文
  - 函数在执行时会创建一个称为“执行上下文（execution context）”的内部对象，执行上下文定义了函数执行时的环境。每个执行上下文都有自己的作用域链，用于标识符解析，当执行上下文被创建时，而它的作用域链初始化为当前运行函数的[[Scope]]所包含的对象。

- 函数执行
  - 在函数执行过程中，每遇到一个变量，都会检索从哪里获取和存储数据，该过程从作用域链头部，也就是从活动对象开始搜索，查找同名的标识符，如果找到了就使用这个标识符对应的变量，如果没有则继续搜索作用域链中的下一个对象，如果搜索完所有对象都未找到，则认为该标识符未定义，函数执行过程中，每个标识符都要经历这样的搜索过程。

#### 创建作用域链的过程

```shell
函数进入全局，创建VO对象，绑定x属性<入栈>
global.VO={x=underfind; foo:reference of function}(这里只是预解析，为AO对象绑定声明的属性，函数执行时才会执行赋值语句，所以值是underfind)
遇到foo函数，创建foo.AO，绑定y属性<入栈>
foo.AO={y=underfind, bar:reference of function}
遇到bar函数，创建bar.AO，绑定z属性<入栈>
bar.AO={z:underfind}
作用域链和执行上下文都会保存在堆栈中，所以：
bar函数的scope chain为：[0]bar.AO-->[1]foo.AO-->[2]global.VO
foo函数的scope chain为：[0]foo.AO-->[1]global.Vo
//建议：少定义全局变量
//理由：因为作用域链是栈的结构，全局变量在栈底，每次访问全局变量都会遍历一次栈，//这样会影响效率
```

函数的scope等于自身的AO对象加上父级的scope，也可以理解为一个函数的作用域等于自身活动对象加上父级作用域.函数执行前后的作用域链

![SC_1](https://pic.amfc.ltd/learn/python/js/SC_1.png)

![SC_2](https://pic.amfc.ltd/learn/python/js/SC_2.png)

