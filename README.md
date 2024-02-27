# amazon-sales-assignment

Amazon Sales Data Analysis

This project focuses on analyzing Amazon sales data to derive insights and perform calculations such as sales tax and net sales for specific regions. The dataset used in this analysis contains information about product sales, order states, selling fees, and timestamps.

Overview

The primary objectives of this project are as follows:

Clean the raw Amazon sales data.
Calculate sales tax for specific states (e.g., Iowa and California).
Compute net sales by deducting taxes and fees from product sales.
Generate summary statistics for net sales, orders, and refunds.

Note: I intentionally left out EDA

Project Structure

main.py: Python script containing the code for data cleaning, processing, analysis, and visualization.
data/: Directory containing the raw data file (amazonsales data.csv) and the cleaned data files (Iowa_california_combined_edited_sorted_v2.xlsx, orders_data_edited_v2.xlsx, refunds_data_edited_v2.xlsx).
README.md: Markdown file providing an overview of the project, instructions for running the code, and any additional information.

Requirements

Python 3.x
Pandas library
NumPy library
datetime module
Usage
Clone the repository to your local machine:

bash
Copy code
git clone https://github.com/KitAndre82/amazon-sales-assignment.git
Navigate to the project directory:

bash
Copy code
cd amazon-sales-analysis
Install the required dependencies:

bash
Copy code
pip install pandas numpy
Run the main.py script:

bash
Copy code
python main.py

After execution, the cleaned and processed data files will be saved in the data/ directory, and summary statistics will be printed to the console.
