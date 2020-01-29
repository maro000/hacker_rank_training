SELECT
    name
FROM
    STUDENTS
WHERE
    marks > 75
;

-- RIGHT({name},3)
-- 右から３つまで取得

SELECT
    NAME
FROM
    EMPLOYEE
WHERE
    months < 10
    AND salary > 2000
;

select round(LONG_W,4)
from STATION
where LAT_N>38.7780
order by LAT_N
limit 1;

