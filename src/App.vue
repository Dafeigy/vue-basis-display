<script  lang ='ts' setup>
  import HeaderDisplay from './components/HeaderDisplay.vue';
  import TableDisplay from './components/TableDisplay.vue'
  import { Calendar, Search } from '@element-plus/icons-vue'
  import { ref,reactive, provide, inject } from 'vue';
  
  const input1 = ref('');
  var symbols:String[] = []
  sessionStorage.removeItem("symbols")
  const AddDate = ()=>{
    if (input1.value){
      symbols.push(input1.value)
      sessionStorage.setItem("symbols",JSON.stringify(symbols));
      console.log(sessionStorage.getItem("symbols"))
    }
    else{
      alert("Please select contract date!")
    }
  }

  const DelDate = ()=>{
    if (input1.value){
      symbols = symbols.filter(item => item !== input1.value);
      sessionStorage.setItem("symbols",JSON.stringify(symbols));
    }
    else{
      alert("Please select contract date!")
    }
  }
  
</script>


<template>
  <div id="container">
    <div id="control">
      <el-date-picker
          v-model="input1"
          type="month"
          placeholder="←选择合约月份"
          value-format="YYMM"
          locale="locale"
        />
      <el-button type="primary" style="margin-left: .5%; background-color: #444; border: none;" @click="AddDate">Add</el-button>
      <el-button type="danger" style="margin-left: .5%; border: none;" @click="DelDate">Del</el-button>
    </div>
    <div id="header">
      <HeaderDisplay></HeaderDisplay>
    </div>
    <div id="futures">
      <TableDisplay></TableDisplay>
    </div>
  
  </div>
  
</template>

<style scoped>

#futures :deep( .el-table__row)>td{
  /* 去除表格线 */
  border: none;
}

#control{
  margin: 1%;
  margin-left: 0;
}

</style>