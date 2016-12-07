drop table if exists addressbook;
create table addressbook (
	id integer primary key autoincrement,
	login_user text not null,
	name text not null,
	phone_num integer not null
	);