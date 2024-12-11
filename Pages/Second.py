import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Second:
    def __init__(self):
        pass

    def app(self):
        st.title("Scatter Plot with Regression Line")
        st.subheader("""
            By examining a dataset of ticket sales, including metrics on pre-sale purchases, theater locations, 
            and post-release performance, we can assess how such major releases influence cinema attendance patterns, 
            competition with smaller films, and the shifting dynamics in audience behavior.

        """)

        # File path for the dataset
        file_path = "cinema.csv"  # Adjust path as needed
        try:
            df = pd.read_csv(file_path)
        except FileNotFoundError:
            st.error(f"Static file '{file_path}' not found. Please check the file path.")  # Error handling
            return

        # Slider for row selection with a maximum range of 0 to 500
        st.subheader("View the dataset")
        max_range = min(500, len(df))  # Ensure max range does not exceed dataset length
        row_range = st.slider("Select range of rows to display (affects the scatter plot):", 0, max_range, (0, 10))
        selected_rows = df.iloc[row_range[0]:row_range[1] + 1]


        st.subheader("Scatter Plot with Regression Line")  # Plot section title
        if st.button("Generate Scatter Plot"):
            if "day" in selected_rows.columns and "total_sales" in selected_rows.columns:
                x = selected_rows["day"].dropna()
                y = selected_rows["total_sales"].dropna()

                # Ensure x and y have the same length
                min_length = min(len(x), len(y))
                x, y = x[:min_length], y[:min_length]

                # Regression line calculation
                coefficients = np.polyfit(x, y, 1)
                regression_line = np.polyval(coefficients, x)

                # Plot the graph
                fig, ax = plt.subplots()
                ax.scatter(x, y, color='blue', alpha=0.5, label="Data Points")
                ax.plot(x, regression_line, color='red',
                        label=f"Regression Line: y = {coefficients[0]:.2f}x + {coefficients[1]:.2f}")
                ax.set_xlabel("Day")
                ax.set_ylabel("Total Sales")
                ax.set_title("Scatter Plot: Total Sales vs Day")
                ax.legend()
                ax.grid()

                st.pyplot(fig)
            else:
                st.warning("The dataset must contain 'day' and 'total_sales' columns.")



        st.markdown(
            """
            <style>
            h1 {
                color: pink;
                font-size: 30px;
                text-align: center;
                font-family: Avantgarde, TeX Gyre Adventor, URW Gothic L, sans-serif;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )


# Run the app
if __name__ == "__main__":
    app = Second()
    app.app()
