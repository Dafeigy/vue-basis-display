<script setup>
import HeaderDisplay from './components/HeaderDisplay.vue';
import TableDisplay from './components/TableDisplay.vue'
import { Calendar, Search } from '@element-plus/icons-vue'
import { ref } from 'vue';


const input1 = ref('')

const DebugTest = ()=>{
  if (input1.value){
    alert(input1.value)
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
          value-format="YYDD"
          :locale="locale"
        />
      <el-button type="primary" style="margin-left: .5%; background-color: #444; border: none;" @click="DebugTest()">Get</el-button>
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