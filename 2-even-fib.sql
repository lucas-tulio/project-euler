select num, fib, sum(if(fib % 2 = 0, fib, 0)) sum_of_even_fibs from (
  select num, cast((power(((1 + sqrt(5)) / 2), num) - power(-1 / ((1 + sqrt(5)) / 2), num)) / sqrt(5) as unsigned) fib
    from (
      select num from (
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
      ) t1 where num >= 1 and num <= 92 -- fib(92) is the limit MySQL can store in a variable
    ) numbers
  ) fibs where fib < 4000000
;


