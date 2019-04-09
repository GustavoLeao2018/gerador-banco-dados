create database petshop;
use petshop;

create table racas(
    idRaca integer not null  auto_increment primary key,
    raca varchar(50) not null
);

create table especies(
    idEspecie integer not null auto_increment primary key,
    especie varchar(50) not null
);

create table animais(
    idAnimais integer not null auto_increment primary key,
    nome varchar(100) not null,
    dataNascimento date not null,
    dtUltTrat date not null,
    idRacas integer,
    idEspecie integer
);

create table fornecedor(
    idfornecedor integer not null auto_increment primary key,
    razaoSocial varchar(50) not null
);

create table auditFinanceira(
    idAuditFinanceira integer not null auto_increment primary key,
    operacao varchar(10) not null,
    usuario varchar(4) not null,
    ifFinanceira integer,
    dataVenc date,
    valorPrev decimal(10, 2),
    dataPagto: date,
    valorPagto decimal(10, 2),
    tipo integer,
    numNF integer
);

create table movFinanceira(
    idFincanceiro integer not null auto_increment primary key,
    dataVenc date,
    valorPrev decimal(10, 2),
    dataPagto date,
    valorPagto decimal(10, 2), 
    tipo integer,
    numNf integer
);

create table nf(
    numNf integer not null auto_increment primary key,
    dataNf date, 
    tipo integer,
    atualizada integer, 
    idFornecedor integer,
    idProp integer
);


