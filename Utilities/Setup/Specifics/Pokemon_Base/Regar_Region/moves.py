#!/bin/env python
# add comment latter

moves['HM1'] = Battle_Move('HM1',"Regar","Glitch move that lowers random stat",1,1,0,"None",81,35,0,'user.stats.random(-1,100); user.damage.physical; appear.hypnosis','noop')
moves['HM2'] = Battle_Move('HM2',"Regar","Glitch move that drains HP",2,1,0,"None",177,6,26,'drain.hp; appear.noop','noop')
moves['HM3'] = Battle_Move('HM3',"Regar","Glitch move",1,1,0,"Normal",50,3,59,'if not target.status.asleep then return; drain.hp; appearance.beam["hyper"]','noop')
moves['HM4'] = Battle_Move('HM4',"Regar","Glitch  hyper beam",1,1,0,"Glitch",58,50,12,'user.next_turn="charge"; target.damage.phyiscal; appear.beam["hyper"]','noop')
moves['HM5'] = Battle_Move('HM5',"Regar","Glitch",2,1,0,"Glitch",102,38,6,'target.damage.special; appear.growl','noop')
moves['TM1'] = Battle_Move('TM1',"Regar","Glitched Poison Move",1,1,0,"Normal",36,1,3,'target.status.inflict('poison',30); target.damage.physical; appear.noop','noop')
moves['TM2'] = Battle_Move('TM2',"Regar","Glitched evasion lowering move",1,1,0,"None",15,51,11,'target.stats.evade(-2,100); target.damage.physical; appear.harden','noop')
moves['TM3'] = Battle_Move('TM3',"Regar","Glitched low powe damage move",1,1,0,"None",8,32,57,'target.damage.physical; appear.noop',"noop")
moves['TM4'] = Battle_Move('TM4',"Regar","Glitched noop",3,1,0,"Water",0,18,39,'target.damage.physical; appear.powder["poisonous"]',"noop")
moves['TM5'] = Battle_Move('TM5',"Regar","Glitched evasion increasing move",3,-1,0,",K Pk%sxX",76,30,33,'target.self.evade(+3,100); appear.noop;',"noop")
moves['TM6'] = Battle_Move('TM6',"Regar","Glitched mid damage move",1,1,0,"Poison",55,69,127,'target.damage.physical;appear.tail["whip"]',"noop")
moves['TM7'] = Battle_Move('TM7',"Regar","Glitched random damage move",1,1,0,"Ghost",131,20,0,'target.damage.random;appear.cut["generic"]',"noop")
moves['TM8'] = Battle_Move('TM8',"Regar","Glitched move that damages",2,1,0,"Glitch",30,17,20,'missed(user.damage(-user.HP.max*.5); target.damage.special; appear,sratch("bland");',"noop")
moves['TM9'] = Battle_Move('TM9',"Regar","Glitched Jihad move",1,1,0,"IIIItoto",255,33,16,'target.damage.physical; user.faint; appear.punch('fire');',"noop")
moves['TM10'] = Battle_Move('TM10',"Regar","Glitched moderate attack move",1,1,0,"Normal",74,31,0,'target.damage.physical; appear.focus["energy"]',"noop")
moves[''] = Battle_Move('',"Regar","",,1,0,"",,,,'',"noop")
moves[''] = Battle_Move('',"Regar","",,1,0,"",,,,'',"noop")


location.moves[''] = Move_Hex('',"Regar-RB",0xC4)
