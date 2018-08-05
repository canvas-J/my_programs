use db1;
show tables;


select * from T001 limit 20;
















-- 22☆、查询所有课程的成绩第2名到第3名的学生信息及该课程成绩

-- 思路：所有课程成绩的学生及课程信息（一个记录集合），再利用函数排序（一个记录集合），选择第2名和第3名的记录。

with abc as
(select row_number() over(partition by a.cid order by a.score desc)as ranking,s.sid,s.sname,a.cid,b.cname,
a.score from student s inner join sc a on s.sid=a.sid inner join course b on a.cid=b.cid)
select * from abc where ranking in (2,3);
 

select * from
(select row_number() over(partition by a.cid order by a.score desc)as ranking,s.sid,s.sname,a.cid,b.cname,
a.score from student s inner join sc a on s.sid=a.sid inner join course b on a.cid=b.cid) t
where t.ranking in(2,3);

 

-- 22.1 sql 2000用子查询完成
-- score重复时保留名次空缺
select * from (select t.* , px = (select count(1) from sc 
where cid = t.cid and score > t.score) + 1 from sc t) m 
where px between 2 and 3 order by m.cid , m.px;
-- score重复时合并名次
select * from (select t.* , px = (select count(distinct score) from sc 
where cid = t.cid and score >= t.score) from sc t) m 
where px between 2 and 3 order by m.cid , m.px;
 

-- 22.2 sql 2005用rank,DENSE_RANK完成
-- score重复时保留名次空缺(rank完成)
select * from (select t.*, px = rank() over(partition by cid order by score desc) 
from sc t) m 
where px between 2 and 3
order by m.cid, m.px;
-- score重复时合并名次(DENSE_RANK完成)
select * from (select t.* , px = DENSE_RANK() over(partition by cid order by score desc) 
from sc t) m where px between 2 and 3 
order by m.cid , m.px;
 

-- 23☆☆☆、统计各科成绩各分数段人数：课程编号,课程名称,'100-85','85-70','70-60','0-60'及所占百分比
-- 思路：sc表和course表联合查询（一个记录集合），然后每个字段都看做是一个子查询，最后将这些子查询拼接起来。
select b.cid as '课程编号',b.cname as '课程名称',
count(1) as'总人数',
count(case when a.score<60 then 1 else null end) as '不及格人数',
convert(decimal(5,2),count(case when a.score>=0 and a.score<60 then 1 else null end)*100/count(1)) as '不及格率%',
count(case when a.score>=60 and a.score<70 then 1 else null end) as '及格人数',
convert(decimal(5,2),count(case when a.score>=60 and a.score<70 then 1 else null end)*100/count(1)) as '及格率%',
count(case when a.score>=70 and a.score<85 then 1 else null end) as '优良人数',
convert(decimal(5,2),count(case when a.score>=70 and a.score<85 then 1 else null end)*100/count(1)) as '优良率%',
count(case when a.score>=85 then 1 else null end) as '优秀人数',
convert(decimal(5,2),count(case when a.score>=85 then 1 else null end)*100/count(1)) as '优秀率%'
from sc a inner join course b on a.cid=b.cid 
group by b.cid,b.cname;
-- 以上方法为横向显示。


select b.cid as '课程编号',b.cname as '课程名称',(case when score<60 then '0-59'
when score>=60 and score<70 then '60-69'
when score>=70 and score<85 then '70-85'
else '85-100' end) as '分数段',
count(1) as'人数',
convert(decimal(18,2),count(1)*100/(select count(1) from sc where cid=b.cid)) as '百分比'
from sc a inner join course b on a.cid=b.cid group by all b.cid,b.cname,(case when score<60 then '0-59'
when score>=60 and score<70 then '60-69'
when score>=70 and score<85 then '70-85'
else '85-100' end)
order by b.cid,b.cname,'分数段';
-- 以上方法为纵向显示，但为0的就不显示了。


-- 23.1 统计各科成绩各分数段人数：课程编号,课程名称,'100-85','85-70','70-60','0-60'
-- 横向显示
select course.cid 课程编号, course.cname as课程名称,
  sum(case when score >=85 then 1 else 0 end) '85-100',
  sum(case when score >=70 and score <85 then 1 else 0 end) '70-85',
  sum(case when score >=60 and score <70 then 1 else 0 end) '60-70',
  sum(case when score <60 then 1 else 0 end) '0-60'
from sc , course
where sc.cid = course.cid
group by course.cid , course.cname
order by course.cid;
-- 纵向显示1(显示存在的分数段)
select m.cid 课程编号, m.cname 课程名称, 分数段= (
  case when n.score >=85 then '85-100'
       when n.score >=70 and n.score <85 then'70-85'
       when n.score >=60 and n.score <70 then'60-70'
       else'0-60'
  end) ,
  count(1) 数量
from course m , sc n
where m.cid = n.cid
group by m.cid , m.cname , (
  case when n.score >=85 then '85-100'
       when n.score >=70 and n.score <85 then '70-85'
       when n.score >=60 and n.score <70 then '60-70'
       else '0-60'
  end)
order by m.cid , m.cname , 分数段;

-- 纵向显示2(显示存在的分数段，不存在的分数段用0显示)
select m.cid 课程编号, m.cname 课程名称, 分数段= (
  case when n.score >=85 then '85-100'
       when n.score >=70 and n.score <85 then '70-85'
       when n.score >=60 and n.score <70 then '60-70'
       else'0-60'
  end) ,
  count(1) 数量
from course m , sc n
where m.cid = n.cid
group by m.cid , m.cname , (
  case when n.score >=85 then '85-100'
       when n.score >=70 and n.score <85 then '70-85'
       when n.score >=60 and n.score <70 then '60-70'
       else '0-60'
  end)
order by m.cid , m.cname , 分数段;


-- 23.2 统计各科成绩各分数段人数：课程编号,课程名称,'100-85','85-70','70-60','<60'及所占百分比
-- 横向显示
select m.cid 课程编号, m.cname 课程名称,
 (select count(1) from sc where cid = m.cid and score <60) '0-60',
  cast((select count(1) from sc where cid = m.cid and score <60)*100.0/ (select count(1) from sc where cid = m.cid) as decimal(18,2)) '百分比(%)',
  (select count(1) from sc where cid = m.cid and score >=60 and score <70) '60-70',
  cast((select count(1) from sc where cid = m.cid and score >=60 and score <70)*100.0/ (select count(1) from sc where cid = m.cid) as decimal(18,2)) '百分比(%)',
  (select count(1) from sc where cid = m.cid and score >=70 and score <85) '70-85',
  cast((select count(1) from sc where cid = m.cid and score >=70 and score <85)*100.0/ (select count(1) from sc where cid = m.cid) as decimal(18,2)) '百分比(%)',
 (select count(1) from sc where cid = m.cid and score >=85) '85-100',
  cast((select count(1) from sc where cid = m.cid and score >=85)*100.0/ (select count(1) from sc where cid = m.cid) as decimal(18,2)) '百分比(%)'
from course m
order by m.cid;

-- 纵向显示1(显示存在的分数段)
select m.cid '课程编号' , m.cname '课程名称' , 分数段= (
  case when n.score >=85 then '85-100'
       when n.score >=70 and n.score <85 then '70-85'
       when n.score >=60 and n.score <70 then '60-70'
       else '0-60'
  end) ,
  count(1) 数量 , 
  cast(count(1) *100.0/ (select count(1) from sc where cid = m.cid) as decimal(18,2)) '百分比(%)'
from course m , sc n
where m.cid = n.cid
group by m.cid , m.cname , (
  case when n.score >=85 then '85-100'
       when n.score >=70 and n.score <85 then '70-85'
       when n.score >=60 and n.score <70 then '60-70'
       else '0-60'
  end)
order by m.cid , m.cname , 分数段;

-- 纵向显示2(显示存在的分数段，不存在的分数段用0显示)
select m.cid '课程编号' , m.cname '课程名称' , 分数段= (
  case when n.score >=85 then '85-100'
       when n.score >=70 and n.score <85 then '70-85'
       when n.score >=60 and n.score <70 then '60-70'
       else '0-60'
  end) ,
  count(1) 数量 , 
  cast(count(1) *100.0/ (select count(1) from sc where cid = m.cid) as decimal(18,2)) '百分比(%)'
from course m , sc n
where m.cid = n.cid
group by all m.cid , m.cname , (
  case when n.score >=85 then '85-100'
       when n.score >=70 and n.score <85 then '70-85'
       when n.score >=60 and n.score <70 then '60-70'
       else '0-60'
  end)
order by m.cid , m.cname , 分数段;
 

-- 24、查询学生平均成绩及其名次
-- 思路：所有学生的平均成绩（一个记录集合），再使用函数进行排序。
select s.sid,s sname,row_number() over(order by avg(score) desc) as ranking,convert(decimal(18,2),
avg(score)) as '平均成绩' from student s inner join sc a on s.sid=a.sid group by s.sid,s sname;
-- 只显示有成绩的学生。



select s.sid,s sname,row_number() over(order by avg(score) desc) as ranking,convert(decimal(18,2),
avg(score)) as '平均成绩' from student s left join sc a on s.sid=a.sid group by s.sid,s sname;
-- 显示所有学生。

 

-- 24.1 查询学生的平均成绩并进行排名，sql 2000用子查询完成，分平均成绩重复时保留名次空缺和不保留名次空缺两种。
select t1.* , px = (select count(1) from
(
  select m.sid '学生编号' ,
         m.sname '学生姓名' ,
         is null(cast(avg(score) as decimal(18,2)),0) '平均成绩'
  from student m left join sc n on m.sid = n.sid
  group by m.sid, m sname
)t2 where 平均成绩> t1.平均成绩) +1 from
(
  select m.sid '学生编号' ,
         m.sname '学生姓名' ,
         is null(cast(avg(score) as decimal(18,2)),0) '平均成绩'
  from student m left join sc n on m.sid = n.sid
  group by m.sid, m.sname
)t1
order by px;


select t1.* , px = (select count(distinct平均成绩) from
(
  select m.sid '学生编号' ,
         m.sname '学生姓名' ,
         is null(cast(avg(score) as decimal(18,2)),0) '平均成绩'
  from student m left join sc n on m.sid = n.sid
  group by m.sid, m.sname
)t2 where 平均成绩>= t1.平均成绩) from
(

  select m.sid '学生编号' ,
         m.sname '学生姓名' ,
         is null(cast(avg(score) as decimal(18,2)),0) '平均成绩'
  from student m left join sc n on m.sid = n.sid
  group by m.sid, m.sname
)t1
order by px;

 

-- 24.2 查询学生的平均成绩并进行排名，sql 2005用rank,DENSE_RANK完成，分平均成绩重复时保留名次空缺和不保留名次空缺两种。
select t.*, px = rank() over(order by'平均成绩'desc) from
(
  select m.sid '学生编号' ,
         m.sname '学生姓名' ,
         is null(cast(avg(score) as decimal(18,2)),0) '平均成绩'
  from student m left join sc n on m.sid = n.sid
  group by m.sid, m sname
)t
order by px;

 

select t.* , px = DENSE_RANK() over(order by'平均成绩'desc) from
(
  select m.sid '学生编号' ,
         m.sname '学生姓名' ,
         is null(cast(avg(score) as decimal(18,2)),0) '平均成绩'
  from student m left join sc n on m.sid = n.sid
  group by m.sid, m.sname
)t
order by px;

 

-- 25、查询各科成绩前三名的记录

-- 思路：各学科成绩排序（一个记录集合），再取前3。

select * from
(select row_number() over(partition by a.cid order by a.score desc)as ranking,
s.sid, s.sname, a.score from student s 
inner join sc a on s.sid=a.sid) t 
where ranking in (1,2,3);
 

-- 25.1 分数重复时保留名次空缺
select m.* , n.cid , n.score from student m, sc n where m.sid = n.sid and n.score in
(select top3 score from sc where cid = n.cid order by score desc)
order by n.cid , n.score desc;

 

-- 25.2 分数重复时不保留名次空缺，合并名次
-- sql 2000用子查询实现
select * from (select t.* , px = (select count(distinct score) from sc 
where cid = t.cid and score >= t.score) from sc t) m 
where px between 1 and 3 order by m.cid , m.px;

-- sql 2005用DENSE_RANK实现
select * from 
(select t.* , px = DENSE_RANK() 
  over(partition by cid 
    order by score desc) from sc t
) m 
where px between 1 and 3
order by m.cid , m.px;

 

-- 26、查询每门课程被选修的学生数
-- 思路：每门课被选修的学生数（一个记录集合）。
select * from course a inner join
(select cid,count(*) as '人数' from sc group by cid) b
on a.cid=b.cid;

 

select a.cid,a.cname,count(1) as '人数' from course a inner join sc b
on a.cid=b.cid group by a.cid,a.cname;

 

select cid, count(sid) '学生数' from sc group by cid;
 

-- 27、查询出只有两门课程的全部学生的学号和姓名
select student.sid ,student sname
from student , sc
where student.sid = sc.sid
group by student.sid , student.sname
having count(sc.cid) =2
order by student.sid;

 

-- 28、查询男生、女生人数
-- 思路：

select ssex,count(1)as '人数' from student group by ssex;

 
 
select count(ssex) as 男生人数 from student where ssex = N'男';

select count(ssex) as 女生人数 from student where ssex = N'女';

select sum(
case when ssex = N'男'then 1 else 0 end
) '男生人数',
sum(
case when ssex = N'女'then 1 else 0 end
) '女生人数'from student;

select case when ssex = N'男'then N'男生人数'else N'女生人数'end '男女情况' , 
count(1) '人数' from student 
group by case when ssex = N'男'then N'男生人数'else N'女生人数'end;

 

-- 29、查询名字中含有"风"字的学生信息
select * from student where sname like'%风%';
 
select * from student where sname like N'%风%';

select * from student where charindex(N'风' , sname) >0;

 

-- 30、查询同名同性学生名单，并统计同名人数
-- 思路：按照姓名字段进行GROUP BY，同时计算人数，只要大于1，就是同姓同名。
select sname,count(1) as '人数' from student group by sname having count(1)>1;

select sname '学生姓名', count(*) '人数'from student group by sname having count(*) >1;
 

-- 31、查询1990年出生的学生名单(注：student表中sage列的类型是datetime)
select * from student where datepart(year,sage)='1990';

select * from student where year(sage) =1990;

select * from student where dateiff(yy,sage,'1990-01-01') =0;

select * from student where datepart(yy,sage) =1990;

select * from student where convert(varchar(4), sage, 120) ='1990';

 

-- 32、查询每门课程的平均成绩，结果按平均成绩降序排列，平均成绩相同时，按课程编号升序排列

-- 思路：每门课程的平均成绩（一个记录集合），再使用函数排序，排序时根据平均成绩、课程编号。

select row_number() over(order by convert(decimal(18,2),avg(a.score)) desc,b.cid) 
as '排名',b.cid,b.cname,convert(decimal(18,2),avg(a.score)) as '平均成绩' from sc ainner join course b
on a.cid=b.cid group by b.cid, b.cname;

 

select m.cid , m.cname , cast(avg(n.score) as decimal(18,2)) avg_score
from course m, sc n
where m.cid = n.cid   
group by m.cid, m.cname
order by avg_score desc, m.cid asc;

 

-- 33、查询平均成绩大于等于85的所有学生的学号、姓名和平均成绩
select s.sid, s.sname, convert(decimal(18,2), avg(a.score)) as '平均成绩' 
from student s inner join sc a
on s.sid=a.sid group by s.sid, s.sname 
having avg(a.score)>=85;

 

select a.sid , a sname , cast(avg(b.score) as decimal(18,2)) avg_score
from student a , sc b
where a.sid = b.sid
group by a.sid , a.sname
having cast(avg(b.score) as decimal(18,2)) >=85
order by a.sid;

 

-- 34、查询课程名称为"数学"，且分数低于60的学生姓名和分数
select s.sid, s sname, b.cname, a.score from student s inner join sc a
on s.sid=a.sid inner join course b
on a.cid=b.cid
where b.cname='数学' and a.score<60;

 

select sname , score
from student , sc , course
where sc.sid = student.sid 
and sc.cid = course.cid 
and course.cname = N'数学'
and score <60;

 

-- 35、查询所有学生的课程及分数情况；
select s.sid,s sname,b.cid,b.cname,a.score
from student s inner join sc a on s.sid=a.sid inner join course b on a.cid=b.cid;

 

select student.* , course.cname , sc.cid ,sc.score 
from student, sc , course
where student.sid = sc.sid and sc.cid = course.cid
order by student.sid , sc.cid;

 

-- 36、查询任何一门课程成绩在70分以上的姓名、课程名称和分数；
select s.sid,s sname,b.cid,b.cname,a.score from student s inner join sc a
on s.sid=a.sid inner join course b
on a.cid=b.cid
where a.score>70;

 

select student.* , course.cname , sc.cid ,sc.score 
from student, sc , course
where student.sid = sc.sid and sc.cid = course.cid and sc.score >=70
order by student.sid , sc.cid;

 

-- 37、查询不及格的课程
select s.sid,s.sname,b.cid,b.cname,a.score from student s inner join sc a
on s.sid=a.sid inner join course b
on a.cid=b.cid
where a.score<60;

 

select student.* , course.cname , sc.cid ,sc.score 
from student, sc , course
where student.sid = sc.sid and sc.cid = course.cid and sc.score <60
order by student.sid , sc.cid;

 

-- 38、查询课程编号为01且课程成绩在80分以上的学生的学号和姓名；
select s.sid,s sname,b.cid,b.cname,a.score from student s inner join sc a
on s.sid=a.sid inner join course b
on a.cid=b.cid
where a.score>=80 and b.cid='01';

 

select student.* , course.cname , sc.cid ,sc.score 
from student, sc , course
where student.sid = sc.sid and sc.cid = course.cid and sc.cid ='01'and sc.score >=80
order by student.sid , sc.cid;

 

-- 39、求每门课程的学生人数
select b.cid,b.cname,count(1) as '人数' from sc a inner join course b
on a.cid=b.cid 
group by b.cid,b.cname;

 

select course.cid , course.cname, count(*) 学生人数
from course , sc
where course.cid = sc.cid
group by course.cid , course.cname
order by course.cid , course.cname;

 

-- 40、查询选修"张三"老师所授课程的学生中，成绩最高的学生信息及其成绩
-- 思路：上张三老师课的学生（一个记录集合）
select top1 from student s inner join sc a
on s.sid=a.sid inner join course b
on a.cid=b.cid inner join teacher c
on b.tid=c.tid where c.tname='张三' order by a.score desc;

 

-- 40.1 当最高分只有一个时
select top1, student.*, course.cname , sc.cid ,sc.score 
from student, sc , course ,teacher
where student.sid = sc.sid and sc.cid = course.cid and course.tid = teacher.tid and teacher.tname = N'张三'
order by sc.score desc;

 

-- 40.2 当最高分出现多个时
select student.* , course.cname , sc.cid ,sc.score 
from student, sc , course ,teacher
where student.sid = sc.sid and sc.cid = course.cid and course.tid = teacher.tid and teacher.tname = N'张三'and
sc.score= (select max(sc.score) 
    from sc , course , teacher 
    where sc.cid = course.cid and course.tid = teacher.tid and teacher.tname = N'张三'
    );
 

-- 41☆☆☆☆☆、查询不同课程成绩相同的学生的学生编号、课程编号、学生成绩
-- 思路：

-- 方法1

select m.* from sc m,(select cid , score from sc group by cid , score having count(1) >1) n
where m.cid= n.cid and m.score = n.score order by m.cid , m.score , m.sid;

-- 方法2
select m.* from sc m where exists(select 1 from (select cid , score from sc group by cid , score having count(1) >1) n
where m.cid= n.cid and m.score = n.score) order by m.cid , m.score , m.sid;

-- 42、查询每门课程成绩最好的前两名
-- 思路：每门课程全部成绩（一个记录集合）。
select * from (select row_number() over (partition by cid order by score desc) as ranking,* from sc) a where ranking in (1,2);


select t.* from sc t where score in (select top2 score from sc where cid = T.cid order by score desc) order by t.cid , t.score desc;

-- 43、统计每门课程的学生选修人数（超过5人的课程才统计）。要求输出课程号和选修人数，查询结果按人数降序排列，若人数相同，按课程号升序排列 
select b.cid, b.cname, count(1) as '人数' from sc a inner join course b
on a.cid=b.cid 
group by b.cid,b.cname having count(1)>5 
order by count(1) desc,b.cid;

 

select course.cid, course.cname, count(*) 学生人数
from course , sc
where course.cid = sc.cid
group by course.cid , course.cname
having count(*) >=5
order by 学生人数 desc , course.cid;

 

-- 44、检索至少选修两门课程的学生学号
select s.sid,s sname,count(1) as '课程数' from student s inner join sc a
on s.sid=a.sid group by s.sid,s.sname having count(1)>=2;

 
select student.sid ,student.sname
from student, sc
where student.sid = sc.sid
group by student.sid , student.sname
having count(1) >=2
order by student.sid;

 

-- 45、查询选修了全部课程的学生信息
select s.sid, s.sname, count(1) as '课程数' from student s inner join sc a
on s.sid=a.sid group by s.sid,s.sname having count(1)>=(select count(1) from course);

-- 方法1 根据数量来完成
select student.*from student where sid in
(select sid from sc group by sid having count(1) = (select count(1) from course));
-- 方法2 使用双重否定来完成
select t.*from student t where t.sid not in
(
  select distinct m.sid from
  (
    select sid , cid from student , course
  ) m where not exists (select 1 from sc n where n.sid = m.sid and n.cid = m.cid)
);

-- 方法3 使用双重否定来完成
select t. * from student t where not exists(select 1 from
(
  select distinct m.sid from
  (
    select sid , cid from student , course
  ) m where not exists (select 1 from sc n where n.sid = m.sid and n.cid = m.cid)
) k where k.sid = t.sid
);


-- 46、查询各学生的年龄
select *,datediff(year,sage,getdate()) as '年龄' from student;
-- 粗略算法
select *,datediff(day,sage,getdate())/365 as '年龄' from student;

-- 具体算法

 

-- 46.1 只按照年份来算
select *, datediff(yy, sage, getdate()) 年龄 from student;

 

-- 46.2 按照出生日期来算，当前月日 < 出生年月的月日则，年龄减一
select *, case when right(convert(varchar(10),getdate(), 120),5) <right(convert(varchar(10),sage,120),5) 
then datediff(yy , sage , getdate()) -1 else datediff(yy , sage ,getdate()) end '年龄' from student;

-- 47、查询本周过生日的学生
-- 思路：将学生出生日期的年换成今年，然后加上具体日期，再和今天比较，如果为0，就是本周，如果为-1，就是下周，如果为1，就是上周。
select * from student
where datediff(week,convert(varchar, datepart(yy, getdate()))+right(convert(varchar(10),sage,120),6),getdate())=0;

select * from student where datediff(week,datename(yy,getdate()) +right(convert(varchar(10),sage,120),6),getdate()) =0;


-- 48、查询下周过生日的学生
select * from student
where datediff(week,convert(datepart(yy,getdate()),varchar)+right(convert(sage,varchar(10),120),6),getdate())=-1;

select * from student where datediff(week,datename(yy,getdate()) +right(convert(varchar(10),sage,120),6),getdate()) =-1;

-- 49、查询本月过生日的学生
-- 思路：把学生的出生日期的年换成今年，然后判断月是否在当前月。为0就是本月，为1就是上月，为-1就是下月。
select * from student
where datediff(mm,convert(varchar,datepart(yy,getdate()))+right(convert(varchar(10),sage,120),6),getdate())=0;

select*from student where datediff(mm,datename(yy,getdate()) +right(convert(varchar(10),sage,120),6),getdate()) =0;

-- 50、查询下月过生日的学生
select * from student
where datediff(mm,convert(varchar,datepart(yy,getdate()))+right(convert(varchar(10),sage,120),6),getdate())=-1;


select * from student where date diff(mm,datename(yy,getdate()) +right(convert(varchar(10),sage,120),6),getdate()) =-1;