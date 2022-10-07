select b.CATEGORY,	b.price as MAX_PRICE,	b.PRODUCT_NAME
from 
    (select category, max(price) as max_price
    from food_product
    group by category
    having category in ('과자','국','김치','식용유')) a inner join food_product b
        on a.category=b.category and a.max_price = b.price
order by b.price desc