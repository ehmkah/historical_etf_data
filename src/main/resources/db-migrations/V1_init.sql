CREATE TABLE countries (
                           id SERIAL PRIMARY KEY,
                           countryname VARCHAR(100) NOT NULL
);

CREATE TABLE etfs (
                     id SERIAL PRIMARY KEY,
                     fond_name TEXT NOT NULL,
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
                         allocation_percentage DECIMAL(5,2) NOT NULL, -- e.g., 5.25 = 5.25%
                         FOREIGN KEY (valuation_date_id) REFERENCES valuation_dates(id),
                         FOREIGN KEY (etf_id) REFERENCES etfs(id),
                         FOREIGN KEY (stock_id) REFERENCES stocks(id)
);

select * from stocks