/*
    Nome: Gustavo Leão Nogueira de Oliveira
*/

/* Exercicio 1*/

create view remedio_do_animal as
    /* Seleciona o nome do animal, o nome do produto (como o remédio) e o preço do produto */
    select a.nome, r.nome as remedio, r.preco from tratamento 
        join consulta using(idconsulta)
        join animal a using(idanimal)
        join remediosprodutos r using(idremedioproduto);

/*Exercicio 2*/

create view veterinarios_de_cada_animal as
    /*  Seleciona o nome da pessoa (como veterinario), o nome do animal
        a hora e a data da consulta */
    select p.nome veterinario,a.nome,hora,datacons from consulta join pessoas p using(idpessoa) join animal a using(idanimal) 
    join veterinarios v using(idpessoa)
        where p.idpessoa=v.idpessoa;

/* Exercicio 3 */
create view lista_consulta_do_animal as
    /* seleciona o nome do dono, o nome do animal, a hora e a data da consulta
    */
    select p.nome dono,a.nome,hora,datacons from consulta 
        join pessoas p using(idpessoa) 
        join animal a using(idanimal);


/* Exercicio 4 */
create view lista_servico_animal as
    /* seleciona o nom do animal, da pessoa
    */
    select a.nome,p.nome as dono,s.descricao,datasolicitacao,hora,s.valor from solicita 
        join pessoas p using(idpessoa)
        join animal a using(idanimal) 
        join servicos s using(idservico);

/* Exercicio 5*/
create view data_dos_remedio as
    /* seleciona o nome e a data da consulta dos remédios do tratamento */
    select r.nome,c.datacons from tratamento 
        join remediosprodutos r using(idremedioproduto) 
        join consulta c using(idconsulta);

/* Exercicio 6 */
create view remedios_nao_prescritos as
    /* seleciona o nome do remédio e a data da consulta do tratamento */
    select r.nome,c.datacons from tratamento 
        right outer join remediosprodutos r using(idremedioproduto)  
        left outer join consulta c using(idconsulta)
            where datacons is null;

