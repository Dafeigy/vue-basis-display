# vue-basis-visualization demo

显示实时的基差、基差率数据。数据的处理与运算在前端完成，后端只返回数据。


前端使用依赖:

- Element-UI-Plus，用于表格组件。

- Axios，异步请求。

后端支持:

- Flask

## 基本使用
### 使用前置

```sh
npm install
pip install flask, flask_cors
```

### 启动

前端Vue启动：
```sh
npm run dev
```

后端flask启动（仅作为模拟数据交互流程）：
```sh
flask run 
```
后端数据请求参考后面一节。


### 编译

```sh
npm run build
```
## 代码结构

### 基本结构

构建了两个组件：`HeaderDisplay`和`TableDisplay`，此二者分别对应的是股指的数据显示以及期货的数据显示的组件。添加新的合约日期的组件因为较为简单，则直接在`App.Vue`中进行编写。实时的可视化是前端通过`setInterval`向后端定期请求最新的合约/股指数据实现的。请求间隔均在对应的`.vue`文件中的`xxxInterval`变量中定义，单位为毫秒；股指、期货数据的获取依赖于后端的Flask的两个路由，用于模拟实际的数据交互情况。

### 数据请求

后端我使用了Flask进行模拟，设置了两个路由`/get-contracts-data`和`/get-etf-data`。Flask应用默认设置在`127.0.0.1:5000`上运行，因此在Vue的两个组件中，请求的url地址分别为：

- `http://127.0.0.1:5000/get-etf-data`，无参数。

- `http://127.0.0.1:5000/get-contracts-data`，有参数。

前者的可视化页面在初始化时将会显示对应的股指信息，最新价格将会以`NaN`值显示；如果请求获取最新的价格失败，则不会对数据进行更新。该值会以json格式保存在SessionStorage中的`ETF_realtime`字段中。

后者的参数为合约的日期`YYMM`格式的字符串，代表的是合约到期月。该参数在后端处理后会返回对应的不同月份四个合约的相关信息。该参数为空时，不会在页面显示数据。该参数在每一个页面实例中均会保存到SessionStorage的`symbols`字段中。

这个参数的获取来源于`App.vue`中的两个`<el-button>`对应的点击事件函数: `AddDate`和`DelDate`。这两个按钮会绑定月份选择器中的月份值，并将这个值存放到symbols中，进行添加或删除的操作，并在每一次操作结束后更新SessionStorage中的`symbols`。

| 注意：如果需要关闭浏览器再打开时恢复上一次添加的合约信息，可以考虑将SessionStorage更换为LocalStorage。

### 路由返回数据格式

所有的数据值都由随机数生成。

- `/get-etf-data`：返回股指数据的最新价。返回样例如下:
  
  ```json
  {
  "data":{
    "sh016_value": 2049,
    "sh300_value": 3927,
    "sh905_value": 6012,
    "sh852_value": 6128
  },
  "response_time": "2024-11-25 14:42.304"
  }
  ```

- `/get-contracts-data`：返回对应日期的四支股指期货的数据，返回样例如下:

  ```json
  // 参数为空时
  {}
 
  // 参数为”2412“时
  {
    "2412":{
      "data":{
        "IH_2412":{
          "buy_value": 2563,
          "sell_value": 2632
        },
        "IF_2412":{
          "buy_value": 2563,
          "sell_value": 2632
        },
        "IC_2412":{
          "buy_value": 2563,
          "sell_value": 2632
        },
        "IM_2412":{
          "buy_value": 2563,
          "sell_value": 2632
        },
      },
      "time":2024-11-26 14:42.042,
      "expired": 83
    }
  }

  // 参数为"[2412,2503]"时
  {
    "2412":{
      "data":{
        "IH_2412":{
          "buy_value": 2563,
          "sell_value": 2632
        },
        "IF_2412":{
          "buy_value": 2563,
          "sell_value": 2632
        },
        "IC_2412":{
          "buy_value": 2563,
          "sell_value": 2632
        },
        "IM_2412":{
          "buy_value": 2563,
          "sell_value": 2632
        },
      },
      "time":2024-11-26 14:42.042,
      "expired": 83
    },
    "2503":{
      "data":{
        "IH_2503":{
          "buy_value": 2563,
          "sell_value": 2632
        },
        "IF_2503":{
          "buy_value": 2563,
          "sell_value": 2632
        },
        "IC_2503":{
          "buy_value": 2563,
          "sell_value": 2632
        },
        "IM_2503":{
          "buy_value": 2563,
          "sell_value": 2632
        },
      },
      "time":2024-11-26 14:42.042,
      "expired": 83
    }
  }
  ```

  其中的`time`是指数据更新的时间，expired指代当前时间距离该合约最后的交易日的交割时间，后期用于计算基差率。合约的到期日计算是在后端完成的，目前只设定了`[2412,2501,2503,2506]`四个日期的交割日，如果使用其他交割日期会无法计算基差率。

### 基差与基差率计算

基差的计算公式为：

$$
基差= 股指最新价-最新的合约对应的买一/卖一价
$$

基差率计算公式为，245为当年的交易日数：

$$
基差率= \frac{基差}{股指最新价}\times\frac{245}{到期日数}
$$

计算在`TableDisplay`组件中完成，并且对基差率使用`:formatter`进行百分数保留三位小数的转换。具体的操作则是从SessionStorage取出所需的数据进行计算，并将计算结果绑定到一个ref中，实现数据的响应式更新。







