#!/bin/env python
# Right--fill in the comments... eventually

import sqlalchemy as sa

metadata = sa.MetaData()

battle_move_table = sa.Table('battle_moves', metadata,
                             sa.Column('name',sa.String), # move name
                             sa.Column('generation',sa.String), # generation id
                             sa.Column('description',sa.Text), # move description
                             sa.Column('category',sa.Integer), # status, physical or special
                             sa.Column('target',sa.Integer), # the move's target type
                             sa.Column('prioriy', sa.Integer), # move priorty
                             sa.Column('battle_type',sa.String), # what battle typing applies?
                             sa.Column('basic_attack',sa.Integer), # the moves' basic attack value
                             sa.Column('accuracy',sa.Integer), # moves accuracy percentage
                             sa.Column('max_pp',sa.Integer), # moves maximum power points
                             sa.Column('attack_script',sa.Text), # what the attack does in battle
                             sa.Column('overworld_script',sa.Text), # the move's overworld effect
                             );

contest_move_table = sa.Table('contest_moves', metadata
                              sa.Column('name',sa.String), # move name
                              sa.Column('generation',sa.String), # contest generation
                              sa.Column('description',sa.Text), # contest description
                              sa.Column('contest_type',sa.String), # context type name
                              sa.Column('appeal',sa.Integer), # appeal ammount
                              sa.Column('jamming',sa.Integer), # jamming ammount
                              sa.Column('appeal_script',sa.Text), # appeal script
                              sa.column('jamming_script',sa.Text), # jamming script
                              );

class Battle_Move(object):
    def __init__(self, name, generation, description, category, target, priority, 
                 battle_type, basic_attack, accuracy, max_pp, attack_script, 
                 overworld_script):
        self.name = name
        self.generation = generation
        self.description = description
        self.category = category
        self.target = target
        self.priority = priority
        self.battle_type
        self.basic_attack = basic attack
        self.accuracy = accuracy
        self.max_pp = max_pp
        self.attack_script = attack_script
        self.overworld_script = overworld_script

    def __repr(self):
        return "<Battle_Move('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')>" % \
            (self.name, self.generation, self.category, self.target, self.priority, self.battle_type, \
             self.basic_attack, self.accuracy, self.max_pp, self.attack_script, self.over_world_script)

class Contest_Move(object):
    def __init__(self, name, generation, description, contest_type, appeal, jamming, appeal_script, jamming_script):
        self.name = name
        self.generation = generation
        self.description = description
        self.contest_type = contest_type
        self.appeal = appeal
        self.jamming = jamming
        self.appeal_script = appeal_script
        self.jamming_script = jamming_script

    def __repr(self):
        return "<Contest_Move('%s','%s','%s','%s','%s','%s','%s','%s')>" % \
            (self.name, self.generation, self.description, self.contest_type, self.appeal, self.jamming,
             self.appeal_script, self.jamming_script)

def add_engine(engine):
    metadata.create_all(engine)

sa.orm.mapper(Battle_Move, battle_move_table)
sa.orm.mapper(Contest_Move, contest_move_table)

if __name__ eq '__main__':
    engine = sa.create_engine('sql:///:memory:',echo=True);
    add_engine(engine);
