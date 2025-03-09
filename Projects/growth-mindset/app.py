import streamlit as st
import pandas as pd
from io import BytesIO
import os

st.set_page_config(page_title="Data Sweeper", layout="wide")
st.title("🚀 Data Sweeper")
st.write("Transform your files between CSV & Excel Formats with built-in data cleaning & visualization!")

# File Uploader
uploaded_files = st.file_uploader(
    "📂 Upload Files (CSV or Excel)", accept_multiple_files=True, type=["csv", "xlsx"]
)

if uploaded_files:
    for file in uploaded_files:
        # extract extension of file
        file_ext = os.path.splitext(file.name)[-1].lower()

        try:
            if file_ext == ".csv":
                df = pd.read_csv(file, encoding="latin1")
            elif file_ext == ".xlsx":
                df = pd.read_excel(file)
            else:
                st.error(f"Unsupported File Type: {file_ext}")
                continue
        except Exception as e:
            st.error(f"⚠️ Error reading file {file.name}: {e}")
            continue

        # Display File Info
        st.markdown(f"### 📄 **{file.name}**  \n📏 **Size:** {file.size / 1024:.2f} KB")
        st.dataframe(df.head())

        # options for data cleaning
        st.subheader("🛠️ Data Cleaning Options")

        if st.checkbox(f"Clean Data for {file.name}"):
            col1, col2 = st.columns(2)

            with col1:
                if st.button(f"Remove Duplicates from {file.name}"):
                    df.drop_duplicates(inplace=True)
                    st.write("Duplicates Removed!")

            with col2:
                if st.button(f"Fill Missing Values for {file.name}"):
                    numeric_cols = df.select_dtypes(include="number").columns
                    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                    st.write("Missing Values have been Filled!")

        # choose specific columns to keep or convert
        st.subheader("Select Columns to Convert")
        columns = st.multiselect(f"Select Columns for {file.name}",df.columns)
        df = df[columns]

        # Create visualizations
        st.subheader("📊 Data Visualization")
        if st.checkbox(f"Show Visualization for {file.name}"):
            st.bar_chart(df.select_dtypes(include="number").iloc[:,:2])

        # File Conversion Section
        st.subheader("🔄 File Conversion")
        conversion_type = st.radio(f"Convert {file.name} to:", ["CSV", "Excel"], key=file.name)

        if st.button(f"Convert & Download {file.name}"):
            buffer = BytesIO()

            new_file_name = file.name.replace(file_ext, f".{conversion_type.lower()}")

            if conversion_type == "CSV":
                df.to_csv(buffer, index=False)
                file_name = file.name.replace(file_ext, ".csv")
                mime_type = "text/csv"

            elif conversion_type == "Excel":
                df.to_excel(buffer, index=False)
                file_name = file.name.replace(file_ext, ".xlsx")
                mime_type = "application/vnd.openxmlformat-officedocument.spreadsheetml.sheet"
            buffer.seek(0)

            # donwnload button
            st.download_button(
                label=f"📥 Download {new_file_name}",
                data=buffer,
                file_name=new_file_name,
                mime=mime_type
            )

st.info("📌 Tip: You can upload multiple files at once!")