#!/bin/env python
# Right--fill in the comments.

import sqlalchemy as sa

metadata = sa.MetaData()

ability_table = sa.Table('abilities', metadata,
                         sa.Column('id', sa.Integer, primary_key=True),
                         sa.Column('Name', sa.String), #ability name
                         sa.Column('in_game_desc', sa.String),
                         sa.Column('complete_description', sa.Text),
                         sa.Column('battle_entry_effect', sa.Text),
                         sa.Column('battle_exit_effect', sa.Text),
                         sa.Column('overworld_effect', sa.Text),
                         )

class Abilities(object):
    def __init__(self, Name, in_game, complete, battle_entry, battle_exit, overworld):
        self.Name = Name
        self.in_game_desc = in_game
        self.complete_description = complete
        self.battle_entry_effect = battle_entry
        self.battle_exit_effect = battle_exit
        self.overworld_effect = overworld

    def __repr(self):
        return "<Abilities('%s','%s','%s','%s','%s')>" % (self.Name, self.in_game_desc, 
                                                          self.complete_description, 
                                                          self.battle_entry_effect,
                                                          self.battle_exit_effect,
                                                          self.overworld_effect)
def add_engine(engine):
    metadata.create_all(engine)

sa.orm.mapper(Abilities, ability_table)

if __name__ eq '__main__':
    engine = sa.create_engine('sql:///:memory:',echo=True);
    add_engine(engine)
