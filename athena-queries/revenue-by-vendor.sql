select vendorid,
	round(sum(total_amount), 2) as revenue,
	count(*) as trips
from nyc_taxi_db.cleaned_data
group by vendorid
order by revenue desc;
