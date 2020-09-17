CREATE TABLE tb_transformadores (
   id serial PRIMARY KEY,
   nome VARCHAR (255) NOT NULL,
   subestacao char(3) UNIQUE NOT NULL
);

CREATE TABLE tb_transformadores_num_serie (
  id_transformador INT UNIQUE NOT NULL,
  num_serie VARCHAR(20),
  FOREIGN KEY (id_transformador)
      REFERENCES tb_transformadores (id)
);