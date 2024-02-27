#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from datetime import datetime

# Function to map full US state names to abbreviations or mark as International if not found
def map_state_to_abbrev(state, state_map):
    if pd.isna(state):
        return "Unknown"
    state_title = state.title()
    return state_map.get(state_title, "International")

# Function to calculate sales tax
def calculate_sales_tax(amount, rate):
    return round(amount - (amount / (1 + rate)), 2)

# Load data
df = pd.read_csv('/Users/andrew/Downloads/internship files/amazonsales data.csv')

# Define US state abbreviation mapping
us_state_to_abbrev = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
    "District of Columbia": "DC",
    "American Samoa": "AS",
    "Guam": "GU",
    "Northern Mariana Islands": "MP",
    "Puerto Rico": "PR",
    "United States Minor Outlying Islands": "UM",
    "U.S. Virgin Islands": "VI",
}

# Clean 'order state' column and add 'Order_states' column
df['Order_states'] = df['order state'].apply(lambda x: map_state_to_abbrev(x, us_state_to_abbrev))

# Separate data for Iowa and California
IA_data = df[df['Order_states'] == 'IA'].copy()
CA_data = df[df['Order_states'] == 'CA'].copy()

# Calculate sales tax for Iowa and California
IA_data['sales_tax_state'] = calculate_sales_tax(IA_data['product sales'], 0.06)
CA_data['sales_tax_state'] = calculate_sales_tax(CA_data['product sales'], 0.0725)

# Calculate average local sales tax for Iowa and California
IA_data['sales_tax_avg_local'] = calculate_sales_tax(IA_data['product sales'], 0.0094)
CA_data['sales_tax_avg_local'] = calculate_sales_tax(CA_data['product sales'], 0.0157)

# Calculate net sales
IA_data['net_sales'] = IA_data['product sales'] + IA_data['selling fees'] - IA_data['sales_tax_state'] - IA_data['sales_tax_avg_local']
CA_data['net_sales'] = CA_data['product sales'] + CA_data['selling fees'] - CA_data['sales_tax_state'] - CA_data['sales_tax_avg_local']

# Combine Iowa and California data
ia_ca_data = pd.concat([IA_data, CA_data])

# Sort data by date
ia_ca_data['date/time'] = pd.to_datetime(ia_ca_data['date/time'])
ia_ca_data = ia_ca_data.sort_values(by='date/time')

# Save cleaned and processed data to Excel
ia_ca_data.to_excel('/Users/andrew/Downloads/internship files/Iowa_california_combined_edited_sorted_v2.xlsx', index=False)

# Summary statistics
net_sales_total = ia_ca_data['net_sales'].sum()
total_orders = ia_ca_data[ia_ca_data['type'] == 'Order']['net_sales'].sum()
total_refunds = ia_ca_data[ia_ca_data['type'] == 'Refund']['product sales'].sum()

# Save orders and refunds data to Excel
orders = ia_ca_data[ia_ca_data['type'] == 'Order']
refunds = ia_ca_data[ia_ca_data['type'] == 'Refund']
orders.to_excel('/Users/andrew/Downloads/internship files/orders_data_edited_v2.xlsx', index=False)
refunds.to_excel('/Users/andrew/Downloads/internship files/refunds_data_edited_v2.xlsx', index=False)

# Print summary statistics
print("Total net sales:", net_sales_total)
print("Total sales revenue from orders:", total_orders)
print("Total refunds:", total_refunds)


# In[ ]:




