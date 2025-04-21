from io import StringIO
import streamlit as st
import pandas as pd
import pygwalker as pyg
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import streamlit.components.v1 as components

st.title("Phân tích dữ liệu từ file CSV")

uploaded_file = st.file_uploader("Chọn file CSV", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("Dữ liệu ban đầu")
    st.dataframe(df.head())
    st.write("Số dòng:", df.shape[0])
    st.write("Số cột:", df.shape[1])
    st.subheader("Thông tin mô tả dữ liệu")
    st.write("Các thống kê cơ bản:")
    st.dataframe(df.describe())
    st.write("Kiểu dữ liệu:")
    st.write(df.dtypes)
    st.write("Số giá trị thiếu:")
    st.write(df.isnull().sum())
    st.subheader("Phân tích dữ liệu tương tác với PygWalker ")
    pyg_html = pyg.walk(df, return_html=True, env="Streamlit")
    components.html(pyg_html, height=600, scrolling=True)

    st.subheader("Lọc dữ liệu")
    columns_to_filter = st.multiselect("Chọn các cột để lọc:", df.columns)

    filtered_df = df.copy()
    for col in columns_to_filter:
        unique_values = df[col].unique()
        selected_values = st.multiselect(
            f"Chọn giá trị cho cột '{col}':", unique_values
        )
        if selected_values:
            filtered_df = filtered_df[filtered_df[col].isin(selected_values)]

    if filtered_df.shape[0] < df.shape[0]:
        st.subheader("Dữ liệu đã lọc")
        st.dataframe(filtered_df)

        # Cho phép tải dữ liệu đã lọc
        csv_buffer = StringIO()
        filtered_df.to_csv(csv_buffer, index=False)
        st.download_button(
            label="Tải xuống dữ liệu đã lọc dưới dạng CSV",
            data=csv_buffer.getvalue(),
            file_name="filtered_data.csv",
            mime="text/csv",
        )

    st.subheader("Biểu đồ tương quan")
    numerical_cols = df.select_dtypes(include=np.number).columns.tolist()
    if numerical_cols:
        st.info("Chọn các cột số để vẽ biểu đồ tương quan (nếu có).")
        cols_for_corr = st.multiselect(
            "Chọn các cột số:",
            numerical_cols,
            default=numerical_cols[: min(len(numerical_cols), 5)],
        )

        if len(cols_for_corr) > 1:
            corr_matrix = df[cols_for_corr].corr()
            fig_corr, ax_corr = plt.subplots()
            sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", ax=ax_corr)
            st.pyplot(fig_corr)
        else:
            st.warning("Vui lòng chọn ít nhất hai cột số để vẽ biểu đồ tương quan.")
    else:
        st.info("Không có cột số nào trong dữ liệu để vẽ biểu đồ tương quan.")
