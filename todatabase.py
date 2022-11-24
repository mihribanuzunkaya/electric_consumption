from pymongo import *
import matplotlib.pyplot as plot
import mplcursors as mpc
import pandas as pd
import streamlit as st
import plotly.graph_objects as px
import plotly.graph_objs as go



connection=MongoClient(host="localhost:27017")
connection=connection.iqvworks
electricReportCollection=connection.electricreport

st.sidebar.title("Raporlar")
page = st.sidebar.selectbox("Görüntülemek İstediğiniz Raporu Seçiniz",("Makine Bazlı Raporlar", "Ay Bazlı Raporlar"))


datas = electricReportCollection.find()
data_2021_list = []
data_2022_list = []

data_2021_dict = {}
data_2022_dict = {}

machine_names = [{"machine": {'name': '11-UT01'}}, {"machine": {'name': '12-UT02'}}, {"machine": {'name': '13-UF01'}},{"machine": {'name': '14-UF02'}}, {"machine": {'name': '09-DIM04'}},{"machine": {'name': '15-ST01'}}]

machines = []
machines2 = []
consumption_2021 = []
consumption_2022 = []
total = 0
results = []
results_2022 = []

# Protal Haziran-Aralık 2021 Makinelerin Toplam Elektrik Tüketimi Raporu
for i in datas:
    if '2021' in i['date']:

        data_2021_dict = {"machine": {"name": i["machine"]["name"]}, "difference": i["difference"], "date": i["date"]}
        data_2021_list.append(data_2021_dict)

    elif '2022' in i['date']:
        data_2022_dict = {"machine": {"name": i["machine"]["name"]}, "difference": i["difference"],"date": i["date"]}
        data_2022_list.append(data_2022_dict)

for a in machine_names:
    for j in data_2021_list:
        if j["machine"]["name"] == a["machine"]["name"]:
            total += int(j["difference"])

    result = {"machine": {"name": a["machine"]["name"]}, "result": (total / 1000)*2}
    consumption_2021.append(result["result"])
    machines.append(result["machine"]["name"])
    results.append(result)

total_2022 = 0
for a in machine_names:
    for j in data_2022_list:
        if j["machine"]["name"] == a["machine"]["name"]:
            total_2022 += int(j["difference"])

    result_2022 = {"machine": {"name": a["machine"]["name"]}, "result": total_2022 / 1000}
    consumption_2022.append(result_2022["result"])
    machines2.append(result_2022["machine"]["name"])
    results_2022.append(result_2022)



if page == 'Makine Bazlı Raporlar':
    st.header('Protal Makinelerin Toplam Elektrik Tüketimi (kWh) 2021 ')
    monthly_barchart = pd.DataFrame(consumption_2021, machines)
    st.bar_chart(monthly_barchart)

    st.header('Protal Makinelerin Toplam Elektrik Tüketimi (kWh) 2022 ')
    monthly_barchart_2022 = pd.DataFrame(consumption_2022, machines2)
    st.bar_chart(monthly_barchart_2022)

    st.header('2021 ve 2022 Toplam Tüketim')
    fig = px.Figure(data = [go.Bar(name = '2021', x= machines, y = consumption_2021), go.Bar(name = '2022',x = machines, y = consumption_2022 )])
    st.plotly_chart(fig, use_container_width=True)






# Protal Makinelerin 2021 Aylık Raporları

def report_monthly_2021(machine_name, date):
    total_month = 0
    for i in data_2021_list:
        if i['machine']['name'] == machine_name:
            if date in i['date']:
                total_month += int(i['difference'])
    return total_month

def report_monthly_2022(machine_name, date):
    total_month = 0
    for i in data_2022_list:
        if i['machine']['name'] == machine_name:
            if date in i['date']:
                total_month += int(i['difference'])
    return total_month

months = ['Haziran', 'Temmuz', 'Ağustos','Eylül', 'Ekim', 'Kasım', 'Aralık']
months_2022 = ['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran', 'Temmuz', 'Ağustos','Eylül', 'Ekim', 'Kasım']


monthly_consumption_11_UT01 = [report_monthly_2021('11-UT01', '2021, 6')/1000, report_monthly_2021('11-UT01','2021, 7')/1000, report_monthly_2021('11-UT01', '2021, 8')/1000, report_monthly_2021('11-UT01', '2021, 9')/1000, report_monthly_2021('11-UT01', '2021, 10')/1000, report_monthly_2021('11-UT01', '2021, 11')/1000, report_monthly_2021('11-UT01', '2021, 12')/1000]

monthly_consumption_11_UT01_2022 = [report_monthly_2022('11-UT01', '2022, 1')/1000,report_monthly_2022('11-UT01', '2022, 2')/1000, report_monthly_2022('11-UT01', '2022, 3')/1000, report_monthly_2022('11-UT01', '2022, 4')/1000, report_monthly_2022('11-UT01', '2022, 5')/1000, report_monthly_2022('11-UT01', '2022, 6')/1000, report_monthly_2022('11-UT01','2022, 7')/1000, report_monthly_2022('11-UT01', '2022, 8')/1000, report_monthly_2022('11-UT01', '2022, 9')/1000, report_monthly_2022('11-UT01', '2022, 10')/1000, report_monthly_2022('11-UT01', '2022, 11')/1000]


monthly_consumption_12_UT02 =[report_monthly_2021('12-UT02', '2021, 6')/1000, report_monthly_2021('12-UT02','2021, 7')/1000, report_monthly_2021('12-UT02', '2021, 8')/1000, report_monthly_2021('12-UT02', '2021, 9')/1000, report_monthly_2021('12-UT02', '2021, 10')/1000, report_monthly_2021('12-UT02', '2021, 11')/1000, report_monthly_2021('12-UT02', '2021, 12')/1000]

monthly_consumption_12_UT02_2022 = [report_monthly_2022('12-UT02', '2022, 1')/1000,report_monthly_2022('12-UT02', '2022, 2')/1000, report_monthly_2022('12-UT02', '2022, 3')/1000, report_monthly_2022('12-UT02', '2022, 4')/1000, report_monthly_2022('12-UT02', '2022, 5')/1000, report_monthly_2022('12-UT02', '2022, 6')/1000, report_monthly_2021('12-UT02','2022, 7')/1000, report_monthly_2021('12-UT02', '2022, 8')/1000, report_monthly_2022('12-UT02', '2022, 9')/1000, report_monthly_2022('12-UT02', '2022, 10')/1000, report_monthly_2022('12-UT02', '2022, 11')/1000]


monthly_consumption_13_UF01 =[report_monthly_2021('13-UF01', '2021, 6')/1000, report_monthly_2021('13-UF01','2021, 7')/1000, report_monthly_2021('13-UF01', '2021, 8')/1000, report_monthly_2021('13-UF01', '2021, 9')/1000, report_monthly_2021('13-UF01', '2021, 10')/1000, report_monthly_2021('13-UF01', '2021, 11')/1000, report_monthly_2021('13-UF01', '2021, 12')/1000]

monthly_consumption_13_UF01_2022 = [report_monthly_2022('13-UF01', '2022, 1')/1000,report_monthly_2022('13-UF01', '2022, 2')/1000, report_monthly_2022('13-UF01', '2022, 3')/1000, report_monthly_2022('13-UF01', '2022, 4')/1000, report_monthly_2022('13-UF01', '2022, 5')/1000, report_monthly_2022('13-UF01', '2022, 6')/1000, report_monthly_2022('13-UF01','2022, 7')/1000, report_monthly_2022('13-UF01', '2022, 8')/1000, report_monthly_2022('13-UF01', '2022, 9')/1000, report_monthly_2022('13-UF01', '2022, 10')/1000, report_monthly_2022('13-UF01', '2022, 11')/1000]

monthly_consumption_14_UF02 =[report_monthly_2021('14-UF02', '2021, 6')/1000, report_monthly_2021('14-UF02','2021, 7')/1000, report_monthly_2021('14-UF02', '2021, 8')/1000, report_monthly_2021('14-UF02', '2021, 9')/1000, report_monthly_2021('14-UF02', '2021, 10')/1000, report_monthly_2021('14-UF02', '2021, 11')/1000, report_monthly_2021('14-UF02', '2021, 12')/1000]

monthly_consumption_14_UF02_2022 = [report_monthly_2022('14-UF02', '2022, 1')/1000,report_monthly_2022('14-UF02', '2022, 2')/1000, report_monthly_2022('14-UF02', '2022, 3')/1000, report_monthly_2022('14-UF02', '2022, 4')/1000, report_monthly_2022('14-UF02', '2022, 5')/1000, report_monthly_2022('14-UF02', '2022, 6')/1000, report_monthly_2022('14-UF02','2022, 7')/1000, report_monthly_2022('14-UF02', '2022, 8')/1000, report_monthly_2022('14-UF02', '2022, 9')/1000, report_monthly_2022('14-UF02', '2022, 10')/1000, report_monthly_2022('14-UF02', '2022, 11')/1000]

monthly_consumption_09_DIM04 =[report_monthly_2021('09-DIM04', '2021, 6')/1000, report_monthly_2021('09-DIM04','2021, 7')/1000, report_monthly_2021('09-DIM04', '2021, 8')/1000, report_monthly_2021('09-DIM04', '2021, 9')/1000, report_monthly_2021('09-DIM04', '2021, 10')/1000, report_monthly_2021('09-DIM04', '2021, 11')/1000, report_monthly_2021('09-DIM04', '2021, 12')/1000]

monthly_consumption_09_DIM04_2022 = [report_monthly_2022('09-DIM04', '2022, 1')/1000,report_monthly_2022('09-DIM04', '2022, 2')/1000, report_monthly_2022('09-DIM04', '2022, 3')/1000, report_monthly_2022('09-DIM04', '2022, 4')/1000, report_monthly_2022('09-DIM04', '2022, 5')/1000, report_monthly_2022('09-DIM04', '2022, 6')/1000, report_monthly_2022('09-DIM04','2022, 7')/1000, report_monthly_2022('09-DIM04', '2022, 8')/1000, report_monthly_2022('09-DIM04', '2022, 9')/1000, report_monthly_2022('09-DIM04', '2022, 10')/1000, report_monthly_2022('09-DIM04', '2022, 11')/1000]

monthly_consumption_15_ST01 =[report_monthly_2021('15-ST01', '2021, 6')/1000, report_monthly_2021('15-ST01','2021, 7')/1000, report_monthly_2021('15-ST01', '2021, 8')/1000, report_monthly_2021('09-DIM04', '2021, 9')/1000, report_monthly_2021('15-ST01', '2021, 10')/1000, report_monthly_2021('15-ST01', '2021, 11')/1000, report_monthly_2021('15-ST01', '2021, 12')/1000]

monthly_consumption_15_ST01_2022 = [report_monthly_2022('15-ST01', '2022, 1')/1000,report_monthly_2022('15-ST01', '2022, 2')/1000, report_monthly_2022('15-ST01', '2022, 3')/1000, report_monthly_2022('15-ST01', '2022, 4')/1000, report_monthly_2022('15-ST01', '2022, 5')/1000, report_monthly_2022('09-DIM04', '2022, 6')/1000, report_monthly_2022('15-ST01','2022, 7')/1000, report_monthly_2022('15-ST01', '2022, 8')/1000, report_monthly_2022('15-ST01', '2022, 9')/1000, report_monthly_2022('15-ST01', '2022, 10')/1000, report_monthly_2022('15-ST01', '2022, 11')/1000]






if page == 'Ay Bazlı Raporlar':
    st.header('2021')
    st.write('11-UT01 Rapor')
    monthly_barchart_11_UT01 = pd.DataFrame(monthly_consumption_11_UT01, months)
    st.bar_chart(monthly_barchart_11_UT01)

    st.write('12-UT01 Rapor')
    monthly_barchart_12_UT02 = pd.DataFrame(monthly_consumption_12_UT02, months)
    st.bar_chart(monthly_barchart_12_UT02)

    st.write('13-UF01 Rapor')
    monthly_barchart_13_UF01 = pd.DataFrame(monthly_consumption_13_UF01, months)
    st.bar_chart(monthly_barchart_13_UF01)

    st.write('14-UF02 Rapor')
    monthly_barchart_14_UF02 = pd.DataFrame(monthly_consumption_14_UF02, months)
    st.bar_chart(monthly_barchart_14_UF02)

    st.write('09-DIM04 Rapor')
    monthly_barchart_09_DIM04 = pd.DataFrame(monthly_consumption_09_DIM04, months)
    st.bar_chart(monthly_barchart_09_DIM04)

    st.write('15-ST01 Rapor')
    monthly_barchart_15_ST01 = pd.DataFrame(monthly_consumption_15_ST01, months)
    st.bar_chart(monthly_barchart_15_ST01)

    st.header('2022')

    st.write('11-UT01 Rapor')
    monthly_barchart_11_UT01_2022 = pd.DataFrame(monthly_consumption_11_UT01_2022, months_2022)
    st.bar_chart(monthly_barchart_11_UT01_2022)

    st.write('12-UT01 Rapor')
    monthly_barchart_12_UT02_2022 = pd.DataFrame(monthly_consumption_12_UT02_2022, months_2022)
    st.bar_chart(monthly_barchart_12_UT02_2022)

    st.write('13-UF01 Rapor')
    monthly_barchart_13_UF01_2022 = pd.DataFrame(monthly_consumption_13_UF01_2022, months_2022)
    st.bar_chart(monthly_barchart_13_UF01_2022)

    st.write('14-UF02 Rapor')
    monthly_barchart_14_UF02_2022 = pd.DataFrame(monthly_consumption_14_UF02_2022, months_2022)
    st.bar_chart(monthly_barchart_14_UF02_2022)

    st.write('09-DIM04 Rapor')
    monthly_barchart_09_DIM04_2022 = pd.DataFrame(monthly_consumption_09_DIM04_2022,months_2022)
    st.bar_chart(monthly_barchart_09_DIM04_2022)

    st.write('15-ST01 Rapor')
    monthly_barchart_15_ST01_2022 = pd.DataFrame(monthly_consumption_15_ST01_2022, months_2022)
    st.bar_chart(monthly_barchart_15_ST01_2022)














