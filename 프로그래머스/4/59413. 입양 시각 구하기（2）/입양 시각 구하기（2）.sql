SET @HOUR = -1;

SELECT @HOUR := @HOUR+1 as hour, 
    (SELECT COUNT(animal_id) 
     FROM animal_outs
     WHERE @HOUR = HOUR(datetime)) as count
FROM animal_outs
WHERE @HOUR < 23
