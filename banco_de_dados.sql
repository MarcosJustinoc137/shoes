CREATE TABLE customer(
	id_customer SERIAL PRIMARY KEY,
	customer_name VARCHAR(50) NOT NULL,
	customer_number VARCHAR(20),
	maker VARCHAR(100)
);

CREATE TABLE customer_seam(
	id_customer_seam SERIAL PRIMARY KEY,
	customer_id INTEGER NOT NULL,
	name_seam VARCHAR(20) NOT NULL,
	valor NUMERIC(10,2) NOT NULL,

	FOREIGN KEY (customer_id)
		REFERENCES customer(id_customer),
	CHECK (name_seam IN ('cordinha','string','costura lateral'))
);

CREATE TABLE request(
	id_request SERIAL PRIMARY KEY,
	customer_seam_id INTEGER NOT NULL,
	date_request TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	amount INTEGER NOT NULL,

	FOREIGN KEY (customer_seam_id)
		REFERENCES customer_seam(id_customer_seam)
);