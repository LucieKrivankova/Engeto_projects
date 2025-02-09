-- create table t_lucie_krivankova_project_SQL_secondary_final as (
select 
	e.year,
	e.country,
	e.gdp,
	e.gini,
	e.population
from countries c
left join economies e
	on c.country = e.country
where 1=1
	and c.continent = 'Europe'
	and e.year between 2006 and 2018
--)
;
