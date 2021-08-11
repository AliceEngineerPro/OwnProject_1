# DOM的增删改查

## node的CURD

### 增

```js
createElement(name);  // 创建元素
appendChind();  //将元素添加
```

### 删

```bash
获得要删除的元素
获得它的父元素
使用removeChild()方法删除
```

### 改

```bash
第一种方式:
	使用上面增和删结合完成修改
第二中方式:
	使用setAttribute();方法修改属性
	使用innerHTML属性修改元素的内容
```

### 查

通过DOM对象

- <font color = #ff0000>示例</font>

```js
<script type="text/javascript">
//在第一个div中动态增加一个a标签. 该a标签点击之后跳转到百度首页.
    function addNode(){
        //1.获得 第一个div
        var div = document.getElementById("div_1");
        //2.创建a标签  createElement==>创建一个a标签   <a></a>
        var eleA =  document.createElement("a");
        //3.为a标签添加属性 <a href="http://www.baidu.com"></a>
        eleA.setAttribute("href", "http://www.baidu.com");
        //4.为a标签添加内容 <a href="http://www.baidu.com">百度</a>
        eleA.innerHTML = "百度";    
        //5.将a标签添加到div中
        div.appendChild(eleA);
    }
    //点击后 删除div区域2
    function deleteNode(){
        //1 获得要删除的div区域
            var div = document.getElementById("div_2");
        //2.获得父亲
            var parent = div.parentNode;
        //3 由父亲操刀 
            parent.removeChild(div);
    }
    //点击后 替换div区域3 为一个美女
    function updateNode(){
        //1 获得要替换的div区域3
        var div = document.getElementById("div_3");
        //2创建img标签对象 <img />
        var img = document.createElement("img");
        //3添加属性 <img src="001.jpg" />
        img.setAttribute("src", "001.JPG");
        //4.获得父节点
        var parent = div.parentNode;
        //5.替换
        parent.replaceChild(img, div);
    }
    //点击后 将div区域4 克隆一份 添加到页面底部
    
    function copyNode(){
        //1.获取要克隆的div
        var div = document.getElementById("div_4");
        //2.克隆 参数为true 那么克隆时克隆所有子元素. false 只克隆自己
        var div_copy = div.cloneNode(true);
        //3.获得父亲
        var parent = div.parentNode;
        //4.添加
        parent.appendChild(div_copy);
    }
    
    
</script>
```

## 修改 HTML DOM 

- 改变 HTML 内容 

改变元素内容的最简答的方法是使用 innerHTML ，innerText。

- 改变 CSS 样式 

```js
<p id="p2">Hello world!</p>
document.getElementById("p2").style.color="blue";<br>
```

- 改变 HTML 属性 

```js
elementNode.setAttribute(name,value)
elementNode.getAttribute(name)<-------------->elementNode.value(DHTML)
```

- 创建新的 HTML 元素 

```js
createElement(name)
```

- 删除已有的 HTML 元素 

```js
elementNode.removeChild(node)
```

- 关于class的操作 

```js
elementNode.className
elementNode.classList.add
elementNode.classList.remove
```

