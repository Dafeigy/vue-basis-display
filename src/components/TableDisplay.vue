<template>
    <div style="display: flex; align-content: right;">
      <el-table
        :data="returnData"
        :span-method="objectSpanMethod"
        :cell-style="columnStyle"
        :header-cell-style="headerStyle"
        :border="true"
        
      >
        <el-table-column prop="IH_time" label="合约代码" />
        <el-table-column prop="IH_basis" label="基差"/>
        <el-table-column :formatter="formatPercentage" prop="IH_basis_pct" label="基差率" />
        <el-table-column prop="IH_trade_flag" label="" width="90vw"/>
        <el-table-column prop="IF_time" label="合约代码" />
        <el-table-column prop="IF_basis" label="基差"/>
        <el-table-column :formatter="formatPercentage" prop="IF_basis_pct" label="基差率"/>
        <el-table-column prop="IF_trade_flag" label="" width="90vw"/>
        <el-table-column prop="IC_time" label="合约代码" />
        <el-table-column prop="IC_basis" label="基差"/>
        <el-table-column :formatter="formatPercentage" prop="IC_basis_pct" label="基差率"/>
        <el-table-column prop="IC_trade_flag" label="" width="90vw"/>
        <el-table-column prop="IM_time" label="合约代码" />
        <el-table-column prop="IM_basis" label="基差"/>
        <el-table-column :formatter="formatPercentage" prop="IM_basis_pct" label="基差率"/>
        <el-table-column prop="IM_trade_flag" label="" width="90vw"/>
      </el-table>
    </div>
    <div id="contract-time">
        Update Time: {{ contractsUpdateTime }}
    </div>
</template>

<style>
  #display{
    width: 90%;
    display: flex;
    float: right;
  }
  #contract-time{
    margin: 1%;
    text-align: right;
    font-size: .5em;

  }
  
</style>

<script lang="ts" setup>
    import axios from 'axios';
    import type { TableColumnCtx } from 'element-plus'
    import { onMounted, onUnmounted, ref } from 'vue';

    let intervalId = null;
    let contractUpdateInterval = 500
    var symbols = []
    const returnData = ref([])
    const contractsUpdateTime = ref("")
    
    interface SpanMethodProps {
        row: BasisData
        column: TableColumnCtx<BasisData>
        rowIndex: number
        columnIndex: number
    }
    const objectSpanMethod = ({
        row,
        column,
        rowIndex,
        columnIndex,
    }: SpanMethodProps) => {
        if (columnIndex %4 === 0) { //每4行对应的是合约Symbol，合并这两行
            if (rowIndex % 2 === 0) {
            return {
                rowspan: 2,
                colspan: 1,
            }
            } else {
            return {
                rowspan: 0,
                colspan: 0,
            }
            }
        }
    }
    const columnStyle = ({row, column, rowIndex, columnIndex})=>{
        if ((columnIndex + 1) % 4 === 0) {  
            // return 'color: #888;'
            if (rowIndex % 2 === 1){
                return {
                'background-color': '#808080',
                'color': '#aaa',
                'font-size': "1em",
                'width': "10px",
                'text-align': "right"
                }
            }
            else {
                return {
                'background-color': '#808080',
                'color': '#aaa',
                'font-size': "1em",
                'width': "10px",
                'text-align': "left"
                }
            }
        }
        else if(columnIndex % 4 === 0){
            return {
                'text-align': "center"
            }
        }
        else {
            return {
                "text-align":"right"
            }
        }
    }
    const headerStyle = ({})=>{
        return {
            'background':'#fff', 
            'color':'black', 
            'text-align': 'center',
            'border': 'none'
        }

    }

    const formatPercentage = (a,b,c)=>{
        return (c * 100).toFixed(3) + "%"
    }
    interface BasisData {
        IH_time: string
        IH_basis: number
        IH_basis_pct: number
        IH_trade_flag: string
        IF_time: string
        IF_basis: number
        IF_basis_pct: number
        IF_trade_flag: string
        IC_time: string
        IC_basis: number
        IC_basis_pct: number
        IC_trade_flag: string
        IM_time: string
        IM_basis: number
        IM_basis_pct: number
        IM_trade_flag: string
    }

    const fetchData = async () => {
        symbols = JSON.parse(sessionStorage.getItem("symbols"));
        // console.log(symbols)
        if (symbols === null){
            return
        }
        try {
            const params = {
                list: symbols.join(",")
            };
            if (symbols.length ===0){
                returnData.value = []
                return
            }
            const response = await axios.get('http://127.0.0.1:5000/get-contracts-data',{params});
            const data = await response.data;
            contractsUpdateTime.value = data[symbols.at(-1)].time
            let etf_latest = JSON.parse(sessionStorage.getItem("ETF_Realtime"))
            returnData.value = []
            // console.log("We start here")
            // console.log(data)
            for (const date of Object.keys(data)) {
                var sell = {IH_trade_flag: "卖一",
                            IF_trade_flag: "卖一",
                            IC_trade_flag: "卖一",
                            IM_trade_flag: "卖一",
                        }
                var buy = {
                    IH_trade_flag: '买一',
                    IF_trade_flag: '买一',
                    IC_trade_flag: '买一',
                    IM_trade_flag: '买一'
                }
                
                for (const contract of Object.keys(data[date]['data'])){
                    var expired_time = data[date]['expired']
                    if (contract.startsWith("IH")){
                        sell['IH_time'] = contract
                        buy['IH_time'] = contract
                        sell['IH_basis'] = data[date]['data'][contract]['sell_value'] - etf_latest.data.sh016_value
                        buy['IH_basis'] = data[date]['data'][contract]['buy_value'] - etf_latest.data.sh016_value
                        sell['IH_basis_pct'] = (sell['IH_basis']/etf_latest.data.sh016_value)/expired_time * 245
                        buy['IH_basis_pct'] = (buy['IH_basis']/etf_latest.data.sh016_value)/expired_time * 245
                        
                    }
                    else if(contract.startsWith("IF")){
                        sell['IF_time'] = contract
                        buy['IF_time'] = contract
                        sell['IF_basis'] = data[date]['data'][contract]['sell_value'] - etf_latest.data.sh300_value
                        buy['IF_basis'] = data[date]['data'][contract]['buy_value'] - etf_latest.data.sh300_value
                        sell['IF_basis_pct'] = (sell['IF_basis']/etf_latest.data.sh300_value)/expired_time * 245
                        buy['IF_basis_pct'] = (buy['IF_basis']/etf_latest.data.sh300_value)/expired_time * 245
                    }
                    else if(contract.startsWith("IC")){
                        sell['IC_time'] = contract
                        buy['IC_time'] = contract
                        sell['IC_basis'] = data[date]['data'][contract]['sell_value'] - etf_latest.data.sh905_value
                        buy['IC_basis'] = data[date]['data'][contract]['buy_value'] - etf_latest.data.sh905_value
                        sell['IC_basis_pct'] = (sell['IC_basis']/etf_latest.data.sh905_value)/expired_time * 245
                        buy['IC_basis_pct'] = (buy['IC_basis']/etf_latest.data.sh905_value)/expired_time * 245
                    }
                    else if(contract.startsWith("IM")){
                        sell['IM_time'] = contract
                        buy['IM_time'] = contract
                        sell['IM_basis'] = data[date]['data'][contract]['sell_value'] - etf_latest.data.sh852_value
                        buy['IM_basis'] = data[date]['data'][contract]['buy_value'] - etf_latest.data.sh852_value
                        sell['IM_basis_pct'] = (sell['IM_basis']/etf_latest.data.sh852_value)/expired_time * 245
                        buy['IM_basis_pct'] = (buy['IM_basis']/etf_latest.data.sh852_value)/expired_time * 245
                    }
                }
                returnData.value.push(sell, buy)
            }
        } catch (error) {
            console.error('请求失败:', error);
        }
        };

        onMounted(() => {
        setInterval(fetchData, contractUpdateInterval);
        });

        onUnmounted(() => {
        clearInterval(intervalId);
        });
    
    // Get data from TableDisplay.

</script>
