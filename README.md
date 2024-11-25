# vue-basis-table

展示表格，后端我用flask传进来进行测试。

## Recommended IDE Setup

[VSCode](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur).

## Customize configuration

See [Vite Configuration Reference](https://vite.dev/config/).

## Project Setup

```sh
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```

### Compile and Minify for Production

```sh
npm run build
```


Vue3中，App.vue中定义了
```vue
<template>
<el-button type="primary" style="margin-left: .5%; background-color: #444; border: none;" @click="AddDate()">Add</el-button>
</template>
const input1 = ref('')

const AddDate = ()=>{
  if (input1.value){
    // TODO
  }
  else{
    alert("Please select contract date!")
  }
}
```

另一个组件文件`TableDisplay.vue`中有:
```vue
    const symbols = reactive([]);

    const addSymbol = (symbol) => {
        symbols.push(symbol);
    }
```
现在我希望：当按钮被点击时，可以将对应的input1.value值传递给symbols。