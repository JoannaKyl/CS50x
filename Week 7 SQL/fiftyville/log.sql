-- Explore the table and schema of fiftyville.db
sqlite3 fiftyville.db
.table
.schema

-- Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery.
-- Interviews were conducted today with three witnesses who were present at the time – each of their interview transcripts mentions the bakery. |
select description from crime_scene_reports where year = 2023 and month = 7 and day = 28 and street = 'Humphrey Street';

-- Eugene:
-- I don't know the thief's name, but it was someone I recognized.
-- Earlier this morning, before I arrived at Emma's bakery, I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.                                                                                                 |

-- Raymond:
-- As the thief was leaving the bakery, they called someone who talked to them for less than a minute.
-- In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow.
-- The thief then asked the person on the other end of the phone to purchase the flight ticket. |

-- Ruth:
-- Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away.
-- If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame.
select name, transcript from interviews where year = 2023 and month = 7 and day = 28 order by name;

-- Based on Eugene, these are the suspects who withdrew money during the period
-- | account_number | amount |   id   |  name   |  phone_number  | passport_number | license_plate |
-- +----------------+--------+--------+---------+----------------+-----------------+---------------+
-- | 81061156       | 30     | 438727 | Benista | (338) 555-6650 | 9586786673      | 8X428L0       |
-- | 16153065       | 80     | 458378 | Brooke  | (122) 555-4581 | 4408372428      | QX4YZN3       |
-- | 49610011       | 50     | 686048 | Bruce   | (367) 555-5533 | 5773159633      | 94KL13X       |
-- | 26013199       | 35     | 514354 | Diana   | (770) 555-1861 | 3592750733      | 322W7JE       |
-- | 25506511       | 20     | 396669 | Iman    | (829) 555-5269 | 7049073643      | L93JTIZ       |
-- | 28296815       | 20     | 395717 | Kenny   | (826) 555-1652 | 9878712108      | 30G67EN       |
-- | 28500762       | 48     | 467400 | Luca    | (389) 555-5198 | 8496433585      | 4328GD8       |
-- | 76054385       | 60     | 449774 | Taylor  | (286) 555-6063 | 1988161715      | 1106N58       |
-- +----------------+--------+--------+---------+----------------+-----------------+---------------+
select bank_accounts.account_number, atm_transactions.amount, people.id, people.name, people.phone_number, people.passport_number, people.license_plate
from atm_transactions, bank_accounts, people
where year = 2023 and month = 7 and day = 28
and atm_location = 'Leggett Street'
and transaction_type = 'withdraw'
and bank_accounts.account_number = atm_transactions.account_number
and people.id = bank_accounts.person_id
order by people.name;

-- Based on Raymond, suspect is on phone within a min, further narrow down to 5 people
-- +-------------+----------------+----------------+----------+
-- | caller_name |     caller     |    receiver    | duration |
-- +-------------+----------------+----------------+----------+
-- | Benista     | (338) 555-6650 | (704) 555-2131 | 54       |
-- | Bruce       | (367) 555-5533 | (375) 555-8161 | 45       |
-- | Diana       | (770) 555-1861 | (725) 555-3243 | 49       |
-- | Kenny       | (826) 555-1652 | (066) 555-9701 | 55       |
-- | Taylor      | (286) 555-6063 | (676) 555-6554 | 43       |
-- +-------------+----------------+----------------+----------+
select people.name as caller_name, phone_calls.caller, phone_calls.receiver, phone_calls.duration
from people, phone_calls
where people.phone_number = phone_calls.caller
and people.name in ('Benista', 'Brooke', 'Bruce', 'Diana', 'Iman', 'Kenny', 'Luca', 'Taylor')
and phone_calls.year = 2023 and phone_calls.month = 7 and phone_calls.day = 28
and phone_calls.duration < 60
order by name;

-- Based on Ruth, the thief drove the car way between 10:15 and 10:25, so Bruce or Diana
-- +--------+------+--------+----------+
-- |  name  | hour | minute | activity |
-- +--------+------+--------+----------+
-- | Bruce  | 10   | 18     | exit     |
-- | Diana  | 10   | 23     | exit     |
-- | Taylor | 10   | 35     | exit     |
-- +--------+------+--------+----------+
select people.name, bakery_security_logs.hour, bakery_security_logs.minute, bakery_security_logs.activity
from people, bakery_security_logs
where bakery_security_logs.year = 2023 and bakery_security_logs.month = 7 and bakery_security_logs.day = 28 and bakery_security_logs.hour = 10
and people.name in ('Bruce', 'Taylor', 'Diana', 'Kenny', 'Taylor')
and bakery_security_logs.license_plate = people.license_plate
order by name;

-- Based on Raymond, the theif will leave on 29th earliest flight, so it is Bruce
--+-------+----+------------------------+------+------+------+
-- | name  | id | destination_airport_id | hour | hour | seat |
-- +-------+----+------------------------+------+------+------+
-- | Bruce | 36 | 4                      | 8    | 8    | 4A   |
-- | Diana | 18 | 6                      | 16   | 16   | 4C   |
-- +-------+----+------------------------+------+------+------+
select people.name, flights.id, flights.destination_airport_id, flights.hour, flights.hour, passengers.seat
from people, passengers, flights
where people.name in ('Bruce', 'Diana')
and flights.year = 2023 and flights.month = 7 and flights.day = 29
and passengers.flight_id = flights.id
and passengers.passport_number = people.passport_number
order by name;

-- Going to New York City
-- +----+--------------+-------------------+---------------+
-- | id | abbreviation |     full_name     |     city      |
-- +----+--------------+-------------------+---------------+
-- | 4  | LGA          | LaGuardia Airport | New York City |
-- +----+--------------+-------------------+---------------+
select * from airports where id = 4;

-- Who is the accomplice, let's look at who Bruce called
-- +-------+
-- | name  |
-- +-------+
-- | Robin |
-- +-------+
select people.name from people where phone_number = '(375) 555-8161';
