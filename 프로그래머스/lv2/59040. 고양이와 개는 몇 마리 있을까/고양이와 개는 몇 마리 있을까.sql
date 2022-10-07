select animal_type, count(animal_id) as count
from animal_ins
where animal_type in ('cat','dog')
group by animal_type
order by animal_type