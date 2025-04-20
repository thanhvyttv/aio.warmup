import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

st.title("Bài 1 - Vẽ Đồ thị hàm số cơ bản")


def func(func_name, x):
    if func_name == "sin":
        return np.sin(x)
    elif func_name == "cos":
        return np.cos(x)
    elif func_name == "exp":
        return np.exp(x)
    else:
        return np.log(np.abs(x) + 1e-8)


def generate_graph(func_name, start, end, num_point=400):
    x = np.linspace(start, end, num_point)
    y = func(func_name, x)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(x, y, label=f"y = {func_name}(x)")
    ax.set_title(f"Đồ thị hàm số y = {func_name}(x) trên đoạn [{start}, {end}]")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)


# Create selection in UI
option = st.selectbox("Select the function name", ("sin", "cos", "exp", "log"))

start_val, end_val = st.slider(
    "Select range of x value:", -10.0, 10.0, (-10.0, 10.0), key="create_slider_1"
)

if st.button("Generate Exercise 1:"):
    generate_graph(option, start_val, end_val)

# Bài 2
st.title("Bài 2: So sánh hai hàm số")

option1 = st.selectbox("Select the function name 1", ("sin", "cos", "exp", "log"))
option2 = st.selectbox("Select the function name 2", ("sin", "cos", "exp", "log"))


def generate_2_graphs(func_name1, func_name2, start, end, num_point=400):
    x = np.linspace(start, end, num_point)
    y1 = func(func_name1, x)
    y2 = func(func_name2, x)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(x, y1, label=f"y = {func_name1}(x)")
    ax.plot(x, y2, label=f"y = {func_name2}(x)")
    ax.set_title(
        f"Đồ thị hàm số y = {func_name1}(x) và y = {func_name2}(x) trên đoạn [{start}, {end}]"
    )
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)


start_val2, end_val2 = st.slider(
    "Select range of x value:", -10.0, 10.0, (-10.0, 10.0), key="create_slider_2"
)

if st.button("Generate Exercise 2"):
    generate_2_graphs(option1, option2, start_val2, end_val2)

# Bài 3 - Vẽ đồ thị hàm bậc 2
st.title("Bài 3: Vẽ đồ thị hàm bậc 2")
st.subheader("y = ax² + bx + c")


def func_3(a, b, c, x):
    return a * x**2 + b * x + c


a = st.number_input("Input number a:", value=1.0, step=0.1)
b = st.number_input("Input number b:", value=1.0, step=0.1)
c = st.number_input("Input number c:", value=1.0, step=0.1)

min_x, max_x = st.slider(
    "Select min x value", -10.0, 10.0, (-10.0, 10.0), key="x_value"
)


def generate_graph_3(a, b, c, start, end, num_point=400):
    x = np.linspace(start, end, num_point)
    y = func_3(a, b, c, x)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(x, y, label="y = ax² + bx + c")
    ax.set_title(f"Đồ thị hàm số y = ax² + bx + c trên đoạn [{start}, {end}]")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)


if st.button("Calculate"):
    generate_graph_3(a, b, c, min_x, max_x)


# Bài 4
st.title("Bài 4 - Tương tác với Slider để khảo sát đồ thị")


a4 = st.slider("Select number a", -5.0, 5.0, 1.0, 0.1, key="a_value")
b4 = st.slider("Select number b", -5.0, 5.0, 1.0, 0.1, key="b_value")
c4 = st.slider("Select number c", -5.0, 5.0, 1.0, 0.1, key="c_value")

generate_graph_3(a4, b4, c4, -10, 10)

# Bài 5 Heatmap cho hàm z = x² + y²
st.title("Bài 5: Heatmap cho hàm z = x² + y²")
min_val = st.slider("Giá trị nhỏ nhất cho x và y:", -10.0, 10.0, -5.0, key="min_val")
max_val = st.slider("Giá trị lớn nhất cho x và y:", -10.0, 10.0, 5.0, key="max_val")
num_points = st.slider("Giá trị numpoints", 0, 100, 10, key="num_points")
x = np.linspace(min_val, max_val, num_points)
y = np.linspace(min_val, max_val, num_points)
X, Y = np.meshgrid(x, y)

Z = X**2 + Y**2

# Create dataframe
df_z = pd.DataFrame(Z)

# Create HeatMap by Seaborn
fig, ax = plt.subplots()
sns.heatmap(df_z, annot=False, cmap="viridis", cbar_kws={"label": "z value"}, ax=ax)
ax.set_title("Heatmap của hàm $z = x^2 + y^2$")
ax.set_xlabel("X value")
ax.set_ylabel("Y value")
ax.invert_yaxis()

st.pyplot(fig)
