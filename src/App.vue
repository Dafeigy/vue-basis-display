<script setup>
import HeaderDisplay from './components/HeaderDisplay.vue';
import TableDisplay from './components/TableDisplay.vue'
import { Calendar, Search } from '@element-plus/icons-vue'
import { ref } from 'vue';
const input1 = ref('')

const DebugTest = ()=>{
  alert(input1.value)
}
</script>


<template>
  <div id="container">
    <div id="control">
      <el-date-picker
          v-model="input1"
          type="month"
          placeholder="Pick a month"
          value-format="YYDD"
        />
      <el-button type="primary" style="margin-left: .5%;" @click="DebugTest()">Get</el-button>
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