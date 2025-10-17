select date_trunc('day', pickup_datetime) as trip_day,
	count(*) as trips
from nyc_taxi_db.cleaned_data
group by 1
order by 2 desc;
