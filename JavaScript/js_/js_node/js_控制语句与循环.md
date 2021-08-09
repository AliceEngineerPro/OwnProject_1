# JavaScript控制语句与循环

## 控制语句

### if 控制语句

```shell
if-else基本格式
if (表达式){
语句１;
......
}else{
语句２;
.....
}
功能说明
如果表达式的值为true则执行语句1,
否则执行语句2
```

![控制语句1](https://pic.amfc.ltd/learn/python/js/%E6%8E%A7%E5%88%B6%E8%AF%AD%E5%8F%A5.png)

```javascript
var x= (new Date()).getDay();
//获取今天的星期值，0为星期天
var y;

if ( (x===6) || (x===0) ) {
y="周末";
}else{
y="工作日";
}

alert(y);

//等价于

y="工作日";
if ( (x===6) || (x===0) ) {
y="周末";
}
```

- if 可以单独使用

```shell
if语句嵌套格式

if (表达式1) {
    语句1;
}else if (表达式2){
    语句2;
}else if (表达式3){
    语句3;
} else{
    语句4;
}
```

![if嵌套](https://pic.amfc.ltd/learn/python/js/%E5%B5%8C%E5%A5%97if.png)

### switch 选择控制语句

```shell
switch基本格式
switch (表达式) {
    case 值1:语句1;break;
    case 值2:语句2;break;
    case 值3:语句3;break;
    default:语句4;
}
```

![switch控制语句](https://pic.amfc.ltd/learn/python/js/switch_1.png)

```javascript
var x = 4

switch(x){
case 1:y="星期一";    break;
case 2:y="星期二";    break;
case 3:y="星期三";    break;
case 4:y="星期四";    break;
case 5:y="星期五";    break;
case 6:y="星期六";    break;
case 7:y="星期日";    break;
default: y="未定义";}
```

### for 循环控制语句

```shell
for循环基本格式
for (初始化;条件;增量){
    语句1;
    ...
}
功能说明
实现条件循环，当条件成立时，执行语句1，否则跳出循环体
```

![for循环](https://pic.amfc.ltd/learn/python/js/for_1.png)

```javascript
for (var i=1;i<=7;i++){
    document.write("<H"+i+">hello</H "+i+"> ");
    document.write("<br>");
}
//  ----------------------------------------------
    var arr=[1,"hello",true]//var dic={"1":"111"}
    for (var j in arr){
        console.log(j)
        console.log(arr[j])
    }
```

### while循环控制语句

```shell
while循环基本格式
while (条件){
语句1；
...
}
功能说明
运行功能和for类似，当条件成立循环执行语句花括号{}内的语句，否则跳出循环
```

![while循环](https://pic.amfc.ltd/learn/python/js/while_1.png)

```js
var i=1;
while (i<=7) {
    document.write("<H"+i+">hello</H "+i+"> ");
    document.write("<br>");
    i++;
}
//循环输出H1到H7的字体大小
```

```javascript
/* sayhello是定义的函数名，前面必须加上function和空格*/
function sName() {
    var hellostr;
    var myname=prompt("请问您贵姓？","李");
    hellostr="您好，"+myname+'先生，欢迎进入"探索之旅"！';
    alert(hellostr);
    document.write(hellostr);
}
sName()
//这里是对前面定义的函数进行调用
```

### 异常处理

```javascript
try {
    //这段代码从上往下运行，其中任何一个语句抛出异常该代码块就结束运行
}
catch (e) {
    // 如果try代码块中抛出了异常，catch代码块中的代码就会被执行。
    //e是一个局部变量，用来指向Error对象或者其他抛出的对象
}
finally {
     //无论try中代码是否有异常抛出（甚至是try代码块中有return语句），finally代码块中始终会被执行。
}
```

