SELECT A.AUTHOR_ID, A.AUTHOR_NAME,
    B.CATEGORY, sum(BS.SALES * B.PRICE) AS TOTAL_SALES
FROM BOOK B, AUTHOR A, BOOK_SALES BS
WHERE B.AUTHOR_ID=A.AUTHOR_ID
AND B.BOOK_ID=BS.BOOK_ID
AND DATE_FORMAT(BS.SALES_DATE, "%Y-%m")="2022-01"
GROUP BY B.AUTHOR_ID, B.CATEGORY
ORDER BY A.AUTHOR_ID, B.CATEGORY DESC;