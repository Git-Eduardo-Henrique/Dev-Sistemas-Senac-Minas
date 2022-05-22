use sakila;

SET SQL_SAFE_UPDATES = 0;

#1
select country from country;

#2
select count(country) as NumPaises from country;

#3
select country from country where country like '%A';

#4
select distinct release_year from film;

#5
update film set release_year = '2007' where title like 'B%';
select title, release_year from film where title like 'B%';

#6
select length, title, rating from film where length > 100 and rating = 'G';
#7
update film set release_year = '2008' where rental_duration < 4 and rating = 'pg';
select release_year, title, rental_duration, rating from film where rating = 'pg' and rental_duration < 4; 
#8
select count(*) as quantidade from film where rating = 'pg-13' and rental_rate > '2.40';
#9
select distinct language.name from film, language where film.language_id = language.language_id;
#10
update film set language_id = '6' where rental_rate > 4;
select title, rental_rate, language_id from film where language_id = '6'; # incompleto

#11
update film set language_id = '3' where rental_rate = 0.99;
select title, rental_rate from film where language_id = '3';

#12
select count(*) as quantiFilmes from film group by rating;

#13
select distinct rental_rate from film;

#14
select count(*) as quantiFilmes from film group by rental_rate;

#15
select  count(title) as quantiFilmes, rental_rate from film group by rental_rate having count(title) > 340;

#16

#17

#18

#19
select max(rental_DURATION) from film;

#20
select count(title) as quant_films from film where rental_duration = (select max(rental_DURATION) from film);

#21
select count(title) as FILMES from film where (language_id = '3' or language_id = '6') and rental_duration = 7; # imcompleto

#22
select rating, rental_rate, count(*) as QuantFilmes from film group by rating, rental_rate order by rating;

#23
select category.name, max(rental_duration) as TempoMaximo 
from film, category, film_category where film.film_id = film_category.film_id 
and film_category.category_id = category.category_id group by category.name ;

#24
select category.name, count(*) as QUANT 
from film, category, film_category where film.film_id = film_category.film_id
and film_category.category_id = category.category_id group by category.name;

#25
select rating, count(*) as QUANT from film where rating = 'G';

#26
select rating, count(*) as QUANT from film group by rating having rating = 'G' or rating = 'PG';

#27
select rating, count(*) as QUANT from film group by rating;

#28

#29
select release_year, count(*) as QUANT from film group by release_year order by QUANT;

#30
select release_year, count(*) as QUANT from film group by release_year having QUANT > 400 order by QUANT;

#31A


#32A
select city.city, country.country from city, film, country  
where country.country like 'E%' and country.country_id = city.country_id group by country.country; #  imcompleto

select * from city where country_id = '28';
select * from city;
select * from country;

#31B

select count(*) from city 
#32B

#33

#34

#35


