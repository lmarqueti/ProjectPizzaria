create database erp;

use erp;


create table cadastros(
id int auto_increment not null primary key,
nome varchar(50) not null,
senha varchar(20) not null,
nivel int not null
  
);
 
insert into cadastros (nome,senha,nivel) values ('admin', 'admin', 2);
insert into cadastros (nome,senha,nivel) values ('marqueti', '1234', 2);
insert into cadastros (nome,senha,nivel) values ('bruxo', 'ronaldo', 2);
 
create table produtos(
id int auto_increment not null primary key,
nome varchar(100) not null,
ingredientes varchar(1000),
grupo varchar(100),
preco float
 
);
 drop table pedidos;
 
create table pedidos(
id int not null primary key auto_increment,
nome varchar(100) not null,
ingredientes varchar(1000),
grupo varchar(100),
localEntrega varchar(500),
observacoes varchar(1000),
qtd int not null
);

select * from produtos;
 
insert into pedidos (nome, ingredientes, grupo, localEntrega, observacoes, qtd) values ('pizza de mussarela', 'mussarela', 'pizzas', '', 'sem cebola',1);
insert into pedidos (nome, ingredientes, grupo, localEntrega, observacoes,qtd) values ('coca', '', 'bebidas', '', '',1);
insert into pedidos (nome, ingredientes, grupo, localEntrega, observacoes,qtd) values ('pizza de mussarela', 'mussarela', 'pizzas', '', 'sem cebola',1);
insert into pedidos (nome, ingredientes, grupo, localEntrega, observacoes,qtd) values ('coca', '', 'bebidas', '', '');
insert into pedidos (nome, ingredientes, grupo, localEntrega, observacoes,qtd) values ('pizza de mussarela', 'mussarela', 'pizzas', '', 'sem cebola',1);
insert into pedidos (nome, ingredientes, grupo, localEntrega, observacoes,qtd) values ('coca', '', 'bebidas', '', '',1);

select * from pedidos;
create table estatisticaVendido(
 
id int not null primary key auto_increment,
nome varchar(100) not null,
grupo varchar(100),
preco float
	
 
);
 
insert into estatisticaVendido(nome, grupo, preco) values ('pizza de mussarela', 'pizzas', 34.90);
 
insert into estatisticaVendido(nome, grupo, preco) values ('coca', 'bebidas', 6);
 
insert into estatisticaVendido(nome, grupo, preco) values ('pizza de portuguesa', 'pizzas', 34.90);
 
insert into estatisticaVendido(nome, grupo, preco) values ('suco de laranja', 'pizzas', 7);

insert into estatisticaVendido(nome, grupo, preco) values ('suco de laranja', 'pizzas', 7);
insert into estatisticaVendido(nome, grupo, preco) values ('pizza de portuguesa', 'pizzas', 34.90);
insert into estatisticaVendido(nome, grupo, preco) values ('coca', 'bebidas', 6);
 
insert into estatisticaVendido(nome, grupo, preco) values ('coca', 'bebidas', 6);
 
insert into estatisticaVendido(nome, grupo, preco) values ('coca', 'bebidas', 6);
 
select * from estatisticavendido;

select * from produtos;

select * from cadastros;