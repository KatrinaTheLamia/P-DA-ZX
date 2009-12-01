
create table trainer (
    name varchar(31),
    title varchar(31),
    id integer,
);

create table trainer_images (
    trainer_id integer,
    game varchar(2);
    battle_palette data,
    overworld_palette data,
    front_sprite data,
    back_sprite data,
    overworld_sprite data,
);

create table trainer_model (
    trainer_id integer,
    skin data,
    palette data,
    mesh data,
    skeleton data,
);

create table trainer_text (
    trainer_id integer,
    notes varchar(100),
    preparation text,
    text_trigger varchar(15),
    text_entry varchar(63),
);

create table inventory_current (
    trainer_id integer,
    item varchar(31),
    ammount integer,
);

create table berries_current (
    trainer_id integer,
    berry varchar(31),
    ammount integer,
);

create table tm_current (
    trainer_id integer,
    tm integer,
    ammount integer,
);

create table hm_current (
    trainer_id integer,
    hm integer,
);

create table pokemon (
    trainer_id integer,
    pokemon_id integer,
    game char(2),
    pokemon varchar(31),
    nick varchar(31),
    item varchar(31),
    gender char,
    poke_virus char,
    shiny boolean,
    ball char(2),
    Exp_Points integer,
    nature char(7),
    timestamp date,
    location varchar(31),
    met_level integer,
    food_type varchar(5),
    ability varchar(23),
    happiness integer,
    sheen integer,
);

create table pokemon_stat (
    pokemon_id integer,
    stat_id integer,
);

create table pokemon_contest (
    pokemon_id integer,
    contest_type varchar(7),
    ammount integer,
);

create table moves (
    pokemon_id integer,
    move varchar(15),
    curr_pp integer,
);

create table ribbons (
    pokemon_id integer,
    ribbon varchar(15),
);
