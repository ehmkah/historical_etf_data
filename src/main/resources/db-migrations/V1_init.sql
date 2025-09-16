CREATE TABLE countries (
                           id SERIAL PRIMARY KEY,
                           countryname text NOT NULL UNIQUE
);

CREATE TABLE etfs (
                     id SERIAL PRIMARY KEY,
                     fond_name TEXT NOT NULL UNIQUE ,
                     isin TEXT NOT NULL UNIQUE
);
CREATE TABLE stocks (
                     id SERIAL PRIMARY KEY,
                     stock_name TEXT NOT NULL,
                     isin TEXT NOT NULL UNIQUE,
                     country_id INT NOT NULL,
                     FOREIGN KEY (country_id) REFERENCES countries(id)
);

CREATE TABLE valuation_dates (
                                id SERIAL PRIMARY KEY,
                                valuation_datetime TIMESTAMP NOT NULL
);

CREATE TABLE holdings (
                         id SERIAL PRIMARY KEY,
                         valuation_date_id INTEGER NOT NULL,
                         etf_id INTEGER NOT NULL,
                         stock_id INTEGER NOT NULL,
                         allocation_percentage DECIMAL(5,2) NOT NULL,
                         FOREIGN KEY (valuation_date_id) REFERENCES valuation_dates(id),
                         FOREIGN KEY (etf_id) REFERENCES etfs(id),
                         FOREIGN KEY (stock_id) REFERENCES stocks(id)
);

drop table holdings;
drop table stocks;
drop table countries;
drop table valuation_dates;
drop table etfs;
drop table countries;
commit
