-- Drop tables prior to setup
drop table if exists countries cascade;
drop table if exists cities cascade;
drop table if exists venues cascade;

create table countries (
    country_code char(2) primary key,
    country_name text unique
);


insert into countries (country_code, country_name) values
    ('us', 'United States'),
    ('mx', 'Mexico'),
    ('au', 'Australia'),
    ('gb', 'United Kingdom'),
    ('de', 'Germany'),
    ('ll', 'Loompland');


select * from countries;

delete from countries where country_code = 'll';

select * from countries;

create table cities (
    name text not null,
    postal_code varchar(9) check (postal_code <> ''),
    country_code char(2) references countries,
    primary key (country_code, postal_code)
);

insert into cities values ('Toronto', 'M4C1B5', 'ca');

insert into cities values ('Portland', '87200', 'us');

select * from cities;

update cities set postal_code = '97206'
where postal_code = '87200' and name = 'Portland';

select * from cities;

select cities.*, country_name
from cities inner join countries
on cities.country_code = countries.country_code;

create table venues (
    venue_id serial primary key,
    name varchar(255),
    street_address text,
    type char(7)
        check ( type in ('public', 'private') ) default 'public',
    postal_code varchar(9),
    country_code char(2),
    foreign key (country_code, postal_code)
        references cities (country_code, postal_code) match full
);

insert into venues (name, postal_code, country_code) values
    ('Crystal Ballroom', '97206', 'us');

select * from venues;

select v.venue_id, v.name, c.name
from venues v inner join cities c
on v.postal_code = c.postal_code and v.country_code = c.country_code;

insert into venues (name, postal_code, country_code) values
    ('Voodoo Doughnut', '97206', 'us') returning venue_id;
