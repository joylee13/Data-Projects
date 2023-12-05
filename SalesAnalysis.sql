SELECT * FROM `E-CommerceSales`.`amazon sale report`; 
SELECT * FROM `E-CommerceSales`.`international sale report`;

-- Identify the Most Profittable Cities.
SELECT TopCities, Sales, Revenue, round(`Revenue`*100/(sum(`Revenue`) over ()),2) as PercentageRevenue
FROM(SELECT `ship-city` as TopCities, count(`ship-city`) as Sales, sum(if(`Qty`!= 0,`Amount` ,0)) as Revenue
	 FROM `E-CommerceSales`.`amazon sale report`
	 GROUP BY `ship-city`) A
GROUP BY TopCities
ORDER BY Sales DESC
LIMIT 10;

-- What are the Best Selling Categories? Exclude Cancelled Shipments from Revenue
SELECT `Category`, `Qty`, `Revenue`, round(`Revenue`*100/(sum(`Revenue`) over ()),2) as PercentageRevenue
FROM (SELECT `Category`, count(`Category`) as Qty, sum(if(`Qty`!= 0,`Amount` ,0)) as Revenue
	  FROM `E-CommerceSales`.`amazon sale report`
	  GROUP BY `Category`) A
GROUP BY `Category`
ORDER BY Qty DESC;

-- Months with the highest number of sales in 2022 (amazon report)
CREATE OR REPLACE VIEW Sales_and_Revenue_Months AS
SELECT `Month`, `Qty`,`Revenue`, round(`Revenue`*100/(sum(`Revenue`) over ()),2) as PercentageRevenue, 
	(case when `Month` = "January" or `Month` = "February" or `Month` = "March" then "Q1"
						  when `Month` = "April" or `Month` = "May" or `Month` = "June" then "Q2"
						  when `Month` = "July" or `Month` = "August" or `Month` = "September" then "Q3"
						  when `Month` = "October" or `Month` = "November" or `Month` = "December" then "Q4" end) as Quarter
FROM (SELECT MONTHNAME(`Date`) as Month, 
		   count(if(`Qty`!= 0, EXTRACT(MONTH from `Date`) ,0)) as Qty, 
		   sum(if(`Qty`!= 0,`Amount` ,0)) as Revenue
	  FROM `E-CommerceSales`.`amazon sale report`
	  GROUP BY Month) A
GROUP BY Month
HAVING Month is not null
ORDER BY Qty DESC;

SELECT *
FROM Sales_and_Revenue_Months;

-- Revenue Statistics by Quarters in 2022
SELECT `Quarter`, QuarterlyRevenue, round((`QuarterlyRevenue`-`Original`)*100/`Original`,2) as PercentChange
FROM (SELECT `Quarter`, sum(`Revenue`) as QuarterlyRevenue, lag(sum(`Revenue`),1) over(ORDER BY `Quarter` ASC) as Original
	  FROM Sales_and_Revenue_Months
      GROUP BY `Quarter`) A
GROUP BY `Quarter`
ORDER BY `Quarter` ASC;


-- Top 10 Customers (International Sale Report)
SELECT `CUSTOMER`, count(`CUSTOMER`) as Sales, sum(`GROSS AMT`) as GrossAmt, round(avg(`GROSS AMT`),2) as AvgAmt
FROM `E-CommerceSales`.`international sale report`
GROUP BY `CUSTOMER`
ORDER BY GrossAmt DESC
LIMIT 10;

-- Join International and Amazon Reports to get Categories
CREATE OR REPLACE VIEW Joint_Report AS
SELECT A.`Date`, A.`Style`, `Category`, `ship-city`, B.`CUSTOMER`, B.`GROSS AMT`
FROM `E-CommerceSales`.`amazon sale report` A
RIGHT JOIN `E-CommerceSales`.`international sale report` B on A.`Style` = B.`Style`;

-- Revenue By City, Customer and Category
WITH CTE AS (
	SELECT `ship-city`, `CUSTOMER`, `Category`, count(`Category`) as QtyPurchased, sum(`GROSS AMT`) as GrossAmt
	FROM Joint_Report
	GROUP BY `ship-city`, `CUSTOMER`, `Category`
	HAVING `Category` is not null
	ORDER BY GrossAmt DESC
	)

SELECT *
FROM CTE
LIMIT 20;

