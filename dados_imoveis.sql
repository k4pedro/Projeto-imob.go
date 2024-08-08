create database dados;
use dados;

create table `cadastrados` (
`numero_do_contribuinte` varchar(12) not null,
`nome_de_logradouro_do_imovel` varchar(40) not null,
`numero_do_imovel` int(4) not null,
`complemento_do_imovel` varchar(20) not null,
`bairro_do_imovel` varchar(30) not null,
`cep_do_imovel` varchar(9) not null,
`area_do_terreno` int(6) not null,
`valor_do_m2_do_terreno` int(6) not null,
primary key (`numero_do_contribuinte`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

select * from cadastrados