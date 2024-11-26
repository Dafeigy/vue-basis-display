<template>
    <div style="display: flex; align-content: right;" id="etf">
      <el-table
        :data="tableData"
        :show-header="true"
        :border="false"
      >
        <el-table-column prop="sh016_ticker_id" label="指数"/>
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
        Update Time: {{ ETFUpdateTime }}
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
    import { ref, onMounted, onUnmounted } from 'vue';
    let intervalId = null;
    var ETFUpdateInterval = 1000
    const ETFUpdateTime= ref("2024-11-28 17:32.322")
    interface ETF_data {
        sh016_ticker_id: String
        sh016_value: number,
        sh300_ticker_id: String
        sh300_value: number,
        sh905_ticker_id: String
        sh905_value: number,
        sh852_ticker_id: String
        sh852_value: number,
        response_time: String
    }   

    const tableData =ref([
        {
            sh016_ticker_id:"000016.SH",
            sh016_value: 2676,
            sh300_ticker_id:"000030.SH",
            sh300_value: 3986,
            sh905_ticker_id:"000905.SH",
            sh905_value: 5992,
            sh852_ticker_id:"000852.SH",
            sh852_value: 6251,
            response_time: "2000-01-01 12:00.023"
        }
    ])

    const fetchData = async () => {
      try {
        const response = await fetch('http://127.0.0.1:5000/get-etf-data');
        const data = await response.json();
        Object.keys(data['data']).forEach(key => {
          tableData.value[0][key] = data['data'][key];
        });
        ETFUpdateTime.value = data['response_time']
        // NOTE: 组件间通信感觉操作起来比较麻烦 直接用session了
        sessionStorage.setItem("ETF_Realtime", JSON.stringify(data));
      } catch (error) {
        console.error('请求失败:', error);
      }
    };

    onMounted(() => {
      setInterval(fetchData, ETFUpdateInterval);
    });

    onUnmounted(() => {
      clearInterval(intervalId);
    });

</script>