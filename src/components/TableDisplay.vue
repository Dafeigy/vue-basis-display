<template>
    <div style="display: flex; align-content: right;">
      <el-table
        :data="tableData"
        :span-method="objectSpanMethod"
        :cell-style="columnStyle"
        :header-cell-style="headerStyle"
        :border="true"
      >
        <el-table-column prop="IH_time" label="合约代码" />
        <el-table-column prop="IH_basis" label="基差"/>
        <el-table-column prop="IH_basis_pct" label="基差率"/>
        <el-table-column prop="IH_trade_flag" label="" width="90vw"/>
        <el-table-column prop="IF_time" label="合约代码" />
        <el-table-column prop="IF_basis" label="基差"/>
        <el-table-column prop="IF_basis_pct" label="基差率"/>
        <el-table-column prop="IF_trade_flag" label="" width="90vw"/>
        <el-table-column prop="IC_time" label="合约代码" />
        <el-table-column prop="IC_basis" label="基差"/>
        <el-table-column prop="IC_basis_pct" label="基差率"/>
        <el-table-column prop="IC_trade_flag" label="" width="90vw"/>
        <el-table-column prop="IM_time" label="合约代码" />
        <el-table-column prop="IM_basis" label="基差"/>
        <el-table-column prop="IM_basis_pct" label="基差率"/>
        <el-table-column prop="IM_trade_flag" label="" width="90vw"/>
      </el-table>
    </div>
    <div id="contract-time">
        Update Time: 2024-11-21 12:52
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
    /* text-align: right; */
    font-size: .5em;
    display: flex;
    float: right;
  }
  
</style>
<script lang="ts" setup>
import type { TableColumnCtx } from 'element-plus'

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
        borderBottom: '2px #000 solid',
    }

}

const tableData: BasisData[] = [
{
    IH_time: 'IH2412',
    IH_basis: 4.2,
    IH_basis_pct: 1.7,
    IH_trade_flag: "卖一",
    IF_time: 'IF2412',
    IF_basis: -5.8,
    IF_basis_pct: -1.5,
    IF_trade_flag: "卖一",
    IC_time: 'IC2412',
    IC_basis: -48.4,
    IC_basis_pct: -8.6,
    IC_trade_flag: "卖一",
    IM_time: 'IM2412',
    IM_basis: -59.0,
    IM_basis_pct: -10.5,
    IM_trade_flag: "卖一",
},
{
    IH_time: 'IH2412',
    IH_basis: 3.6,
    IH_basis_pct: 1.4,
    IH_trade_flag: '买一',
    IF_time: 'IF2412',
    IF_basis: -6.0,
    IF_basis_pct: -1.6,
    IF_trade_flag: '买一',
    IC_time: 'IC2412',
    IC_basis: -50.2,
    IC_basis_pct: -8.9,
    IC_trade_flag: '买一',
    IM_time: 'IM2412',
    IM_basis: -59.2,
    IM_basis_pct: -10.5,
    IM_trade_flag: '买一',
},
{
    IH_time: 'IH2503',
    IH_basis: 5.6,
    IH_basis_pct: 1.2,
    IH_trade_flag: '卖一',
    IF_time: 'IF2503',
    IF_basis: -2.2,
    IF_basis_pct: -0.3,
    IF_trade_flag: '卖一',
    IC_time: 'IC2503',
    IC_basis: -69.6,
    IC_basis_pct: -6.8,
    IC_trade_flag: '卖一',
    IM_time: 'IM2503',
    IM_basis: -90.8,
    IM_basis_pct: -8.8,
    IM_trade_flag: '卖一',
},
{
    IH_time: 'IH2503',
    IH_basis: 4.2,
    IH_basis_pct: 0.9,
    IH_trade_flag: '买一',
    IF_time: 'IF2503',
    IF_basis: -7.6,
    IF_basis_pct: -1.1,
    IF_trade_flag: '买一',
    IC_time: 'IC2503',
    IC_basis: -75.4,
    IC_basis_pct: -7.3,
    IC_trade_flag: '买一',
    IM_time: 'IM2503',
    IM_basis: -91.6,
    IM_basis_pct: -8.9,
    IM_trade_flag: '买一',
},
]
</script>
