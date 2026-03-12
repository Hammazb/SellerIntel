import os
import pandas as pd
import duckdb

con = duckdb.connect("sellerintel.db")

customers_df = pd.read_csv('data/raw/olist_customers_dataset.csv')
con.execute("CREATE TABLE raw_customers AS SELECT * FROM customers_df")
print(con.execute("SELECT * FROM raw_customers LIMIT 5").fetchdf())

geo_location_df = pd.read_csv('data/raw/olist_geolocation_dataset.csv')
con.execute("CREATE TABLE raw_geo_location AS SELECT * FROM geo_location_df")
print(con.execute("SELECT * FROM raw_geo_location LIMIT 5").fetchdf())

order_items_df = pd.read_csv('data/raw/olist_order_items_dataset.csv')
con.execute("CREATE TABLE raw_order_items AS SELECT * FROM order_items_df")
print(con.execute("SELECT * FROM raw_order_items LIMIT 5").fetchdf())

order_payments_df = pd.read_csv('data/raw/olist_order_payments_dataset.csv')
con.execute("CREATE TABLE raw_order_payments AS SELECT * FROM order_payments_df")
print(con.execute("SELECT * FROM raw_order_payments LIMIT 5").fetchdf())

order_reviews_df = pd.read_csv('data/raw/olist_order_reviews_dataset.csv')
con.execute("CREATE TABLE raw_order_reviews AS SELECT * FROM order_reviews_df")
print(con.execute("SELECT * FROM raw_order_reviews LIMIT 5").fetchdf())

orders_df = pd.read_csv('data/raw/olist_orders_dataset.csv')
con.execute("CREATE TABLE raw_orders AS SELECT * FROM orders_df")
print(con.execute("SELECT * FROM raw_orders LIMIT 5").fetchdf())

products_df = pd.read_csv('data/raw/olist_products_dataset.csv')
con.execute("CREATE TABLE raw_products AS SELECT * FROM products_df")
print(con.execute("SELECT * FROM raw_products LIMIT 5").fetchdf())

sellers_df = pd.read_csv('data/raw/olist_sellers_dataset.csv')
con.execute("CREATE TABLE raw_sellers AS SELECT * FROM sellers_df")
print(con.execute("SELECT * FROM raw_sellers LIMIT 5").fetchdf())

translations_df = pd.read_csv('data/raw/product_category_name_translation.csv')
con.execute("CREATE TABLE raw_category_translation AS SELECT * FROM translations_df")
print(con.execute("SELECT * FROM raw_category_translation LIMIT 5").fetchdf())
