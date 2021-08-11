# jQuery框架

## jQuery是什么

- jQuery是由美国人John Resig创建，至今已吸引了来自世界各地的众多 javascript高手加入其team。
- jQuery是继prototype之后又一个优秀的Javascript框架。其宗旨是——WRITE LESS,DO MORE!
- 它是轻量级的js库(压缩后只有21k) ，这是其它的js库所不及的，它兼容CSS3，还兼容各种浏览器
- jQuery是一个快速的，简洁的javaScript库，使用户能更方便地处理HTMLdocuments、events、实现动画效果，并且方便地为网站提供AJAX交互。
- jQuery还有一个比较大的优势是，它的文档说明很全，而且各种应用也说得很详细，同时还有许多成熟的插件可供选择。

## 什么是jQuery对象

jQuery 对象就是通过jQuery包装DOM对象后产生的对象。jQuery 对象是 jQuery 独有的. 如果一个对象是 jQuery 对象, 那么它就可以使用 jQuery 里的方法: $(“#test”).html();

```js
$("#test").html()    
       //意思是指：获取ID为test的元素内的html代码。其中html()是jQuery里的方法 

       // 这段代码等同于用DOM实现代码： document.getElementById(" test ").innerHTML; 

       //虽然jQuery对象是包装DOM对象后产生的，但是jQuery无法使用DOM对象的任何方法，同理DOM对象也不能使用jQuery里的方法.乱使用会报错

       //约定：如果获取的是 jQuery 对象, 那么要在变量前面加上$. 

var $variable = jQuery 对象
var variable = DOM 对象

$variable[0]：jquery对象转为dom对象      $("#msg").html(); $("#msg")[0].innerHTML
```

jquery的基础语法:**<font color = ff0000>$(selector).action()</font>**

## 寻找元素(选择器和筛选器) 

### 选择器

1. 基本选择器

`$("*")  $("#id")   $(".class")  $("element")  $(".class,p,div")`

2. 层级选择器 

`$(".outer div")  $(".outer>div")   $(".outer+div")  $(".outer~div")`

3. 基本筛选器

`$("li:first")  $("li:eq(2)")  $("li:even") $("li:gt(1)")`

4. <font color = ff0000>属性选择器</font>

`$('[id="div1"]')   $('["alex="sb"][id]')`

5. 表单选择器

`$("[type='text']")----->$(":text")`
`注意只适用于input标签  : $("input:checked")`

### 筛选器

1. 过滤筛选器

`$("li").eq(2)  $("li").first()  $("ul li").hasclass("test")`

2. <font color = ff0000>查找筛选器</font>

```js
$("div").children(".test")  // 子代标签
$("div").find(".test")  // 所有子代标签
$(".test").next()  // 下一个标签
$(".test").nextAll()  //之后所有标签
$(".test").nextUntil(".test1")  //从.test到.test1内的所有标签
$("div").prev()  //上一个标签
$("div").prevAll()  //之上的所有标签
$("div").prevUntil(".test")  //从.test到div的所有标签
$(".test").parent()  // 父代标签
$(".test").parents()  // 所有父代-->到<head>
$(".test").parentUntil(".test1")  // 从.test1到.test的所有父代
$("div").siblings()  //  所有兄弟标签
```

## 操作元素(属性，css，文档处理)

