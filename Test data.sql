select * from charges

-- Initial Charges
insert into charges (description) values('Presidente'), ('Vice Presidente'), ('Social media'), ('Tail Gunner')



-- Test members
select * from members

insert into members (charges_id, fullname, blood_type, email, password, address, phone_number, image, birthdate, is_active, register_date)
values(4, 'Daniel Fierro Najera', 'A+', 'danil.fierro796@gmail.com', 'password', 'address', '6645599035', 'N/A', '1993-07-04', false, CURRENT_DATE)

SELECT members.id, charges_id, charges.description, fullname from members
INNER JOIN charges ON (members.charges_id = charges.id)
