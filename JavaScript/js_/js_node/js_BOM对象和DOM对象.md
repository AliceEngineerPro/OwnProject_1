# BOM对象

BOM（浏览器对象模型），可以对浏览器窗口进行访问和操作。使用 BOM，开发者可以移动窗口、改变状态栏中的文本以及执行其他与页面内容不直接相关的动作。

使 JavaScript 有能力与浏览器“对话”。

## window对象

```shell
window对象
    所有浏览器都支持 window 对象。
    概念上讲.一个html文档对应一个window对象.
    功能上讲: 控制浏览器窗口的.
    使用上讲: window对象不需要创建对象,直接使用即可.
```

### Window 对象方法

```shell
alert()            显示带有一段消息和一个确认按钮的警告框。
confirm()          显示带有一段消息以及确认按钮和取消按钮的对话框。
prompt()           显示可提示用户输入的对话框。
open()             打开一个新的浏览器窗口或查找一个已命名的窗口。
close()            关闭浏览器窗口。
setInterval()      按照指定的周期（以毫秒计）来调用函数或计算表达式。
clearInterval()    取消由 setInterval() 设置的 timeout。
setTimeout()       在指定的毫秒数后调用函数或计算表达式。
clearTimeout()     取消由 setTimeout() 方法设置的 timeout。
scrollTo()         把内容滚动到指定的坐标。
```

#### 交互方法

```shell
方法讲解:    
        //----------alert confirm prompt----------------------------
    //alert('aaa');
    
    
    /* var result = confirm("您确定要删除吗?");
    alert(result); */

    //prompt 参数1 : 提示信息.   参数2:输入框的默认值. 返回值是用户输入的内容.

    // var result = prompt("请输入一个数字!","haha");
    // alert(result);



    方法讲解:    
        //open方法 打开和一个新的窗口 并 进入指定网址.参数1 : 网址.
        //调用方式1
            //open("http://www.baidu.com");
        //参数1 什么都不填 就是打开一个新窗口.  参数2.填入新窗口的名字(一般可以不填). 参数3: 新打开窗口的参数.
            open('','','width=200,resizable=no,height=100'); // 新打开一个宽为200 高为100的窗口
        //close方法  将当前文档窗口关闭.
            //close();
```

#### 练习

```js
var num = Math.round(Math.random()*100);
function acceptInput(){
//2.让用户输入(prompt)    并接受 用户输入结果
var userNum = prompt("请输入一个0~100之间的数字!","0");
//3.将用户输入的值与 随机数进行比较
        if(isNaN(+userNum)){
            //用户输入的无效(重复2,3步骤)
            alert("请输入有效数字!");
            acceptInput();
        }
        else if(userNum > num){
        //大了==> 提示用户大了,让用户重新输入(重复2,3步骤)
            alert("您输入的大了!");
            acceptInput();
        }else if(userNum < num){
        //小了==> 提示用户小了,让用户重新输入(重复2,3步骤)
            alert("您输入的小了!");
            acceptInput();
        }else{
        //答对了==>提示用户答对了 , 询问用户是否继续游戏(confirm).
            var result = confirm("恭喜您!答对了,是否继续游戏?");
            if(result){
                //是 ==> 重复123步骤.
                num = Math.round(Math.random()*100);
                acceptInput();
            }else{
                //否==> 关闭窗口(close方法).
                close();
            }
        }
}
```

#### setInterval clearInterval

```html
<input id="ID1" type="text" onclick="begin()">
<button onclick="end()">停止</button>

<script>


    function showTime(){
           var nowd2=new Date().toLocaleString();
           var temp=document.getElementById("ID1");
           temp.value=nowd2;

    }

    var clock;

    function begin(){

        if (clock==undefined){

             showTime();
             clock=setInterval(showTime,1000);

        }

    }

    function end(){

        clearInterval(clock);
    }

</script>
```

#### setTimeout clearTimeout

```js
var ID = setTimeout(abc,2000); // 只调用一次对应函数.
            clearTimeout(ID);
    function abc(){
        alert('aaa');
    }
```

## History 对象

### History 对象属性

History 对象包含用户（在浏览器窗口中）访问过的 URL。

History 对象是 window 对象的一部分，可通过 window.history 属性对其进行访问。

>length  返回浏览器历史列表中的 URL 数量。

### History 对象方法

>back()    加载 history 列表中的前一个 URL。
> 
>forward()    加载 history 列表中的下一个 URL。
> 
>go()    加载 history 列表中的某个具体页面。

```html
<a href="rrr.html">click</a>
<button onclick=" history.forward()">>>></button>
<button onclick="history.back()">back</button>
<button onclick="history.go()">back</button>
```

## Location 对象

Location 对象包含有关当前 URL 的信息。

Location 对象是 Window 对象的一个部分，可通过 window.location 属性来访问。

### Location 对象方法

```shell
location.assign(URL)
location.reload()
location.replace(newURL)//注意与assign的区别
```

# DOM对象(DHTML)

## 什么是 DOM？

DOM 是 W3C（万维网联盟）的标准。DOM 定义了访问 HTML 和 XML 文档的标准：

"W3C 文档对象模型（DOM）是中立于平台和语言的接口，它允许程序和脚本动态地访问和更新文档的内容、结构和样式。"

W3C DOM 标准被分为 3 个不同的部分：

- 核心 DOM - 针对任何结构化文档的标准模型
- XML DOM - 针对 XML 文档的标准模型
- HTML DOM - 针对 HTML 文档的标准模型

## DOM 节点 

根据 W3C 的 HTML DOM 标准，HTML 文档中的所有内容都是节点(NODE)：

- 整个文档是一个文档节点(document对象)
- 每个 HTML 元素是元素节点(element 对象)
- HTML 元素内的文本是文本节点(text对象)
- 每个 HTML 属性是属性节点(attribute对象)
- 注释是注释节点(comment对象)

画dom树是为了展示文档中各个对象之间的关系，用于对象的导航。

![](https://pic.amfc.ltd/learn/python/js/DOM_1.png)

- 节点(自身)属性
  - attributes - 节点（元素）的属性节点
  - nodeType – 节点类型
  - nodeValue – 节点值
  - nodeName – 节点名称
  - innerHTML - 节点（元素）的文本值
- 导航属性
  - parentNode - 节点（元素）的父节点 (推荐)
  - firstChild – 节点下第一个子元素
  - lastChild – 节点下最后一个子元素
  - childNodes - 节点（元素）的子节点 

<font color=#ff0000>注意：</font>

```shell
<div id="div1">
    <div id="div2"></div>
    <p>hello yuan</p>
</div>

<script>
    var div=document.getElementById("div2");

    console.log(div.nextSibling.nodeName);  //思考:为什么不是P?
</script>
```

<font color=#ff0000>推荐导航属性：</font>

```shell
parentElement              // 父节点标签元素

children                        // 所有子标签
  
firstElementChild          // 第一个子标签元素

lastElementChild           // 最后一个子标签元素

nextElementtSibling       // 下一个兄弟标签元素

previousElementSibling  // 上一个兄弟标签元素
```

节点树中的节点彼此拥有层级关系。

父(parent),子(child)和同胞(sibling)等术语用于描述这些关系。父节点拥有子节点。同级的子节点被称为同胞（兄弟或姐妹）。

- 在节点树中，顶端节点被称为根（root）
- 每个节点都有父节点、除了根（它没有父节点）
- 一个节点可拥有任意数量的子
- 同胞是拥有相同父节点的节点

![](https://pic.amfc.ltd/learn/python/js/%E8%8A%82%E7%82%B9_1.png)

访问 HTML 元素（节点）,访问 HTML 元素等同于访问节点,我们能够以不同的方式来访问 HTML 元素：

页面查找：

- 通过使用 getElementById() 方法 
- 通过使用 getElementsByTagName() 方法 
- 通过使用 getElementsByClassName() 方法 
- 通过使用 getElementsByName() 方法 

局部查找：

```html
<div id="div1">

    <div class="div2">i am div2</div>
    <div name="yuan">i am div2</div>
    <div id="div3">i am div2</div>
    <p>hello p</p>
</div>

<script>

   var div1=document.getElementById("div1");

////支持;
//   var ele= div1.getElementsByTagName("p");
//   alert(ele.length);
////支持
//   var ele2=div1.getElementsByClassName("div2");
//   alert(ele2.length);
////不支持
//   var ele3=div1.getElementById("div3");
//   alert(ele3.length);
////不支持
//   var ele4=div1.getElementsByName("yuan");
//   alert(ele4.length)

</script>
```

# HTML DOM Event(事件)

HTML 4.0 的新特性之一是有能力使 HTML 事件触发浏览器中的动作（action），比如当用户点击某个 HTML 元素时启动一段 JavaScript。下面是一个属性列表，这些属性可插入 HTML 标签来定义事件动作。

```shell
onclick        当用户点击某个对象时调用的事件句柄。
ondblclick     当用户双击某个对象时调用的事件句柄。

onfocus        元素获得焦点。               //练习：输入框
onblur         元素失去焦点。               应用场景：用于表单验证,用户离开某个输入框时,代表已经输入完了,我们可以对它进行验证.
onchange       域的内容被改变。             应用场景：通常用于表单元素,当元素内容被改变时触发.（三级联动）

onkeydown      某个键盘按键被按下。          应用场景: 当用户在最后一个输入框按下回车按键时,表单提交.
onkeypress     某个键盘按键被按下并松开。
onkeyup        某个键盘按键被松开。
onload         一张页面或一幅图像完成加载。
onmousedown    鼠标按钮被按下。
onmousemove    鼠标被移动。
onmouseout     鼠标从某元素移开。
onmouseover    鼠标移到某元素之上。onmouseleave   鼠标从元素离开

onselect      文本被选中。
onsubmit      确认按钮被点击。
```

## 两种为元素附加事件属性的方式

```js
<div onclick="alert(123)">点我呀</div>
<p id="abc">试一试!</p>

<script>
    var ele=document.getElementById("abc");


    ele.onclick=function(){
        alert("hi");
    };

</script>
```

<font color=#ff0000>注意</font>

```js
<div id="abc" onclick="func1(this)">事件绑定方式1</div>
<div id="id123">事件绑定方式2</div>
<script>
    function func1(self){
        console.log(self.id)
    }

    //jquery下是$(self), 这种方式this参数必须填写;

//------------------------------------------
    var ele=document.getElementById("id123").onclick=function(){
         console.log(this.id);
        //jquery下是$(this), 这种方式不需要this参数;
    }
    
</script>
```

## onload：

onload 属性开发中 只给 body元素加.

这个属性的触发 标志着 页面内容被加载完成.

应用场景: 当有些事情我们希望页面加载完立刻执行,那么可以使用该事件属性.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>

    <script>
//          window.onload=function(){
//               var ele=document.getElementById("ppp");
//               ele.onclick=function(){
//                alert(123)
//            };
//          };



          function fun1() {
              var ele=document.getElementById("ppp");
               ele.onclick=function(){
                alert(123)
            };
          }

    </script>
</head>
<body onload="fun1()">

<p id="ppp">hello p</p>

</body>
</html>
```

## onsubmit:

是当表单在提交时触发. 该属性也只能给form元素使用.应用场景: 在表单提交前验证用户输入是否正确.如果验证失败.在该方法中我们应该阻止表单的提交.

```html
<form id="form">
            <input type="text"/>
            <input type="submit" value="点我!" />
</form>

<script type="text/javascript">
            //阻止表单提交方式1().
            //onsubmit 命名的事件函数,可以接受返回值. 其中返回false表示拦截表单提交.其他为放行.

            var ele=document.getElementById("form");
            ele.onsubmit=function(event) {
//                alert("验证失败 表单不会提交!");
//                return false;
                
            // 阻止表单提交方式2 event.preventDefault(); ==>通知浏览器不要执行与事件关联的默认动作。
             alert("验证失败 表单不会提交!");
             event.preventDefault();

    }
```

## Event 对象

Event 对象代表事件的状态，比如事件在其中发生的元素、键盘按键的状态、鼠标的位置、鼠标按钮的状态。

事件通常与函数结合使用，函数不会在事件发生前被执行！event对象在事件发生时系统已经创建好了,并且会在事件函数被调用时传给事件函数.我们获得仅仅需要接收一下即可.

比如onkeydown,我们想知道哪个键被按下了，需要问下event对象的属性，这里就时KeyCode；

## 事件传播

```html
<div id="abc_1" style="border:1px solid red;width:300px;height:300px;">
        <div id="abc_2" style="border:1px solid red;width:200px;height:200px;">
        
        </div>
    </div>
    <script type="text/javascript">
    document.getElementById("abc_1").onclick=function(){
        alert('111');
    }
    document.getElementById("abc_2").onclick=function(event){
        alert('222');
        event.stopPropagation(); //阻止事件向外层div传播.
    }
    
</script>
```