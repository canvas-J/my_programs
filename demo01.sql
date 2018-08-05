-- 创建测试数据
create database db1;
use db1;
CREATE TABLE student (
    sid VARCHAR(10),
    sname NVARCHAR(10),
    sage DATETIME,
    ssex NVARCHAR(10)
);

insert into student values('01' , N'赵雷' , '1990-01-01' , N'男');
insert into student values('02' , N'钱电' , '1990-12-21' , N'男');
insert into student values('03' , N'孙风' , '1990-05-20' , N'男');
insert into student values('04' , N'李云' , '1990-08-06' , N'男');
insert into student values('05' , N'周梅' , '1991-12-01' , N'女');
insert into student values('06' , N'吴兰' , '1992-03-01' , N'女');
insert into student values('07' , N'郑竹' , '1989-07-01' , N'女');
insert into student values('08' , N'王菊' , '1990-01-20' , N'女');

CREATE TABLE course (
    cid VARCHAR(10),
    cname NVARCHAR(10),
    tid VARCHAR(10)
);

insert into course values('01' , N'语文' , '02');
insert into course values('02' , N'数学' , '01');
insert into course values('03' , N'英语' , '03');

CREATE TABLE teacher (
    tid VARCHAR(10),
    tname NVARCHAR(10)
);

insert into teacher values('01' , N'张三');

insert into teacher values('02' , N'李四');

insert into teacher values('03' , N'王五');

CREATE TABLE sc (
    sid VARCHAR(10),
    cid VARCHAR(10),
    score DECIMAL(18 , 1 )
);

insert into sc values('01' , '01' , 80);
insert into sc values('01' , '02' , 90);
insert into sc values('01' , '03' , 99);
insert into sc values('02' , '01' , 70);
insert into sc values('02' , '02' , 60);
insert into sc values('02' , '03' , 80);
insert into sc values('03' , '01' , 80);
insert into sc values('03' , '02' , 80);
insert into sc values('03' , '03' , 80);
insert into sc values('04' , '01' , 50);
insert into sc values('04' , '02' , 30);
insert into sc values('04' , '03' , 20);
insert into sc values('05' , '01' , 76);
insert into sc values('05' , '02' , 87);
insert into sc values('06' , '01' , 31);
insert into sc values('06' , '03' , 34);
insert into sc values('07' , '02' , 89);
insert into sc values('07' , '03' , 98);

show databases;
use db1;
select * from student;
select * from teacher;
select * from sc;
-- rename table student to student;
-- rename table sc to sc;
-- rename table teacher to teacher;

-- 1、查询"01"课程比"02"课程成绩高的学生的信息及课程分数
-- 思路：课程01（一个记录集合），课程02（一个记录集合），stuDENT表（一个记录集合），包含在这三个记录集合里，并且01分数>02分数的记录。
select * from student s 
inner join(select * from sc where cid='01') a on s.sid=a.sid 
inner join (select * from sc where cid='02') b on s.sid=b.sid 
where a.score>b.score;

select a.*, b.*, c.* from student a 
inner join sc b on a.sid=b.sid and b.cid='01' 
inner join sc c on a.sid=c.sid and c.cid='02' 
where b.score>c.score;

select a.*, b.score 课程01分数, c.score 课程02的分数 from student a, sc b, sc c
where a.sid=b.sid and a.sid= c.sid and b.cid ='01'and c.cid ='02'and b.score>c.score;

-- 1.1、查询同时存在"01"课程和"02"课程的情况
-- 思路：课程01（一个记录集合），课程02（一个记录集合），stuDENT表（一个记录集合），包含在这三个记录集合里的记录。
select * from student s 
inner join(select * from sc where cid='01') a on s.sid=a.sid 
inner join (select * from sc where cid='02') b on s.sid=b.sid 
where a.sid=b.sid;

select s.*, a.*, b.* from student s 
join sc a on s.sid=a.sid and a.cid='01' 
join sc b on s.sid=b.sid and b.cid='02';

-- left join(左联接) 返回包括左表中的所有记录和右表中联结字段相等的记录 
-- right join(右联接) 返回包括右表中的所有记录和左表中联结字段相等的记录
-- inner join(等值连接) 只返回两个表中联结字段相等的行


-- 1.2、查询同时存在"01"课程和"02"课程的情况和存在"01"课程但可能不存在"02"课程的情况(不存在时显示为null)(以下存在相同内容时不再解释)
-- 思路：课程01（一个记录集合），课程02可能有，可能不存在（cid=’02’ or cid is null）,stuDENT表（一个记录集合）
select * from student s 
join sc a on s.sid=a.sid and a.cid='01' 
left join sc b on s.sid=b.sid and (b.cid='02' or b.cid is null)
where a.score>ifnull(b.score,0);

-- isnull(列名，0)   isnull()函数是用来判断列名是否为null   如果为NUll 则返回0  否则 返回列名的值

select a.* ,b.score 课程01分数, c.score 课程02的分数 from student a 
join sc b on a.sid = b.sid and b.cid ='01'
left join sc c on a.sid = c.sid and (c.cid ='02' or c.cid is null);

-- 2、查询"01"课程比"02"课程成绩低的学生的信息及课程分数
select * from student s
join sc a on s.sid=a.sid and a.cid='01' 
join sc b on s.sid=b.sid and b.cid='02' 
where a.score<b.score;

-- 2.1、查询同时存在"01"课程和"02"课程的情况
select a.*, b.score 课程01分数, c.score 课程02的分数 
from student a , sc b , sc c
where a.sid = b.sid and a.sid = c.sid and b.cid ='01'and c.cid ='02'and b.score < c.score;

-- 2.2、查询同时存在"01"课程和"02"课程的情况和不存在"01"课程但存在"02"课程的情况
select * from student s
left join sc a on s.sid=a.sid and (a.cid='01' or a.cid is null)
join sc b on s.sid=b.sid and b.cid='02';

select * from student s 
left join(select * from sc where (cid='01' or cid is null)) b on s.sid=b.sid
join(select * from sc where cid='02') a on s.sid=a.sid ;

select a.*, b.score 课程01分数, c.score 课程02的分数 from student a
left join sc b on a.sid = b.sid and b.cid ='01'
join sc c on a.sid = c.sid and c.cid ='02';

-- 3、查询平均成绩大于等于60分的同学的学生编号和学生姓名和平均成绩
-- 思路：平均成绩大于等于60分（一个记录集合），stuDENT表（一个记录集合）
select s.sid, s.sname, b.平均成绩 from student s
inner join (select sid, convert(avg(score),decimal(18, 2)) as 平均成绩 
	from sc group by sid 
	having avg(score)>=60) b
on s.sid=b.sid;

select * from student s 
join(select sid,avg(score) as avgscore from sc 
	group by sid having avg(score)>=60) a
on s.sid=a.sid;

select a.sid, a.sname , cast(avg(b.score) as decimal(18,2)) avg_score
from student a, sc b where a.sid = b.sid
group by a.sid, a.sname
-- 此处选择显示三列，但结果只是最后一列，因此属性均需分组！
having cast(avg(b.score) as decimal(18,2)) >=60
order by a.sid;

-- 4、查询平均成绩小于60分的同学的学生编号和学生姓名和平均成绩
-- 思路：平均成绩小于60分（一个记录集合），stuDENT（一个记录集合）
select s.sid, s.sname, b.平均成绩 from student s 
inner join(select sid,convert(avg(score), decimal(18,2)) as 平均成绩 
	from sc group by sid having avg(score)>60) b
on s.sid=b.sid;

-- 4.1、查询在sc表存在成绩的学生信息的SQL语句。
-- 思路：stuDENT表（一个记录集合）是否有记录包含在sc表（一个记录集合）
select * from student where sid in(select sid from sc);  -- in相当于并列查询，子条件必须只返回一个结果，exists无限制
-- in后面表较小时比exists效率高！任何时候not exists（用了索引）均比not in（逐个遍历）快！
-- select * from student where exists(select sid from sc);  该句无意义！（无对应关系）
-- exists()判断表达式返回结果是否为真，是真就从主表取出数据。
select * from student s where exists(select 1 from sc a where s.sid=a.sid);

-- 4.2、查询在sc表中不存在成绩的学生信息的SQL语句。
select * from student where sid not in (select distinct sid from sc);

select * from student s where not exists (select 1 from sc a where s.sid=a.sid);

select a.sid, a.sname, ifnull(cast(avg(b.score) as decimal(18,2)),0) avg_score
from student a 
left join sc b on a.sid = b.sid
group by a.sid, a.sname
having ifnull(cast(avg(b.score) as decimal(18,2)),0) <60
order by a.sid;


select a.sid, a.sname , cast(avg(b.score) as decimal(18,2)) avg_score
from student a, sc b where a.sid = b.sid
group by a.sid, a.sname
-- 此处选择显示三列，但结果只是最后一列，因此属性均需分组！
having cast(avg(b.score) as decimal(18,2)) >=60
order by a.sid;
-- 5、查询所有同学的学生编号、学生姓名、选课总数、所有课程的总成绩
-- 思路：sc表的选课总数、总成绩（一个记录集合），stuDENT表（一个记录集合）
select s.sid, s.sname, a.选课总数, a.总成绩 from student s 
inner join(select sid, count(*) as 选课总数, sum(score) as 总成绩 
	from sc group by sid) a
on s.sid=a.sid;

select * from student s 
inner join(select sid, count(cid) as '课程总数',sum(score) as '课程总成绩' 
	from sc group by sid) a
on s.sid=a.sid;

select s.sid, s.sname, count(a.cid) as '课程总数', sum(a.score) as '课程总成绩' 
from student s 
inner join sc a on s.sid=a.sid 
group by s.sid,s.sname;

-- 5.1、查询所有有成绩的SQL。
select s.sid, s.sname, a.选课总数, a.总成绩 from student s 
inner join(select sid,count(*) as '选课总数', sum(score) as '总成绩' 
	from sc group by sid) a
on s.sid=a.sid;

select a.sid 学生编号, a.sname 学生姓名, count(b.cid) 选课总数, sum(score) 所有课程的总成绩
from student a, sc b
where a.sid = b.sid
group by a.sid, a.sname
order by a.sid;

-- 5.2、查询所有(包括有成绩和无成绩)的SQL。
select s.sid, s.sname, a.选课总数, a.总成绩 from student s 
left join(select sid,count(*) as '选课总数',sum(score) as '总成绩' 
	from sc group by sid) a
on s.sid=a.sid;

select * from student s 
left join(select sid,count(cid) as '课程总数',sum(score) as '课程总成绩' 
	from sc group by sid) a
on s.sid=a.sid order by s.sid;

select s.sid, s.sname, count(a.cid) as '课程总数',sum(a.score) as '课程总成绩' from student s 
left join sc a on s.sid=a.sid 
group by s.sid, s.sname 
order by s.sid;

select a.sid 学生编号, a.sname 学生姓名, count(b.cid) 选课总数, sum(score) 所有课程的总成绩 from student a 
left join sc b on a.sid = b.sid
group by a.sid, a.sname
order by a.sid;

-- 6、查询"李"姓老师的数量
select count(*) as '数量' from teacher where left(tname,1)='李';-- 获取指定长度字符
-- 方法1
select count(tname) 李姓老师的数量 from teacher where tname like '李%';

-- 方法2
select count(tname) 李姓老师的数量 from teacher where left(tname,1) = N'李';

-- 7、查询学过"张三"老师授课的同学的信息
-- 思路： stuDENT（一个记录集合），张三老师（一个记录集合），张三老师上的课（一个记录集合），张三老师上的课的成绩（一个记录集合）
select * from student s 
inner join sc a on s.sid=a.sid 
inner join course c on a.cid=c.cid 
inner join teacher t on c.tid=t.tid 
where t.tname='张三';

-- 思路：从全部学生中（一个记录集合）提取上过张三老师课的学生（一个记录集合）
select * from student where sid in(
	select sid from sc a 
    inner join course b on a.cid=b.cid 
    inner join teacher c on b.tid=c.tid and c.tname='张三');

select distinct student.* from student, sc, course, teacher
where student.sid = sc.sid and sc.cid = course.cid and course.tid = teacher.tid and teacher.tname = N'张三'
order by student.sid;

-- 8☆、查询没学过"张三"老师授课的同学的信息

-- 思路：从全部学生中（一个记录集合）删除上过张三老师课的学生（一个记录集合）。
select * from student 
where sid not in(select distinct sid from sc a 
	inner join course c on a.cid=c.cid
	inner join teacher t on c.tid=t.tid 
	where t.tname='张三');

select m.* from student m 
where sid not in(select distinct sc.sid from sc , course , teacher 
	where sc.cid = course.cid and course.tid = teacher.tid and teacher.tname =N'张三') 
order by m.sid;

-- 9、查询学过编号为"01"并且也学过编号为"02"的课程的同学的信息
-- 思路：上过课程01（一个记录集合），上过课程02（一个记录集合），stuDENT表（一个记录集合）
select * from student s 
inner join sc a on s.sid=a.sid and a.cid='01' 
inner join sc b on s.sid=b.sid and b.cid='02';

-- 思路：上过课程01的学生（一个记录集合）并且存在上过课程02的学生（一个记录集合）
select * from student s 
inner join sc a on s.sid=a.sid and a.cid='01' 
and exists (select 1 from sc b where s.sid=b.sid and b.cid='02');

-- 方法1
select student.* from student , sc 
where student.sid = sc.sid and sc.cid ='01' and exists(Select 1 from sc sc_2 
	where sc_2.sid = sc.sid and sc_2.cid ='02') 
order by student.sid;

-- 方法2
select student.* from student , sc 
where student.sid = sc.sid and sc.cid ='02'
and exists(select 1 from sc sc_2 
	where sc_2.sid = sc.sid and sc_2.cid ='01') 
order by student.sid;

-- 方法3
select m.* from student m where sid in
(select sid from
	(select distinct sid from sc where cid ='01'
    union all
	select distinct sid from sc where cid ='02'
	) t group by sid having count(1) =2
)
order by m.sid;

 

-- 10☆、查询学过编号为"01"但是没有学过编号为"02"的课程的同学的信息

-- 思路：上过课程01的学生（一个记录集合）并且不存在上过课程02的学生（一个记录集合）
select * from student s 
inner join sc a on s.sid=a.sid and a.cid='01' 
and not exists(select 1 from sc b where s.sid=b.sid and b.cid='02');

-- 思路：从全部学生中（一个记录集合）先提取上过课程01的学生记录（一个记录集合）再排除没上过课程02的学生记录（一个记录集合）
select * from student 
where sid in(select sid from sc where cid='01')
and sid not in (select sid from sc where cid='02');

select * from student s 
inner join sc a on s.sid=a.sid and a.cid='01' 
where s.sid not in (select sid from sc where cid='02');

-- 方法1
select student.* from student, sc 
where student.sid = sc.sid and sc.cid ='01'
and not exists(select * from sc sc_2 where sc_2.sid = sc.sid and sc_2.cid ='02') 
order by student.sid;

-- 方法2
select student.* from student, sc 
where student.sid = sc.sid and sc.cid ='01'and student.sid not in 
(Select sc_2.sid from sc sc_2 where sc_2.sid = sc.sid and sc_2.cid='02') 
order by student.sid;

-- 11、查询没有学全所有课程的同学的信息
-- 思路：从全部学生中（一个记录集合）提取在sc表中课程总数不是全部的学生（一个记录集合）

select * from student where sid in
(select sid from(select sid,count(*) as abc from sc group by sid 
having count(*)<(select count(cname) from course)) t);

-- 该方法只列出有课程分数的学生，一个课程分数也没有的学生不存在第二个记录集合中。

 

-- 思路：从全部学生中（一个记录集合）排除在sc表中有全部课程分数的学生（一个记录集合）
select * from student 
where sid not in(select sid from(select sid,count(*) as abc 
	from sc group by sid 
    having count(*)=(select count(cname) from course)) t);
-- 该方法还会列出一个课程分数都没有的学生。

-- 11.1、同上
select student.* from student, sc
where student.sid = sc.sid
group by student.sid, student.sname, student.sage, student.ssex 
having count(cid)< (select count(cid) from course);

-- 11.2
select student.* from student 
left join sc on student.sid = sc.sid
group by student.sid, student.sname, student.sage, student.ssex 
having count(cid)< (select count(cid) from course);

-- 12、查询至少有一门课与学号为"01"的同学所学相同的同学的信息

-- 思路：从全部学生中（一个记录集合）提取所学课程中至少有一门和学生01所学课程相同（一个记录集合）（也就是课程ID至少有一个存在于学生01的课程ID中）并排除学生01
select * from student where sid in
(select distinct sid from sc where cid in
(select cid from sc where sid='01') and sid<>'01');

select distinct student.* from student , sc 
where student.sid = sc.sid and sc.cid in 
(select cid from sc where sid ='01') and student.sid <>'01';

-- 13☆、查询和"01"号的同学学习的课程完全相同的其他同学的信息
-- 思路：从全部学生中（一个记录集合）提取所学全部课程ID存在于学生01的课程ID中并且课程总数等于学生01的课程总数（一个记录集合）
select * from student where sid in
(select distinct sid from sc where cid in
(select cid from sc where sid='01') and sid<>'01' group by sid
having count(*)=(select count(cid) from sc where sid='01'));

select student.* from student where sid in
(select distinct sc.sid from sc where sid <>'01'and sc.cid in (select distinct cid from sc where sid ='01')
group by sc.sid having count(1) = (select count(cid) from sc where sid='01'));

-- 14、查询没学过"张三"老师讲授的任一门课程的学生姓名
-- 思路：从全部学生中（一个记录集合）排除学过老师张三上过的课的学生（一个记录集合）（就是在sc表中有张三老师上过的课的分数）
select * from student where sid not in
(select distinct a.sid from sc a 
inner join course b on a.cid=b.cid 
inner join teacher c on b.tid=c.tid 
where c.tname='张三');

select student.* from student where student.sid not in
(select distinct sc.sid from sc, course, teacher 
where sc.cid = course.cid and course.tid = teacher.tid and teacher.tname = N'张三')
order by student.sid;

-- 15☆、查询两门及其以上不及格课程的同学的学号，姓名及其平均成绩
-- 思路：全部学生（一个记录集合），两门及以上不及格课程（一个记录集合）
select * from student s inner join
(select sid, count(*) as '不及格门数', convert(avg(score), decimal(18, 2)) as '平均分数' from sc 
where score<60 group by sid having count(cid)>=2) b
on s.sid=b.sid;

-- 太过麻烦
select s.sid, s.sname, count(a.cid) as '不及格门数', convert(avg(a.score), decimal(5, 2)) as average from student s 
inner join sc a on s.sid=a.sid group by s.sid, s.sname having s.sid in
(select sid from(select sid, count(cid) as times from sc 
where score<60 group by sid having count(cid)>=2) t);

select student.sid, student.sname, cast(avg(score) as decimal(18,2)) avg_score from student, sc
where student.sid = sc.sid and student.sid in 
(select sid from sc where score <60 group by sid having count(1)>=2)
group by student.sid, student.sname;
-- avg\max\min\sum等必须有group么？

-- 16、检索"01"课程分数小于60，按分数降序排列的学生信息
-- 思路：全部学生（一个记录集合），课程01分数小于60（一个记录集合）
select * from student s inner join sc a
on s.sid=a.sid where cid='01' and score<60 order by score desc;

select * from student s inner join(select * from sc where cid='01' and score<60) a
on s.sid=a.sid order by a.score;

select student.* , sc.cid , sc.score from student, sc
where student.sid = sc.sid and sc.score <60 and sc.cid ='01'
order by sc.score desc;

-- 17☆☆☆、按平均成绩从高到低显示所有学生的所有课程的成绩以及平均成绩
-- 思路：全部学生（一个记录集合），全部课程分数和平均分（一个记录集合），两个记录集合进行合并行转列（新的一个记录集合）
select s.sid, s.sname, max(case b.cname when N'语文' then a.score else null end) as '语文',
max(case b.cname when N'数学' then a.score else null end) as '数学',
max(case b.cname when N'英语' then a.score else null end) as '英语',
convert(avg(a.score), decimal(18, 2)) as '平均成绩'from student s 
left join sc a on s.sid=a.sid
left join course b on a.cid=b.cid group by s.sid, s.sname
order by 平均成绩 desc;

-- 17.1 SQL 2000 静态
select a.sid 学生编号, a.sname 学生姓名,
max(case c.cname when N'语文' then b.score else null end) 语文,
max(case c.cname when N'数学' then b.score else null end) 数学,
max(case c.cname when N'英语' then b.score else null end) 英语,
cast(avg(b.score) as decimal(18,2)) 平均分 from student a
left join sc b on a.sid = b.sid
left join course c on b.cid = c.cid
group by a.sid , a.sname
order by 平均分 desc;


-- 18☆☆☆☆☆、查询各科成绩最高分、最低分和平均分：以如下形式显示：
-- 课程ID，课程name，最高分，最低分，平均分，及格率，中等率，优良率，优秀率
-- 及格为>=60，中等为：70-80，优良为：80-90，优秀为：>=90
-- 思路：sc表和course表联合查询，每一个字段要求都可以看作是一个子查询，一个一个子查询单独做出来后，再拼接在一起。

select b.cid, b.cname, max(score) as '最高分', min(score) as '最低分', convert(avg(score), decimal(5,2)) as '平均分',
convert(convert(convert(count(case when a.score>=60 then 1 else null end), decimal(5,2))/count(1)*100, decimal(5,2)), char)+'%' as '及格率',
convert(convert(convert(count(case when a.score>=70 and a.score<80 then 1 else null end),decimal(5,2))/count(1)*100, decimal(5,2)),char)+'%' as '中等率',
convert(convert(convert(count(case when a.score>=80 and a.score<90 then 1 else null end),decimal(5,2))/count(1)*100, decimal(5,2)),char)+'%' as '优良率',
convert(convert(convert(count(case when a.score>=90 then 1 else null end),decimal(5,2))/count(1)*100, decimal(5,2)),char)+'%' as '优秀率'
from sc a inner join course b on a.cid=b.cid group by b.cid, b.cname;

 

-- 方法1

select m.cid 课程编号, m.cname 课程名称, max(n.score) 最高分, min(n.score) 最低分,
cast(avg(n.score) as decimal(18,2)) 平均分,
cast((select count(1) from sc where cid = m.cid and score >=60)*100.0/ (select count(1) from sc where cid = m.cid) as decimal(18,2)) '及格率(%)',
cast((select count(1) from sc where cid = m.cid and score >=70 and score <80 )*100.0/ (select count(1) from sc where cid = m.cid) as decimal(18,2)) '中等率(%)',
cast((select count(1) from sc where cid = m.cid and score >=80 and score <90 )*100.0/ (select count(1) from sc where cid = m.cid) as decimal(18,2)) '优良率(%)',
cast((select count(1) from sc where cid = m.cid and score >=90)*100.0/ (select count(1) from sc where cid = m.cid) as decimal(18,2)) '优秀率(%)'
from course m, sc n
where m.cid = n.cid
group by m.cid , m.cname
order by m.cid;

-- 方法2

select m.cid 课程编号, m.cname 课程名称,
(select max(score) from sc where cid = m.cid) 最高分,
(select min(score)from sc where cid = m.cid) 最低分,
(select cast(avg(score) as decimal(18,2)) from sc where cid = m.cid) 平均分,
cast((select count(1) from sc where cid = m.cid and score >=60)*100.0/ (select count(1) from sc where cid = m.cid) as decimal(18,2)) '及格率(%)',
cast((select count(1) from sc where cid = m.cid and score >=70 and score <80 )*100.0/ (select count(1) from sc where cid = m.cid) as decimal(18,2)) '中等率(%)',
cast((select count(1) from sc where cid = m.cid and score >=80 and score <90 )*100.0/ (select count(1) from sc where cid = m.cid) as decimal(18,2)) '优良率(%)',
cast((select count(1) from sc where cid = m.cid and score >=90)*100.0/ (select count(1) from sc where cid = m.cid) as decimal(18,2)) '优秀率(%)'
from course m
order by m.cid;

 

-- 19、按各科成绩进行排序，并显示排名
-- oracle：利用over(partition by 字段名order by 字段名)函数。
-- 正常排序：1，2，3
select row_number() over(partition by cid 
order by cid, score desc) as sort, * from sc;
-- 合并重复不保留空缺：1，1，2，3
select dense_rank() over(partition by cid 
order by cid,score desc) as sort,* from sc;
-- 合并重复保留空缺：1，1，3
select rank() over(partitionby cid 
order by cid,score desc) as sort,* from sc;

-- 19.1 sql 2000用子查询完成
-- score重复时保留名次空缺
select t.*, px = (select count(1) from sc 
where cid = t.cid and score > t.score)+1 from sc t 
order by t.cid, px;
-- score重复时合并名次
select t.* , px = (select count(distinct score) from sc 
where cid = t.cid and score >= t.score) from sc t order by t.cid , px;

 

-- 19.2 sql 2005用rank,DENSE_RANK完成
-- score重复时保留名次空缺(rank完成)
select t.*, px = rank() over(partition by cid 
	order by score desc)
from sc t 
order by t.cid , px;
-- score重复时合并名次(DENSE_RANK完成)
select t.*, px = DENSE_RANK() over(partition by cid 
order by score desc) from sc t order by t.cid , px;

 

-- 20、查询学生的总成绩并进行排名
-- 思路：所有学生的总成绩（一个记录集合），再使用函数进行排序。
select rank() over(order by sum(a.score) desc) as ranking,s.sid,s sname,sum(a.score) as '总成绩' from student s inner join sc a
on s.sid=a.sid groupby s.sid,s sname;
-- 这个查询只能查询到有成绩的7名学生。

 

select dense_rank() over(order by isnull(sum(a.score),0) desc) as ranking, s.sid, s.sname,
is null(sum(a.score),0) as '总成绩'
from student s left join sc a on s.sid=a.sid group by s.sid,s sname;
-- 用了leftjoin就可以查询到所有的8名学生了，包括没有成绩的1名学生。

 

-- 20.1 查询学生的总成绩
select m.sid 学生编号, m.sname 学生姓名, ifnull(sum(score), 0) 总成绩 from student m 
left join sc n on m.sid = n.sid
group by m.sid , m.sname
order by 总成绩 desc;

 

-- 20.2 查询学生的总成绩并进行排名，sql 2000用子查询完成，分总分重复时保留名次空缺和不保留名次空缺两种。
select t1.*, px = (select count(1) from
(
  select m.sid 学生编号,
         m.sname 学生姓名,
         ifnull(sum(score),0) 总成绩
  from student m left join sc n on m.sid = n.sid
  group by m.sid, m.sname
)t2 where 总成绩> t1.总成绩) + 1 from
(
  select m.sid 学生编号,
         m.sname 学生姓名,
         ifnull(sum(score),0) 总成绩
  from student m left join sc n on m.sid = n.sid
  group by m.sid, m.sname
)t1
order by px;

 

select t1.* , px = (select count(distinct总成绩) from
(
  select m.sid [学生编号] ,
         m.sname [学生姓名] ,
         is null(sum(score),0) [总成绩]
  from student m left join sc n on m.sid = n.sid
  group by m.sid, m.sname
)t2 where 总成绩>= t1.总成绩) from
(
  select m.sid [学生编号] ,
        m.sname [学生姓名] ,
        is null(sum(score),0) [总成绩]
  from student m left join sc n on m.sid = n.sid
  group by m.sid, m.sname
)t1
order by px;

 

-- 20.3 查询学生的总成绩并进行排名，sql 2005用rank,DENSE_RANK完成，分总分重复时保留名次空缺和不保留名次空缺两种。

select t.*, px = rank() over(order by[总成绩]desc) from
(
  select m.sid [学生编号] ,
         m.sname [学生姓名] ,
         is null(sum(score),0) [总成绩]
  from student m left join sc n on m.sid = n.sid
  group by m.sid, m.sname
)t
order by px;

 

select t.*, px = DENSE_RANK() over(order by[总成绩]desc) from
(
  select m.sid [学生编号] ,
         m.sname [学生姓名] ,
         is null(sum(score),0) [总成绩]
  from student m left join sc n on m.sid = n.sid
  group by m.sid, m.sname
)t
order by px;

 

-- 21、查询不同老师所教不同课程平均分从高到低显示
-- 思路：不同老师所教不同课程的平均分（一个记录集合），再使用函数over(order by 字段名)
select rank() over(order by convert(decimal(5,2),avg(score)) desc) as ranking,c.tid,c.tname,b.cid,b.cname,
convert(decimal(5,2),avg(score)) as '平均分' from sc a
inner join course b on a.cid=b.cid 
inner join teacher c on b.tid=c.tid 
group by c.tid,c.tname,b.cid,b.cname;
 

select m.tid, m.tname, cast(avg(o.score) as decimal(18,2)) avg_score
from teacher m, course n, sc o
where m.tid = n.tid and n.cid = o.cid
group by m.tid , m.tname
order by avg_score desc;