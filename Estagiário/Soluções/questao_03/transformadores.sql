UPDATE tb_transformadores_num_serie SET num_serie = substr(num_serie, 1, 2) || '.' || substr(num_serie, 3, 4) || '.' || substr(num_serie, 7, 4) || '-' || substr(num_serie, 11, 4) || '/' || substr(num_serie, 15, 2);