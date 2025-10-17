select passenger_count,
	avg(total_amount) as avg_fare
from cleaned_data
group by passenger_count
order by passenger_count;
