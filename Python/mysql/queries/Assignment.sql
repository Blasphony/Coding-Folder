SELECT name, languages.language, languages.percentage FROM countries
JOIN languages ON countries.id = languages.country_id
WHERE languages.language = 'Slovene';

SELECT countries.name, count(*) FROM countries
JOIN cities ON countries.id = cities.country_id
GROUP BY countries.name;

SELECT cities.name, cities.population FROM cities
WHERE cities.country_code = 'MEX' AND cities.population > 500000
GROUP BY cities.name;

SELECT countries.name,languages.percentage FROM countries
JOIN languages ON countries.id = languages.country_id
WHERE languages.percentage > 89;

SELECT countries.name, countries.surface_area FROM countries
WHERE countries.surface_area < 501 AND countries.population > 100000;

SELECT countries.name, countries.government_form, countries.life_expectancy, countries.capital FROM countries
WHERE countries.government_form ='Constitutional Monarchy' AND countries.life_expectancy > 75 AND countries.capital > 200;

SELECT countries.name AS 'Country', cities.name AS 'City_Name', cities.district, cities.population FROM countries
JOIN cities ON countries.id = cities.country_id
WHERE countries.name='Argentina' AND cities.district = 'Buenos Aires' AND cities.population > 500000;

SELECT countries.region, count(*) AS Countries FROM countries
GROUP BY countries.region
ORDER BY Countries DESC;
