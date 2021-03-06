-- delete the tables if they already exist
drop table if exists countries cascade;
drop table if exists cities cascade;
drop table if exists venues cascade;
drop table if exists events cascade;


-- crate the schema for our table
create table countries (
    country_code char(2) primary key,
    country_name text unique
);

-- populate some data
insert into countries (country_code, country_name) values
    ('us', 'United States'),
    ('mx', 'Mexico'),
    ('au', 'Australia'),
    ('gb', 'United Kingdom'),
    ('de', 'Germany'),
    ('ll', 'Loompland');


-- validate that the constraint is observed
insert into countries values ('uk', 'United Kingdom');

-- display all entries in table
select * from countries;

-- delete Loompland, it is not real
delete from countries where country_code = 'll';

-- create cities w/ foreign key constraint to county
create table cities (
    name text not null,
    postal_code varchar(9) check (postal_code <> ''),
    country_code char(2) references countries,
    primary key (country_code, postal_code)
);

-- try to crate a city that does not conform to the foreign key constraint
insert into cities values ('Toronto', 'M4C1B5', 'ca');

-- try a valid insert
insert into cities values ('Portland', '87200', 'us');

-- the postal code was wrong, update it
-- NOTE that I did the lookup by postal code and not name (as the book does)
-- since there is no constraint that the name is unique, if there were other
-- Portlands in the DB, all of their zips would change
update cities set postal_code = '97206'
where postal_code = '87200' and name = 'Portland';

-- perform a join
select cities.*, country_name
from cities inner join countries
    on cities.country_code = countries.country_code;

-- create a venue table
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

-- lets do a join
select v.venue_id, v.name, c.name
from venues v inner join cities c
    on v.postal_code = c.postal_code and v.country_code = c.country_code;

-- add a famous doghnut shop to demonstate returning values
insert into venues (name, postal_code, country_code) values
    ('Voodoo Doughnut', '97206', 'us') returning venue_id;

-- demonstrate outer joins,
-- create evens table and add a few events
create table events (
    event_id serial primary key,
    title text,
    starts timestamp,
    ends timestamp,
    venue_id integer references venues(venue_id)
);
insert into events (title, starts, ends, venue_id) values
    ('LARP Club', '2012-02-15 17:30', '2012-02-15 19:30', 2),
    ('April Fools Day', '2012-04-01', '2012-04-01 23:59', null),
    ('Christmas Day', '2012-12-25', '2012-12-25 23:59', null);

select e.title, v.name
from events e left join venues v
    on e.venue_id = v.venue_id;

-- And if we are going to be searching on event titles and times, lets create an
-- ordered index
create index events_title
    on events using btree (title);
create index events_starts
    on events using btree (starts);
