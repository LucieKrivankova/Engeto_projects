/*Kolik je možné si koupit litrů mléka a kilogramů chleba za první a poslední srovnatelné období v dostupných datech cen a mezd?*/

select 
	year,
	price_name,
	price_avg,
	industry,
	payroll_avg,
	round(payroll_avg/price_avg) as compare
from t_lucie_krivankova_project_SQL_primary_final pf
where 1=1 
	and (price_name like 'Mléko%' or price_name like 'Chl%')
	and (year = 2006 or year = 2018)
order by industry, price_name, year 
;
