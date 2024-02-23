-- 5월 1일 기준 조회
-- 출고 여부 5월 1일까지 출고완료, 이후 출고미정
-- 주문 ID 기준 오름차순
SELECT ORDER_ID, PRODUCT_ID, DATE_FORMAT(OUT_DATE, "%Y-%m-%d") OUT_DATE, 
    (CASE
        WHEN DATE_FORMAT(OUT_DATE, "%m-%d") <= "05-01" THEN "출고완료"
        WHEN DATE_FORMAT(OUT_DATE, "%m-%d") > "05-01" THEN "출고대기"
        ELSE "출고미정"
     END) 출고여부
FROM FOOD_ORDER
ORDER BY ORDER_ID;