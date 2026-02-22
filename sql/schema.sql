-- It will have 2 tables: fact_prices and dim_assets (it's fact because it save numbers and events, Dimensions because save caracteristics)

-- drop table if exists make sure  is just 1 table. fact_prices come first because it is dependent of dim_assets
DROP TABLE IF EXISTS fact_prices;
DROP TABLE IF EXISTs dim_assets;

CREATE TABLE dim_assets (
    id_assets INTEGER PRIMARY KEY AUTOINCREMENT,
    ticker VARCHAR(10) UNIQUE NOT NULL,
    sector VARCHAR(15) NOT NULL
);

CREATE TABLE fact_prices (
    id_prices INTEGER PRIMARY KEY AUTOINCREMENT,
    id_assets INTEGER NOT NULL,
    date DATE NOT NULL,
    adj_close DECIMAL(10,2) NOT NULL, --DECIMAL(total de numeros, números depois da virgula)
    FOREIGN KEY (id_assets) REFERENCES dim_assets (id_assets) 
);