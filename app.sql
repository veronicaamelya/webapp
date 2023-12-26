create table pemesanan (
	id serial,
	play_name text,
	customer_name text,
	gender text,
	game text,
	handphone text,
	waktu time,
	tanggal date
);

insert into pemesanan (play_name, customer_name, gender, game, handphone, waktu, tanggal) 
values
	('land', 'Veronica', 'female', '["bianglala"]', 62838, '08:00', '2023-10-01'),
	('land', 'Jeno', 'male', '["roller coaster", "bombom car"]', 62838, '09:00', '2022-10-02'),
	('air', 'Carissa', 'female', '["flying fox"]', 62838, '10:00', '2022-10-03'),
	('watery', 'Winter', 'female', '["swimming"]', 62838, '11:00', '2022-10-04'),
	('watery', 'Endita', 'male', '["jetski"]', 62838, '12:00', '2022-10-05'),
	('land', 'Putri', 'female', '["roller coaster", "bianglala", "ice skating", "bowling"]', 62838, '08:00', '2022-10-06'),
	('land', 'Marcella', 'male', '["bowling"]', 62838, '09:00', '2022-10-07'),
	('air', 'Mingyu', 'male', '["paralayang", "ice skating"]', 62838, '10:00', '2022-10-08'),
	('air', 'Anin', 'female', '["sky diving"]', 62838, '11:00', '2022-10-09'),
	('watery', 'Yugi', 'male', '["snorkling"]', 62838, '12:00', '2022-10-11')
;
