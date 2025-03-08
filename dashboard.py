import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

# Load Data
@st.cache_data
def load_data():
    customers_df = pd.read_csv("https://raw.githubusercontent.com/acah21/dataset/refs/heads/main/customers_dataset.csv")
    orders_df = pd.read_csv("https://raw.githubusercontent.com/acah21/dataset/refs/heads/main/orders_dataset.csv")
    order_items_df = pd.read_csv("https://raw.githubusercontent.com/acah21/dataset/refs/heads/main/order_items_dataset.csv")
    return customers_df, orders_df, order_items_df

customers_df, orders_df, order_items_df = load_data()

# Konversi tanggal transaksi
orders_df["order_purchase_timestamp"] = pd.to_datetime(orders_df["order_purchase_timestamp"])
latest_date = orders_df["order_purchase_timestamp"].max()

# Sidebar: Pilih Rentang Waktu
st.sidebar.header("Filter Data")
default_start = latest_date - timedelta(days=365)
date_range = st.sidebar.date_input("Pilih Rentang Waktu", [default_start, latest_date])
orders_df = orders_df[(orders_df["order_purchase_timestamp"] >= pd.to_datetime(date_range[0])) & 
                       (orders_df["order_purchase_timestamp"] <= pd.to_datetime(date_range[1]))]

# Agregasi Data RFM
rfm = orders_df.groupby("customer_id").agg(
    Recency=("order_purchase_timestamp", lambda x: (latest_date - x.max()).days),
    Frequency=("order_id", "count")
).reset_index()

monetary = order_items_df.groupby("order_id")["price"].sum().reset_index()
rfm = rfm.merge(orders_df[["customer_id", "order_id"]], on="customer_id", how="left")
rfm = rfm.merge(monetary, on="order_id", how="left")
rfm = rfm.groupby("customer_id").agg(
    Recency=("Recency", "min"),
    Frequency=("Frequency", "max"),
    Monetary=("price", "sum")
).reset_index()

# Sidebar: Pilih Segmen Pelanggan
rfm["Monetary_Segment"] = pd.qcut(rfm["Monetary"], 4, labels=["Low", "Medium", "High", "Very High"])
selected_segment = st.sidebar.selectbox("Pilih Segmen Pelanggan", ["All"] + list(rfm["Monetary_Segment"].unique()))
if selected_segment != "All":
    rfm = rfm[rfm["Monetary_Segment"] == selected_segment]

# Visualisasi
st.title("📊 Dashboard Analisis RFM")

st.subheader("Distribusi RFM")
fig, axes = plt.subplots(1, 3, figsize=(18, 5))
sns.histplot(rfm["Recency"], bins=30, kde=True, ax=axes[0], color="blue")
axes[0].set_title("Distribusi Recency")
sns.histplot(rfm["Frequency"], bins=30, kde=True, ax=axes[1], color="green")
axes[1].set_title("Distribusi Frequency")
sns.histplot(rfm["Monetary"], bins=30, kde=True, ax=axes[2], color="red")
axes[2].set_title("Distribusi Monetary")
st.pyplot(fig)

st.subheader("Matriks Korelasi")
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(rfm[["Recency", "Frequency", "Monetary"]].corr(), annot=True, cmap="coolwarm", fmt=".2f")
st.pyplot(fig)

st.subheader("Top 10 Kota dengan Pelanggan Terbanyak")
customer_city_counts = customers_df["customer_city"].value_counts().reset_index()
customer_city_counts.columns = ["customer_city", "count"]
fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(y=customer_city_counts["customer_city"][:10], x=customer_city_counts["count"][:10], hue=customer_city_counts["customer_city"].head(10), legend=False, palette="Blues_r")
st.pyplot(fig)

st.subheader("Top 10 Negara Bagian dengan Pelanggan Terbanyak")
customer_state_counts = customers_df["customer_state"].value_counts().reset_index()
customer_state_counts.columns = ["customer_state", "count"]
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(y=customer_state_counts["customer_state"].head(10), x=customer_state_counts["count"].head(10), hue=customer_state_counts["customer_state"].head(10), legend=False, palette="Greens_r")
st.pyplot(fig)

st.write("Sumber data: [E-Commerce Public Dataset](https://github.com/acah21/dataset)")

