import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px


def app():
    st.title('Data Plotting')

    st.write('This is the `Data Plotting` page of the multi-page app.')

    # Read data from CSV
    plot_data = pd.read_csv('data.csv')

    # Streamlit line chart
    st.write("### Line Chart")
    st.line_chart(plot_data['sepal length (cm)'])

    # Streamlit bar chart
    st.write("### Bar Chart")
    st.bar_chart(plot_data['sepal width (cm)'])

    # Streamlit area chart
    st.write("### Area Chart")
    st.area_chart(plot_data['petal width (cm)'])

    # Streamlit pie chart
    st.write("### Pie Chart")
    fig_pie = px.pie(plot_data, names='class', title='Class Distribution')
    st.plotly_chart(fig_pie)

    # # Matplotlib for more customization
    # fig, ax = plt.subplots()
    # ax.plot(plot_data['sepal length (cm)'], plot_data['sepal width (cm)'])
    # st.pyplot(fig)


if __name__ == "__main__":
    app()
