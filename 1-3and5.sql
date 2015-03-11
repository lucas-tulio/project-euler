select sum(multiple_3_5) from (
  select num, if(num % 3 = 0 or num % 5 = 0, num, 0) multiple_3_5 from (
    -- Numbers
    select
      (t1.num * 1) + (t2.num * 2) + (t3.num * 4) + (t4.num * 8) + (t5.num * 16) + (t6.num * 32) + (t7.num * 64) + (t8.num * 128) + (t9.num * 256) + (t10.num * 512) as num
    from (
      ((select 0 num) union all (select 1 num)) t1
      cross join
      ((select 0 num) union all (select 1 num)) t2
      cross join
      ((select 0 num) union all (select 1 num)) t3
      cross join
      ((select 0 num) union all (select 1 num)) t4
      cross join
      ((select 0 num) union all (select 1 num)) t5
      cross join
      ((select 0 num) union all (select 1 num)) t6
      cross join
      ((select 0 num) union all (select 1 num)) t7
      cross join
      ((select 0 num) union all (select 1 num)) t8
      cross join
      ((select 0 num) union all (select 1 num)) t9
      cross join
      ((select 0 num) union all (select 1 num)) t10
    )
  ) numbers
  where num >= 1 and num <= 1000
) multiples;
