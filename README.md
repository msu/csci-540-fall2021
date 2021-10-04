# CSCI 540: Advanced Database Systems

**NOTE: This is a live document and is subject to change throughout the
semester.**

Data is everywhere and often a database is a convenient way to store and process
it.  But is a relational database always the best way?  In this class we will
explore several advanced database models, computational paradigms
for processing large data sets, and searching (indexing) techniques.
Database models include spatial, key-value,
columnar, document, and graph; Computational paradigms for large data sets
include MapReduce and Streaming;  Searching techniques include approx-NN, LSH,
and inverted indices.

## Meeting Times

Mon, Wed, Fri 09:00-09:50, 1119 Wilson Hall

## Instructor

David L. Millman, Ph.D.

**Email**: david.millman@montana.edu

**Office hours**: TBD

**Office**: Barnard Hall 359

**Github**: [dlm](https://github.com/dlm)

**Bitbucket**: [david_millman](https://bitbucket.org/david_millman/)


## Learning Outcomes

After successfully completing this course, students will be able to:

* Identify and Explain why a database or collections of databases is appropriate
  for a task
* Build a system using polyglot persistence
* Design and implement algorithms for searching and processing massive data sets


## Textbook

No required text book but optional are highly recommended

Optional and highly recommended:

* [Database System
  Concepts](https://www.amazon.com/Database-System-Concepts-Abraham-Silberschatz-ebook/dp/B07PPHYQGV)
  by Abraham Silberschatz, Henry F. Korth and S. Sudarshan (DBSC below)
* [Seven Databases in Seven Weeks: A Guide to Modern Databases and the NoSQL
  Movement](https://www.amazon.com/Seven-Databases-Weeks-Modern-Movement/dp/1680502530)
  by Eric Redmond and Jim R. Wilson (7DB in reading below) (DO NOT USE 1st
  edition)
* [Probabilistic Data Structures and Algorithms for Big Data
  Applications](https://www.amazon.com/Probabilistic-Data-Structures-Algorithms-Applications/dp/3748190484)
  by Andrii Gakhov (PDS in reading below)
* [Lecture Notes from Modern Algorithmic
  Toolbox](http://timroughgarden.org/notes.html) by Tim Roughgarden and Greg
  Valiant (MAT below)
* [Mining of Massive Datasets](http://i.stanford.edu/~ullman/mmds/book0n.pdf) by
  Jure Leskovec, Anand Rajaraman, and Jeffrey D. Ullman (MMD below)
* SE-Radio:
    - [Advanced Postgres](https://www.se-radio.net/2019/04/se-radio-episode-362-simon-riggs-on-advanced-features-of-postgresql/)
    - [Query Planning](https://www.se-radio.net/2018/06/se-radio-episode-328-bruce-momjian-on-the-postgres-query-planner/)

Others will be added as relevant.

### Prerequisites

* **CSCI 440-- Database Systems**: DBMS architecture; major database models;
  relational algebra fundamentals; SQL query language; index file structures,
  data modeling and management, entity relationship diagrams.

* Comfort with a Unix based operating system.

* Willingness to get your hands dirty installing and working with multiple
  databases

## Class schedule

The lecture schedule is subject to change throughout the semester, but here is
the current plan. Assignments and due dates will be updated as they're assigned
in class.

### Aug

| Date  | Description                                   | Assigned                          | Due                                   | Recommended Reading   | Video                                                             |
|-------|-----------------------------------------------|-----------------------------------|---------------------------------------|-----------------------|-------------------------------------------------------------------|
| 08/25 | [Intro](./README.md)                          |                                   |                                       |                       | [1](https://montana.box.com/s/15qg7x5ciz7hmdc43ewcewkcjhihoqfz)   |
| 08/27 | [Intro/System Setup](./env/README.md)         |                                   |                                       |                       |                                                                   |
|       |                                               |                                   |                                       |                       |                                                                   |
| 08/30 | [Relational 1](./notes/2021-08-30.md)         |                                   |                                       | 7DB - Relational      | [1](https://montana.box.com/s/kdfjc3yegab7g790snvklo5ffjtpepn1)   |

### Sept

| Date  | Description                                   | Assigned                          | Due                                   | Recommended Reading   | Video                                                             |
|-------|-----------------------------------------------|-----------------------------------|---------------------------------------|-----------------------|-------------------------------------------------------------------|
| 09/01 | [Relational 2](./notes/2021-08-30.md)         |                                   |                                       | 7DB - Relational      |                                                                   |
| 09/03 | [Relational 3](./notes/2021-08-30.md)         |                                   |                                       | 7DB - Relational      |                                                                   |
|       |                                               |                                   |                                       |                       |                                                                   |
| 09/06 | NO CLASS (LABOR DAY)                          |                                   |                                       |                       |                                                                   |
| 09/08 | [Querying 1](./notes/2021-09-06.pdf)          |                                   |                                       | DBSC - Ch 12          |                                                                   |
| 09/10 | [Indexing](./notes/2021-09-10.pdf)            |                                   |                                       | DBSC - Ch 11          | [1](https://montana.box.com/s/p53pnlk7tl4xcsmcuc0ewsop36xs127d)   |
|       |                                               |                                   |                                       |                       |                                                                   |
| 09/13 | [Querying 2](./notes/2021-09-13.pdf)          |                                   |                                       | DBSC - Ch 12          |                                                                   |
| 09/15 | [Querying 3](./notes/2021-09-15.pdf)          |                                   |                                       | DBSC - Ch 12          |                                                                   |
| 09/17 | [Sorting](./notes/2021-09-17.pdf)             |                                   |                                       | DBSC - Ch 12          |                                                                   |
|       |                                               |                                   |                                       |                       |                                                                   |
| 09/20 | [Joins 1](./notes/2021-09-20.pdf)             |                                   |                                       | DBSC - Ch 12          |                                                                   |
| 09/22 | [Joins 2](./notes/2021-09-22.pdf)             |                                   |                                       | DBSC - Ch 12          |                                                                   |
| 09/24 | [Joins 3](./notes/2021-09-24.pdf)             |                                   |                                       | DBSC - Ch 12          |                                                                   |
|       |                                               |                                   |                                       |                       |                                                                   |
| 09/27 |  Column 1                                     | [hw01](./hw/01.md)                |                                       | 7DB - Column          |                                                                   |
| 09/29 |  **CLASS CANCELED**                           |                                   |                                       |                       |                                                                   |

### Oct

| Date  | Description                                   | Assigned                          | Due                                   | Recommended Reading   | Video                                                             |
|-------|-----------------------------------------------|-----------------------------------|---------------------------------------|-----------------------|-------------------------------------------------------------------|
| 10/01 |  CAP Theorem w/ Prof Wittie                   |                                   |                                       |                       |                                                                   |
|       |                                               |                                   |                                       |                       |                                                                   |
| 10/04 |  Column 2                                     |                                   |                                       | 7DB - Column          |                                                                   |
| 10/06 |                                               |                                   |                                       |                       |                                                                   |
| 10/08 |                                               |                                   |                                       |                       |                                                                   |
|       |                                               |                                   |                                       |                       |                                                                   |
| 10/11 |                                               |                                   | [hw01](./hw/01.md)                    |                       |                                                                   |
| 10/13 |                                               |                                   |                                       |                       |                                                                   |
| 10/15 |                                               |                                   |                                       |                       |                                                                   |
|       |                                               |                                   |                                       |                       |                                                                   |
| 10/18 |                                               |                                   |                                       |                       |                                                                   |
| 10/20 |                                               |                                   |                                       |                       |                                                                   |
| 10/22 |                                               |                                   |                                       |                       |                                                                   |
|       |                                               |                                   |                                       |                       |                                                                   |
| 10/25 |                                               |                                   |                                       |                       |                                                                   |
| 10/27 |                                               |                                   |                                       |                       |                                                                   |
| 10/29 |                                               |                                   |                                       |                       |                                                                   |


### Nov

| Date  | Description                                   | Assigned                          | Due                                   | Recommended Reading   | Video                                                             |
|-------|-----------------------------------------------|-----------------------------------|---------------------------------------|-----------------------|-------------------------------------------------------------------|
| 11/01 |                                               |                                   |                                       |                       |                                                                   |
| 11/03 |                                               |                                   |                                       |                       |                                                                   |
| 11/05 |                                               |                                   |                                       |                       |                                                                   |
|       |                                               |                                   |                                       |                       |                                                                   |
| 11/08 |                                               |                                   |                                       |                       |                                                                   |
| 11/10 |                                               |                                   |                                       |                       |                                                                   |
| 11/12 |                                               |                                   |                                       |                       |                                                                   |
|       |                                               |                                   |                                       |                       |                                                                   |
| 11/15 | Student Presentations                         |                                   |                                       |                       |                                                                   |
| 11/17 |                                               |                                   |                                       |                       |                                                                   |
| 11/19 |                                               |                                   |                                       |                       |                                                                   |
|       |                                               |                                   |                                       |                       |                                                                   |
| 11/22 | NO CLASS (THANKSGIVING)                       |                                   |                                       |                       |                                                                   |
| 11/24 | NO CLASS (THANKSGIVING)                       |                                   |                                       |                       |                                                                   |
| 11/26 | NO CLASS (THANKSGIVING)                       |                                   |                                       |                       |                                                                   |
|       |                                               |                                   |                                       |                       |                                                                   |
| 11/29 |                                               |                                   |                                       |                       |                                                                   |

### Dec

| Date  | Description                                   | Assigned                          | Due                                   | Recommended Reading   | Video                                                             |
|-------|-----------------------------------------------|-----------------------------------|---------------------------------------|-----------------------|===================================================================|
| 12/01 |                                               |                                   |                                       |                       |                                                                   |
| 12/03 |                                               |                                   |                                       |                       |                                                                   |
|       |                                               |                                   |                                       |                       |                                                                   |
| 11/06 | Final Presentations                           |                                   |                                       |                       |                                                                   |
| 11/08 | Final Presentations                           |                                   |                                       |                       |                                                                   |
| 10/10 | Final Presentations                           |                                   |                                       |                       |                                                                   |

### Potential Upcoming Topics:



* Relational
* Column store
* Document store
* Graph store
* Data structure store
* Processing Large Datasets / Approximating
* Journalling/Write ahead logging
* Compression

## Evaluation

Your grade for this class will be determined by:

* 10% Quizzes (lowest quiz is dropped)
* 35% Homework (lowest homework is dropped)
* 25% Exam
* 10% [Group Presentation](./hw/present.md)
* 20% [Group Project](./hw/proj.md)

## Policies

### Attendance

Attendance in class with not be taken but students are responsible for all
material covered in class.  If you are not in class, you cannot receive credit
for quizzes. Attendance is strongly recommended.

### Assignments

There will be regular homework assignments (about every week or every other week
depending on the difficulty of the assignment) consisting
of written problems and coding exercises.  Homeworks will be
posted in the schedule.  If not specified, solutions should be submitted as a
PDF on Brightspace.
(The tool that I use for grading documents only works with PDFs, so any file
format other than PDF will receive a 0.)
Homework is due at 23:59 on the due date. Late homework will not be accepted.

You do NOT need to write up your solutions with LaTex, but I highly encourage
you to do so.  You can find some resources for getting started with latex (and
for making figures, and keeping all those files safe with git) in the [student
resources repo](https://github.com/compTAG/student-resources).

I encourage collaboration, see collaboration section for details.

### Discussion

Group discussions, questions, and announcements will take place on the
Brightspace message board.
is okay to send me a direct message or email if you have a question that you feel
is not appropriate to share with the class.  If, however, you send me an message
with a question for which the response would be useful to the rest of the class,
I will likely ask you to post publicly.

### Collaboration

Collaboration IS encouraged, however, all submitted individual work must be your
own and you must acknowledge your collaborators at the beginning of the
submission.

On any group project, every team member is expected to make a substantial
contribution. The distribution of the work, however, is up to the team.

A few specifics for the assignments.  You may:

* Work with anyone in the course.
* Share ideas with others in the course
* Help other teams debug their code or proofs.

You may NOT:

* Submit a proof or code that you did not write.
* Modify another's proof or code and claim it as your own.

Using resources in addition to the course materials is encouraged. But, be sure
to properly cite additional resources. Remember, it is NEVER acceptable to pass
others work off as your own.

Paraphrasing or quoting another's work without citing the source is a form of
academic misconduct. Even inadvertent or unintentional misuse or appropriation
of another's work (such as relying heavily on source material that is not
acknowledged) is considered plagiarism. If you have any questions about using
and citing sources, you are expected to ask for clarification. My rule of thumb
is if I am in doubt, I cite.

By participating in this class, you agree to abide by the [student code of
conduct](http://www.montana.edu/policy/student_conduct/).  Please review the
policy.

### Classroom Etiquette

Except for note taking and coding, please keep electronic devices off during
class, they can be distractions to other students. Disruptions to the class will
result in you being asked to leave the lecture and will negatively impact your
grade.

### Special needs information

If you have a documented disability for which you are or may be requesting an
accommodation(s), you are encouraged to contact me and Disabled Student Services
as soon as possible.

If you are a student with a disability and wish to use your approved
accommodations for this course, please contact me during my office hours to
discuss. Please have your Accommodation Notification or Blue Card available for
verification of accommodations.  Accommodations are approved through the Office
of Disability Services located in SUB 174. Please see [Disability Services for
more information](http://www.montana.edu/disabilityservices).

### COVID Stuff

Montana State University strongly recommends students, faculty and staff wear
face masks in indoor public spaces, in accordance with the Centers for Disease
Control recommendations. Montana State University encourages students, faculty
and staff to take advantage of convenient, on-campus clinics for the COVID-19
vaccine. Schedule your appointment by going to:

[www.montana.edu/health/coronavirus](www.montana.edu/health/coronavirus)

This information is from Provost Mokwa’s communication on 8/13/2021.

[COVID-19 Frequently Asked Questions](https://www.montana.edu/health/coronavirus/faq.html)

In the event of contagious illness, please do not come to class or to campus to
turn in work. You should email me if you will miss class due to illness as soon
as practical.

### You Are Not Alone

Students at Montana State University have the right to live and learn in an
academic environment that is free from all forms of discrimination including
sexual and gender-based discrimination, harassment, and violence including
sexual assault, relationship violence, and stalking.  If you (or someone you
know) has experienced or is experiencing these types of behaviors, please know
that you are not alone.  Resources and support are available at MSU.  You can
learn more at: [www.montana.edu/voice](www.montana.edu/voice).  MSU has
confidential resources available to you through the VOICE Center, MSU Counseling
and Psychological Services, and University Health Partners Health Services.
These services are available to provide support, resources, and referrals to
numerous campus and community agencies that can provide the information and
support you need.

Please know that if you choose to confide in me, I am required by the university
to report to the Title IX Coordinator/MSU Office of Institutional Equity, as MSU
and I want to ensure you are connected with all the support the university can
offer.  You are not required to respond to outreach from the university if you
do not want to do so.  You can also make a report yourself, including an
anonymous report, through switness@montana.edu

### Mental Health and Wellness

MSU strives to create a culture of support and recognizes that your mental
health and wellness are equally as important as your physical health. We want
you to know that it’s OK if you experience difficulty, and there are several
resources on campus to help you succeed emotionally, personally, and
academically:

- Counseling & Psychological Services: https://www.montana.edu/counseling/
- Health Advancement: http://www.montana.edu/oha/
- Insight Program (Substance Use): http://www.montana.edu/oha/insight/
- Suicide Prevention: https://www.montana.edu/suicide-prevention/
- Medical Services: https://www.montana.edu/health/medical.html
- WellTrack wellness app: https://montana.welltrack.com
- Mental Health Screening: https://screening.mentalhealthscreening.org/montanastateuniv
- Let’s Talk drop-in services: https://www.montana.edu/counseling/letstalk.html

