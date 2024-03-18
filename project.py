import pandas as pd
import streamlit as st
import altair as alt

st.set_page_config(
    page_title = 'Dasboard Sales',
    page_icon = '📁',
    layout='wide'
)

# Call Data
def call_data(path):
    dd = pd.read_csv(path)
    dd['year'] = dd['Date'].str[:4]
    dd['month'] = dd['Date'].str[5:7]
    dd['date'] = dd['Date'].str[8:]
    return dd

dd = call_data('dairy_dataset.csv')

# Making Functions

def format_large_number(number):
    suffixes = ["", "K", "M", "B", "T"]
    magnitude = 0
    while abs(number) >= 1000 and magnitude < len(suffixes) - 1:
        magnitude += 1
        number /= 1000.0
    return '{:.2f}{}'.format(number, suffixes[magnitude])

def count_farm():
    count_farms = dd.groupby(['Location']).agg(
        {'Location':'count'}
    )
    count_farms = count_farms.rename(columns={'Location':'Jumlah'})
    return st.dataframe(count_farms, height= 200 ,width=300)

def count_product():
    st.subheader('Total Transaksi Setiap Produk')
    count_products = dd.groupby(['Product Name']).agg({
        'Product Name':'count'
    })
    count_products = count_products.rename(columns={'Product Name':'Jumlah'}).reset_index(drop=False)
    count_products = count_products.sort_values(['Jumlah'], ascending=False).reset_index(drop=True)
    list_product = count_products['Product Name'].tolist()
    list_count = count_products['Jumlah'].tolist()
    
    cols = st.columns(4)
    
    columns_to_drop = [
        'Location',
        'Total Land Area (acres)',
        'Number of Cows',
        'Farm Size',
        'Product ID',
        'Brand',
        'Quantity (liters/kg)',
        'Price per Unit',
        'Total Value',
        'Shelf Life (days)',
        'Storage Condition',
        'Production Date',
        'Expiration Date',
        'Quantity Sold (liters/kg)',
        'Price per Unit (sold)',
        'Approx. Total Revenue(INR)',
        'Customer Location',
        'Sales Channel',
        'Quantity in Stock (liters/kg)',
        'Minimum Stock Threshold (liters/kg)',
        'Reorder Quantity (liters/kg)'
    ]
        
    for i in range(len(list_product)):
        if i < 4:
            with cols[i]:
                colsmall = st.columns(2)
                date_sold = dd.loc[dd['Product Name'] == list_product[i]].drop(columns=columns_to_drop).sort_values(['year', 'month', 'date'], ascending=[True, True, True])
                date_sold_monthly = date_sold.groupby(['year']).agg({'Product Name':'count'}).reset_index(drop=False)
                chart=alt.Chart(date_sold_monthly).encode(
                    x=alt.X('year:N', axis=None),
                    y=alt.Y('Product Name:Q', axis=None),
                    text=alt.Text('Product Name:Q'),
                    tooltip=[
                        alt.Tooltip('year', title='Tahun'),
                        alt.Tooltip('Product Name', title='Banyak barang terjual')
                    ]
                ).properties(
                    height=60
                )
                chart_bar = chart.mark_bar()
                text = chart.mark_text(baseline='bottom')
                combined = chart_bar + text 
                with colsmall[0]:
                    ci = st.container(border=True)
                    ci.metric(label=list_product[i], value= list_count[i])
                with colsmall[1]:
                    ci.altair_chart(combined)
        elif 4 <= i < 8:
            with cols[i-4]:
                colsmall = st.columns(2)
                date_sold = dd.loc[dd['Product Name'] == list_product[i]].drop(columns=columns_to_drop).sort_values(['year', 'month', 'date'], ascending=[True, True, True])
                date_sold_monthly = date_sold.groupby(['year']).agg({'Product Name':'count'}).reset_index(drop=False)
                chart=alt.Chart(date_sold_monthly).encode(
                    x=alt.X('year:N', axis=None),
                    y=alt.Y('Product Name:Q', axis=None),
                    text=alt.Text('Product Name:Q'),
                    tooltip=[
                        alt.Tooltip('year', title='Tahun'),
                        alt.Tooltip('Product Name', title='Banyak barang terjual')
                    ]
                ).properties(
                    height=60
                )
                chart_bar = chart.mark_bar()
                text = chart.mark_text(baseline='bottom')
                combined = chart_bar + text 
                with colsmall[0]:
                    ci = st.container(border=True)
                    ci.metric(label=list_product[i], value= list_count[i])
                with colsmall[1]:
                    ci.altair_chart(combined)
        else :
            with cols[i-8]:
                colsmall = st.columns(2)
                date_sold = dd.loc[dd['Product Name'] == list_product[i]].drop(columns=columns_to_drop).sort_values(['year', 'month', 'date'], ascending=[True, True, True])
                date_sold_monthly = date_sold.groupby(['year']).agg({'Product Name':'count'}).reset_index(drop=False)
                chart=alt.Chart(date_sold_monthly).encode(
                    x=alt.X('year:N', axis=None),
                    y=alt.Y('Product Name:Q', axis=None),
                    text=alt.Text('Product Name:Q'),
                    tooltip=[
                        alt.Tooltip('year', title='Tahun'),
                        alt.Tooltip('Product Name', title='Banyak barang terjual')
                    ]
                ).properties(
                    height=60
                )
                chart_bar = chart.mark_bar()
                text = chart.mark_text(baseline='bottom')
                combined = chart_bar + text 
                with colsmall[0]:
                    ci = st.container(border=True)
                    ci.metric(label=list_product[i], value= list_count[i])
                with colsmall[1]:
                    ci.altair_chart(combined)

def count_brand():
    st.subheader('Total Transaksi Setiap Brand')
    count_products = dd.groupby(['Brand']).agg({
        'Brand':'count'
    })
    count_products = count_products.rename(columns={'Brand':'Jumlah'}).reset_index(drop=False)
    count_products = count_products.sort_values(['Jumlah'], ascending=False).reset_index(drop=True)
    list_product = count_products['Brand'].tolist()
    list_count = count_products['Jumlah'].tolist()
    
    cols = st.columns(4)
    
    columns_to_drop = [
        'Location',
        'Total Land Area (acres)',
        'Number of Cows',
        'Farm Size',
        'Product ID',
        'Product Name',
        'Quantity (liters/kg)',
        'Price per Unit',
        'Total Value',
        'Shelf Life (days)',
        'Storage Condition',
        'Production Date',
        'Expiration Date',
        'Quantity Sold (liters/kg)',
        'Price per Unit (sold)',
        'Approx. Total Revenue(INR)',
        'Customer Location',
        'Sales Channel',
        'Quantity in Stock (liters/kg)',
        'Minimum Stock Threshold (liters/kg)',
        'Reorder Quantity (liters/kg)'
    ]
        
    for i in range(len(list_product)):
        if i < 4:
            with cols[i]:
                colsmall = st.columns(2)
                date_sold = dd.loc[dd['Brand'] == list_product[i]].drop(columns=columns_to_drop).sort_values(['year', 'month', 'date'], ascending=[True, True, True])
                date_sold_monthly = date_sold.groupby(['year']).agg({'Brand':'count'}).reset_index(drop=False)
                chart=alt.Chart(date_sold_monthly).encode(
                    x=alt.X('year:N', axis=None),
                    y=alt.Y('Brand:Q', axis=None),
                    text=alt.Text('Brand:Q'),
                    tooltip=[
                        alt.Tooltip('year', title='Tahun'),
                        alt.Tooltip('Brand', title='Banyak barang terjual')
                    ]
                ).properties(
                    height=60
                )
                chart_bar = chart.mark_bar()
                text = chart.mark_text(baseline='bottom')
                combined = chart_bar + text 
                with colsmall[0]:
                    ci = st.container(border=True)
                    ci.metric(label=list_product[i], value= list_count[i])
                with colsmall[1]:
                    ci.altair_chart(combined)
        elif 4 <= i < 8:
            with cols[i-4]:
                colsmall = st.columns(2)
                date_sold = dd.loc[dd['Brand'] == list_product[i]].drop(columns=columns_to_drop).sort_values(['year', 'month', 'date'], ascending=[True, True, True])
                date_sold_monthly = date_sold.groupby(['year']).agg({'Brand':'count'}).reset_index(drop=False)
                chart=alt.Chart(date_sold_monthly).encode(
                    x=alt.X('year:N', axis=None),
                    y=alt.Y('Brand:Q', axis=None),
                    text=alt.Text('Brand:Q'),
                    tooltip=[
                        alt.Tooltip('year', title='Tahun'),
                        alt.Tooltip('Brand', title='Banyak barang terjual')
                    ]
                ).properties(
                    height=60
                )
                chart_bar = chart.mark_bar()
                text = chart.mark_text(baseline='bottom')
                combined = chart_bar + text 
                with colsmall[0]:
                    ci = st.container(border=True)
                    ci.metric(label=list_product[i], value= list_count[i])
                with colsmall[1]:
                    ci.altair_chart(combined)
        else :
            with cols[i-8]:
                colsmall = st.columns(2)
                date_sold = dd.loc[dd['Brand'] == list_product[i]].drop(columns=columns_to_drop).sort_values(['year', 'month', 'date'], ascending=[True, True, True])
                date_sold_monthly = date_sold.groupby(['year']).agg({'Brand':'count'}).reset_index(drop=False)
                chart=alt.Chart(date_sold_monthly).encode(
                    x=alt.X('year:N', axis=None),
                    y=alt.Y('Brand:Q', axis=None),
                    text=alt.Text('Brand:Q'),
                    tooltip=[
                        alt.Tooltip('year', title='Tahun'),
                        alt.Tooltip('Brand', title='Banyak barang terjual')
                    ]
                ).properties(
                    height=60
                )
                chart_bar = chart.mark_bar()
                text = chart.mark_text(baseline='bottom')
                combined = chart_bar + text 
                with colsmall[0]:
                    ci = st.container(border=True)
                    ci.metric(label=list_product[i], value= list_count[i])
                with colsmall[1]:
                    ci.altair_chart(combined)

def progress_bar():
    target = 70000000
    sales = dd['Approx. Total Revenue(INR)'].tolist()
    sales_total = sum(sales)
    sales_target = sales_total/target
    
    co=st.container(border=True)
    
    co.progress(sales_target, text='**Target Penjualan:**')
    
    progress_style = f"""
    <div style="
        display: flex;
        justify-content: space-between;
        align-items: center;">
        <span>0</span>
        <span style="position: absolute; left: {sales_target * 100}%; transform: translateX(-50%);">{format_large_number(sales_total)}</span>
        <span>70M</span>
    </div>
    """
    co.markdown(progress_style, unsafe_allow_html=True)

def progress_donut_chart():
    co = st.container(border=True)
    target = 70000000
    sales = dd['Approx. Total Revenue(INR)'].tolist()
    sales_total = sum(sales)
    sales_target_percentage = sales_total/target * 100
    
    source = pd.DataFrame({
        "Target Tercapai":['', 'Persen Target'],
        "% value":[100-sales_target_percentage ,sales_target_percentage]
    })
    
    source_bg = pd.DataFrame({
        "Target Tercapai":['', 'Persen Target'],
        "% value":[100,0]
    })
    
    plot = alt.Chart(source).mark_arc(innerRadius=50, cornerRadius=5).encode(
        theta=alt.Theta('% value:Q'),
        color=alt.Color('Target Tercapai', scale=alt.Scale(domain=['Persen Target', ''], range=['#29b5e8', '#155F7A']), legend=None),
        tooltip=alt.Tooltip('% value:Q', format='.2f')
    ).properties(
        title='Pencapaian Target Penjualan',
        height=310,
        width=200
    )
    
    plot_bg = alt.Chart(source_bg).mark_arc(innerRadius=50).encode(
        theta=alt.Theta('% value:Q'),
        color=alt.Color('Target Tercapai', scale=alt.Scale(domain=['Persen Target', ''], range=['#29b5e8', '#155F7A']), legend=None),
        tooltip=alt.Tooltip('% value:Q', format='.2f')
    ).properties(
        title='Pencapaian Target Penjualan',
        height=310,
        width=200
    )
    
    text = plot.mark_text(align='center', color="#29b5e8", font="Lato", fontSize=25, fontWeight=700, fontStyle="italic").encode(text=alt.value(f'{format_large_number(sales_target_percentage)} %'))
    combined = plot_bg + plot +text
    return co.altair_chart(combined)

def bar_chart_sales_monthly():
    co = st.container(border=True)
    dd_groupby = dd.groupby(['Brand']).agg({'Approx. Total Revenue(INR)':'sum'}).reset_index(drop=False)
    dd_groupby = dd_groupby.rename(columns={'Approx. Total Revenue(INR)':'Jumlah'})
    dd_groupby = dd_groupby.sort_values(['Jumlah'], ascending=[False]).reset_index(drop=True)
    bar = alt.Chart(dd_groupby).mark_bar().encode(
        x=alt.X('Brand:N', sort=alt.SortField(field='Jumlah', order='descending'), axis=None),
        y=alt.Y('Jumlah:Q', axis=None),
        tooltip=[
            alt.Tooltip('Brand:N', title='Nama Barang'),
            alt.Tooltip('Jumlah:Q', title='Penjualan', format='.2s')
        ]
    ).properties(
        height=200,
        title='Penjualan Barang Setiap Brand'
    )
    text=bar.mark_text(baseline='bottom', fontWeight='bold').encode(text='Brand:N')
    combined = text + bar
    return co.altair_chart(combined, use_container_width=True)
    
def sales_yearly():
    co = st.container(border=True)
    dd_year = dd.groupby(['year']).agg({'Approx. Total Revenue(INR)':'sum', 'Quantity Sold (liters/kg)':'sum'}).reset_index(drop=False)
    dd_year = dd_year.rename(columns={'Approx. Total Revenue(INR)':'Sales', 'Quantity Sold (liters/kg)':'Count'})
    dd_year = dd_year.sort_values(['year'], ascending=[True])
    
    line_sales = alt.Chart(dd_year).mark_line().encode(
        x=alt.X('year:N', axis=alt.Axis(labelAngle=0), title=None),
        y=alt.Y('Sales:Q', scale=alt.Scale(zero=False), title='Sales'),
    ).properties(
        title='Banyaknya Penjualan per Tahun (INR)'
    )
    hover = alt.selection_single(
        fields=['year'],
        nearest=True,
        on='mouseover',
        empty='none'
    )
    points = line_sales.transform_filter(hover).mark_circle(size=65)
    tooltips = alt.Chart(dd_year).mark_rule().encode(
        x=alt.X('year:N', axis=alt.Axis(labelAngle=0), title='None'),
        y=alt.Y('Sales:Q', scale=alt.Scale(zero=False), title='Sales'),
        opacity=alt.condition(
            hover, alt.value(0.3), alt.value(0)
        ),
        tooltip=[
            alt.Tooltip('year', title='Tahun'),
            alt.Tooltip('Sales', title='Penjualan')
        ]
    ).add_selection(hover)
    combined = line_sales + points + tooltips
    return co.altair_chart(combined, use_container_width=True)

def count_yearly():
    co = st.container(border=True)
    dd_year = dd.groupby(['year']).agg({'Approx. Total Revenue(INR)':'sum', 'Quantity Sold (liters/kg)':'sum'}).reset_index(drop=False)
    dd_year = dd_year.rename(columns={'Approx. Total Revenue(INR)':'Sales', 'Quantity Sold (liters/kg)':'Count'})
    dd_year = dd_year.sort_values(['year'], ascending=[True])
    
    line_sales = alt.Chart(dd_year).mark_line().encode(
        x=alt.X('year:N', axis=alt.Axis(labelAngle=0), title=None),
        y=alt.Y('Count:Q', scale=alt.Scale(zero=False), title='Barang Terjual'),
    ).properties(
        title='Banyaknya Barang Terjual per Tahun (Satuan)'
    )
    hover = alt.selection_single(
        fields=['year'],
        nearest=True,
        on='mouseover',
        empty='none'
    )
    points = line_sales.transform_filter(hover).mark_circle(size=65)
    tooltips = alt.Chart(dd_year).mark_rule().encode(
        x=alt.X('year:N', axis=alt.Axis(labelAngle=0), title=None),
        y=alt.Y('Count:Q', scale=alt.Scale(zero=False), title='Barang Terjual'),
        opacity=alt.condition(
            hover, alt.value(0.3), alt.value(0)
        ),
        tooltip=[
            alt.Tooltip('year', title='Tahun'),
            alt.Tooltip('Count', title='Barang Terjual')
        ]
    ).add_selection(hover)
    combined = line_sales + points + tooltips
    return co.altair_chart(combined, use_container_width=True)

def sum_product_name():
    co = st.container(border=True)
    dd_product_name = dd.groupby(['Product Name']).agg({'Approx. Total Revenue(INR)':'sum'}).reset_index(drop=False)
    dd_product_name = dd_product_name.rename(columns={'Approx. Total Revenue(INR)':'Sales'}).reset_index(drop=True)
    bar_chart = alt.Chart(dd_product_name).mark_bar().encode(
        x=alt.X('Sales:Q', title=None),
        y=alt.Y('Product Name:N', title='Nama Produk', sort=alt.SortField(field='Sales', order='descending')),
        tooltip=[
            alt.Tooltip('Product Name', title='Nama Produk'),
            alt.Tooltip('Sales', title='Penjualan')
        ]
    ).properties(
        title='Total Penjualan Produk',
        height=350
    )
    return co.altair_chart(bar_chart, use_container_width=True)


# Start Making Dashboard

cols = st.columns([1.7,1.6,1.7])
with cols[1]:
    st.title('SALES DASHBOARD')

cols = st.columns([0.6, 2.4])
with cols[0]:
    progress_donut_chart()
with cols[1]:
    progress_bar()
    bar_chart_sales_monthly()

cols = st.columns(3)
with cols[0]:
    sales_yearly()
with cols[1]:
    count_yearly()
with cols[2]:
    sum_product_name()
    
with st.expander('Ketuk untuk melihat banyaknya transaksi:'):
    count_product()
    count_brand()