select extract(hour from pickup_datetime) as pickup_hour,
    count(*) as trip_count
from nyc_taxi_db.cleaned_data
group by 1
order by 2 desc
limit 5;
