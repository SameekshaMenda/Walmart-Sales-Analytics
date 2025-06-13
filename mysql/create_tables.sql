CREATE DATABASE IF NOT EXISTS walmart_sales;

USE walmart_sales;



CREATE TABLE sales_train (
    Store INT,
    Dept INT,
    Date DATE,
    Weekly_Sales FLOAT,
    IsHoliday BOOLEAN
);




CREATE TABLE stores (
  Store INT PRIMARY KEY,
  Type VARCHAR(10),
  Size INT
);

CREATE TABLE features (
  Store INT,
  Date DATE,
  Temperature FLOAT,
  Fuel_Price FLOAT,
  MarkDown1 FLOAT,
  MarkDown2 FLOAT,
  MarkDown3 FLOAT,
  MarkDown4 FLOAT,
  MarkDown5 FLOAT,
  CPI FLOAT,
  Unemployment FLOAT,
  IsHoliday BOOLEAN
);


CREATE TABLE sales_test (
  Store INT,
  Dept INT,
  Date DATE,
  IsHoliday BOOLEAN
);
