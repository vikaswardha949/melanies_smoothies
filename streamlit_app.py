# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col
import requests


# Write directly to the app
st.title("My Parents New Healthy Dinner")
st.write(
    """Choose the fruits you want in your custom Smoothie"""
)

cnx =st.connection("snowflake")
session = cnx.session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
st.dataframe(data=my_dataframe, use_container_width=True

ingredients_list = st.multiselect(
    'Choose up to 5 ingredients:' 
,    my_dataframe
,    max_selection = 5
)

if ingredients_list:
    
    ingredients_string = ''

    for fruit_chosen in  ingredients_list:
        ingredients_string += fruit_chosen + ' '

        search_on=pd_df.loc[pd_df['FRUIT_NAME'] == fruit_chosen, 'SEARCH_ON'].iloc[0]
        st.write('The search value for ', fruit_chosen,' is ', search_on, '.')

        st.subheader(fruit_chosen + ' Nutrition Information ')
        smoothiefroot_response = requests.get("https://my.smoothiefroot.com/api/fruit/watermelon")
        st_df=st.dataframe(data=smoothiefroot_response.json(),  use_container_width=True)
    st.write(ingredients_string);

my_insert_stmt = """ insert into smoothies.public.orders(ingredients)
        values('""" + ingredients_string + """')"""

st.write(my_insert_stmt)



#st.write(my_insert_stmt)
time_to_insert = st.button('Submit Order')


if time_to_insert:
   session.sql(my_insert_stmt).collect()
   st.success('Your Smoothie is ordered!', icon ="✅") 
import requests
smoothiefroot_response = requests.get("https://my.smoothiefroot.com/api/fruit/watermelon")
sf_df = st.text(smoothiefroot_response.json(), use_container_width=True)








            



