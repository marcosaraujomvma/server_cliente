CREATE TABLE rastros
(
  id serial NOT NULL,
  id_medidor text,
  leitura text,
  ts_medidor text,
  ts_server timestamp without time zone DEFAULT now(),
  CONSTRAINT rastros_pkey PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE rastros
  OWNER TO postgres;
