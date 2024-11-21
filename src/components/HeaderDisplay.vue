<template>
    <div style="display: flex; align-content: right;" id="etf">
      <el-table
        :data="tableData"
        :show-header="true"
        :border="false"
      >
        <el-table-column prop="sh016_ticker_id" label="指数" />
        <el-table-column prop="sh016_value" label="最新价"/>
        <el-table-column prop="sh300_ticker_id" label="指数"/>
        <el-table-column prop="sh300_value" label="最新价"/>
        <el-table-column prop="sh905_ticker_id" label="指数" />
        <el-table-column prop="sh905_value" label="最新价"/>
        <el-table-column prop="sh852_ticker_id" label="指数"/>
        <el-table-column prop="sh852_value" label="最新价"/>
      </el-table>
    </div>
    <div id="etf-time">
        Update Time: 2024-11-21 17:52
    </div>
</template>

<style scoped>
#etf-time{
    text-align: right;
    margin: 1%  ;
    font-size: .5em;
}
</style>

<script lang="ts" setup>
    interface ETF_data {
        sh016_ticker_id: String
        sh016_value: number,
        sh300_ticker_id: String
        sh300_value: number,
        sh905_ticker_id: String
        sh905_value: number,
        sh852_ticker_id: String
        sh852_value: number,
    }
    const tableData: ETF_data[] =[
        {
            sh016_ticker_id:"000016.SH",
            sh016_value: 2676,
            sh300_ticker_id:"000030.SH",
            sh300_value: 3986,
            sh905_ticker_id:"000905.SH",
            sh905_value: 5992,
            sh852_ticker_id:"000852.SH",
            sh852_value: 6251
        }
    ]
</script>