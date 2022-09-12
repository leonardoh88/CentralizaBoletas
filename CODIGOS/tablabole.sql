create table boleta (id Serial, rut text, consumo text, precio int);

insert into boleta (rut, consumo, precio) values
  ('192223331', 'gas', 25000);

select * from boleta;
