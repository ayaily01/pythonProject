import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

class Third:
    def __init__(self):
        pass

    def app(self):
        st.title("Smooth Snake Plot: Ticket Price by Day")
        st.subheader("""
          This dataset could reveal insights into market segmentation, pricing strategies,
           and the financial sustainability of non-blockbuster films in a landscape dominated by high-grossing franchises.
        """)

        # File path for the dataset
        file_path = "cinema.csv"  # Adjust path as needed
        try:
            df = pd.read_csv(file_path)
        except FileNotFoundError:
            st.error(f"Static file '{file_path}' not found. Please check the file path.")  # Error handling
            return

        # Show the full dataset
        st.subheader("View the dataset")
        st.dataframe(df, height=400, width=600)

        st.subheader("Smooth Snake Plot: Average Ticket Price by Day")
        if st.button("Generate Smooth Snake Plot"):
            if "day" in df.columns and "ticket_price" in df.columns:
                # Group by day and calculate the average ticket price for each day
                avg_prices = df.groupby("day")["ticket_price"].mean().reset_index()

                # Apply a rolling average to smooth the line (window size of 3)
                avg_prices['smoothed'] = avg_prices['ticket_price'].rolling(window=3).mean()

                # Plot the smooth snake plot
                fig, ax = plt.subplots()
                ax.plot(avg_prices['day'], avg_prices['smoothed'], color='green', linestyle='-', linewidth=2, label="Smoothed Ticket Price")
                ax.scatter(avg_prices['day'], avg_prices['smoothed'], color='blue', label="Key Points", zorder=5)  # Key points with scatter
                ax.set_xlabel("Day")
                ax.set_ylabel("Smoothed Ticket Price")
                ax.set_title("Smooth Snake Plot: Ticket Price by Day")
                ax.legend()
                ax.grid()

                st.pyplot(fig)
            else:
                st.warning("The dataset must contain 'day' and 'ticket_price' columns.")

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
    app = Third()
    app.app()
