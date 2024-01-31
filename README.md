# Data-Projects
Data analysis and visualization projects utilizing SQL, Tableau and Python skills.

## [Washington's Electric Vehicle Population, Tableau Dashboard](https://public.tableau.com/app/profile/joy.lee2924/viz/Book1_16981999466620/WashingtonE-Vehicles)
Gathered data from the US GSA to provide insights for clients interested in understanding the e-vehicle population in Washington with visualizations of:
 - Average Base MSRP for popular makes
 - Total Registered Vehicles in the N largest zipcodes (with dynamic parameter to adjust N)
 - Top 25 most commonly owned e-vehicle models
 - E-vehicle ownership trends over time

## [E-Commerce Sales Performance Report, SQL](SalesAnalysis.sql)
Utilized MySQL to analyze a Kaggle dataset on 2022 E-commerce sales. Used skills such as joins, views, case statements, CTE's, aggregate functions and more to answer the following business questions:
- What did our sales look like in 2022?
- Which cities are the most profitable?
- What are our best selling categories?
- How did sales vary from quarter to quarter?
- Who are our top customers?

## [Sales Performance Dashboard, Tableau](https://public.tableau.com/app/profile/joy.lee2924/viz/SalesDashboard_17065887203140/SalesDashboard)
Summarized data collected from [Sales Analysis queries](SalesAnalysis.sql) into a Tableau Dashboard highlighting:
- Total sales revenue
- Total quantity of items sold
- Percent sales by category
- Cities with the highest sales
- Top and bottom categories by quantity

## [TMDB Web Scraper, Python](https://github.com/joylee13/TMDB_scraper.git)
- Implemented 3 parsing methods with the Python library scrapy to scrape The Movie Database for NBC's "The Good Place" actors and their credits
- Leveraged pandas functions to analyze the scraped dataset for movies and tv shows that share multiple actors with "The Good Place"
- Plotted the 10 most similar movies and tv shows, based on number of shared actors, in a plotly bar graph visualization

## [Netflix Blendz, Python](https://github.com/joylee13/pic16b_project)
- Designed and implemented a multi page web application using HTML, CSS and flask
- Developed a data management system with sqlite3; wrote queries to fetch user information and create tables inside the database
- Sorted through user watch history to create visualizations for top genres and minutes watched using plotly
