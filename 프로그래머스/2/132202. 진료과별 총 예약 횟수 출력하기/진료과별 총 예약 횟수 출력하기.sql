-- 2022년 5월에 예약한 환자수
-- 진료과 코드별 조회
-- 진료과 별, 예약한 환자 수 기준 오름 차순
-- 진료과 코드 기준 오름 차순
SELECT MCDP_CD 진료과코드, COUNT(MCDP_CD) 5월예약건수
FROM APPOINTMENT
WHERE DATE_FORMAT(APNT_YMD, "%Y-%m")="2022-05"
GROUP BY MCDP_CD
ORDER BY 5월예약건수, MCDP_CD;