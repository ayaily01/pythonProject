import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


class First:
    def __init__(self):
        self.data = None

    def load_data(self, file_path):
        try:
            self.data = pd.read_csv(file_path)
            # Convert numeric months to month names
            self.data["month"] = pd.to_datetime(self.data["month"], format='%m').dt.strftime('%B')
        except FileNotFoundError:
            st.error(f"File '{file_path}' not found.")
        except Exception as e:
            st.error(f"An error occurred while loading the data: {e}")

    def create_bar_chart(self):
        if self.data is not None:
            fig, ax = plt.subplots(figsize=(10, 6))
            # Group by month and sum tickets sold if necessary
            grouped_data = self.data.groupby("month")["tickets_sold"].sum().reindex([
                "January", "February", "March", "April", "May", "June",
                "July", "August", "September", "October", "November", "December"
            ])
            ax.bar(grouped_data.index, grouped_data.values, color="skyblue")
            ax.set_xlabel("Month")
            ax.set_ylabel("Tickets Sold")
            ax.set_title("Monthly Tickets Sold")
            plt.xticks(rotation=45)
            st.pyplot(fig)

    def app(self):
        st.title("Bar Chart of Tickets Sold by Month")
        st.subheader("""

The analysis of 2018s ticket sales provides an opportunity to explore a critical issue in cinema economics: how blockbuster films, driven by extensive 
fan bases and marketing strategies, impact the overall ticket sales distribution across different genres and regions..
                """)
        file_path = "cinema.csv"  # Path to the uploaded file
        self.load_data(file_path)

        if self.data is not None:
            st.write("Dataset Preview:")
            st.write(self.data.head())

            st.write("Bar Chart:")
            self.create_bar_chart()

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


if __name__ == "__main__":
    app = First()
    app.app()
