create or replace function soma(integer, integer)
    returns integer as 'select $1 + $2;'
    language sql immutable
    returns null on null input;

create or replace function subtracao(integer, integer)
    returns integer as 'select $1 - $2;'
    language sql immutable
    returns null on null input;


create or replace function multiplicacao(integer, integer)
    returns integer as 'select $1 * $2;'
    language sql immutable
    returns null on null input;
    
create or replace function divisao(numeric, numeric)
    returns text as 'select to_char($1 / $2, ''999.99'');'
    language sql immutable
    returns null on null input;
	
	


select soma(5, 5);
select soma(5, 9);

select subtracao(5, 5);
select subtracao(5, 9);

select multiplicacao(5, 5);
select multiplicacao(5, 9);

select divisao(75, 7);
select divisao(5, 9);