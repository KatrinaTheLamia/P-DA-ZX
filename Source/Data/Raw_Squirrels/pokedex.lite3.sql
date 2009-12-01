
create table stats (
    id integer primary key
    Pokemon_id integer,
    Name varchar(31),
    current_level integer,
    evs integer,
    iv integer,
    experience integer,
);

create table battle_type (
    Name varchar(15),
    Gen integer,
    Weak_to varchar(15),
    Resist_to varchar(15),
    Weak_from varchar(15),
    Resist_from varchar(15),
    Immune_to varchar(15),
    Immune_from varchar(15),
);

create table contest_type (
    Name varchar(7),
    does_not_like varchar(7),
);

create table abilities (
    id integer primary key,
    Name varchar(23),
    Description text,
    Battle_Effect text,
    Overworld_Effect text,
);

create table battle_move (
    Name varchar(15),
    Gen integer,
    Description text,
    Category integer,
    Priority integer,
    Battle_type varchar(15),
    Basic_attack integer,
    Accuracy integer,
    Max_pp integer,
    Attack_Script text,
);

create table contest_move (
    Name varchar(15).
    Gen integer,
    Description text,
    Contest_Type varchar(7),
    Appeal integer,
    Appeal_Script text,
);

create table technical_machine (
    id integer,
    Name varchar(15),
    Gen integer,
);

create table hidden_machine (
    id integer,
    Name varchar(15),
    Gen integer,
);

create table terrain (
    Name varchar(15),
    Description varchar(100),
    Weather_Effect varchar(15),
    Map data,
);

create table weather_effect (
    Name varchar(15),
    Gen integer,
    Description text,
    Type_Bonus varchar(15),
    Type_Lower varchar(15),
    Effect_Script text,
);

create table pokemon_base (
    Pokemon varchar(31),
    Gen integer,
    Battle_Type_1 varchar(15),
    Battle_Type_2 varchar(15),
    Ability integer,
    Experience_at_100 integer,
    Catch_Rate integer,
    Base_Happiness integer,
    Gender_Ratio float,
    Egg_Ground_1 varchar(15),
    Egg_Ground_2 varchar(15),
    Egg_Cycle integer,
);

create table snag_base (
    Pokemon varchar(31),
    Game varchar(2),
    Spotted varchar(31),
    Trainer varchar(31),
);

create table pokedex_base (
    Pokemon varchar(31),
    Id integer,
    Game varchar(31),
    Species varchar(31),
    Pokemon_Colour varchar(15),
    Height float,
    Weight float,
    Body_Size integer,
    IQ_Group varchar(2),
    Cry data,
    Foot_Print data,
    Body_Style data,
    Habitat data,
    Entry text,
);

create table Pokemon_Moves_Levelup (
    Pokemon varchar(31),
    Gen integer,
    Learn_level integer,
    Move varchar(15),
);

create table Pokemon_Moves_Egg (
    Pokemon varchar(31),
    Gen integer,
    Move varchar(15),
);

create table Pokemon_Moves_Technical (
    Pokemon varchar(31),
    Gen integer,
    TM_Id integer,
);

create table Pokemon_Moves_Hidden (
    Pokemon varchar(31),
    Gen integer,
    HM_Id integer,
);

create table Pokemon_Moves_Tutor (
    Pokemon varchar(31),
    Game varchar(2),
    Move varchar(2),
    Tutor varchar(31),
);

create table ev_yield (
    Pokemon varchar(31),
    Gen integer,
    Stat_Name varchar(31)
    Yield integer,
);

create table evolve (
    Gen integer,
    Pokemon_Now varchar(31),
    Pokemon_To varchar(31).
    Script text,
);

create table items (
    Name varchar(31),
    Gen integer,
    Game varchar(2),
    Description varchar(100),
    Effect text,
    Hold_Effect text,
);

create table item_location (
    Item varchar(31),
    Game varchar(2),
    Location varchar(100),
);

create table hold_item (
    Item varchar(31),
    Pokemon varchar(31),
    Chance float,
);

create table berry (
    Name varchar(31),
    Gen integer,
    id integer,
    Description varchar(100),
    Effect text,
);

create table pokemon_base_stat (
    Pokemon varchar(31),
    Gen integer,
    Stat_Name varchar(31),
    Ammount integer,
);

create table pokemon_flavour (
    Pokemon varchar(31),
    Gen integer,
    Battle_Palette data,
    Overworld_Palette data,
    Front data,
    Back data,
    Overworld data,
);

create table pokemon_model (
    Pokemon varchar(31),
    Game varchar(2),
    Skin data,
    Palette data,
    Mesh data,
    Skeleton data,
);

create table pokemon_text (
    Pokemon varchar(31),
    Game varchar(2),
    Text varchar(100),
    Event text,
);

create table pokemon_location (
    Pokemon varchar(31),
    Game varchar(2),
    Location varchar(31),
    Wild_Level integer,
    Chance float,
    Start_time integer,
    End_time integer,
    Date_of_week integer,
    Month integer,
    Day integer,
);

create table location (
    Name varchar(31).
    Game varchar(2),
    Region varchar(15),
    Description varchar(100),
    Map data,
);

create table location_links (
    Here varchar(31),
    There varchar(31),
);

create table regions (
    Name varchar(15),
    Game varchar(2),
    Map data,
    Description text,
);

create table Location_to_Region (
    Region varchar(15),
    Location varchar(31),
    Game varchar(2),
);

