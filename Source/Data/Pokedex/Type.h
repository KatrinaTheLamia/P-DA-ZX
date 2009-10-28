
// Standard Template Libraries

#ifdef HAS_STD
include <vector>
#else // does not HAS_STD
include <Flow/fake_vector>
#endif

// PDA*ZX specific libraries
include <Flow/widget>
include <Flow/types>

namespace RaddTeam {
	namespace PDA {

		// This is our type object. This generally handles all of the
		// typing in a PDA ZX type application
		class Type : Widget {
			protected:
				// this should match its ID in the table of 
				// types.
				RaddTeam::PDA::IDREF &entry_id;
				// A Unicode string stating the type. Note:
				// this is set up to allow localisation in 
				// software using this framwork.
				RaddTeam::UString name;
				// these point to other types. This includes 
				// information on what types this type 
				// defenses are towards, and what this is 
				// good as an offense towards.
				// This is mostly for double checking if we 
				// have some sort of bug in what we are 
				// looking at for input.
				RaddTeam::PDA::Type_Table
					def_no_effect, 
					def_reduced_effect,
					def_super_effect,
					att_no_effect,
					att_reduced_effect,
					att_super_effect;
				// Keep track of what table refers to us.
				std::vector<RaddTeam::PDA::Type_Table &>
					refers_from;
			public:
				Type(RaddTeam::PDA::Type_Table &first_ref) {
					this->refers_from.push(first_ref);
					this->Capabilities.push(UQ("implements|orphaned"))
						->push(UQ("code|set_Name"));
						->push(UQ("code|get_Name"));
						->push(UQ("code|set_resistant_to"));
						->push(UQ("code|set_weakness_to"));
						->push(UQ("code|set_strong_to"));
						->push(UQ("code|set_resistant_from"));
						->push(UQ("code|set_weakness_from"));
						->push(UQ("code|set_strong_from"));
						->push(UQ("code|_set_entry"));
						->push(UQ("code|_update_neighbours"));
						->push(UQ("todo|get_off_weakness"));
						->push(UQ("todo|get_off_strengths"));
						->push(UQ("todo|get_off_resists"));
						->push(UQ("todo|get_def_weakness"));
						->push(UQ("todo|get_def_strenghts"));
						->push(UQ("todo|get_def_resists"));
						->push(UQ("todo|notify_resists"));
						->push(UQ("todo|notify_strengths"));
						->push(UQ("todo|notify_weaknesses"));
						->push(UQ("todo|launch_notify_threads"));
				}
			// Setting accessors
			public:
				Type *set_Name(RaddTeam::UString new_name) { 
					handle_orphan();
					name = new_name;
					return this;
				}
				Type *set_resistant_to(RaddTeam::PDA::IDREF resist) {
					handle_orphan();
					return _set_entry(UQ("English|Resist_Att"), resist)
						->_update_neighbours(UQ("English|Resist_Def"));
				}
				Type *set_weakness_to(RaddTeam::PDA::IDREF weak) {
					handle_orphan();
					return _set_entry(UQ("English|Weak_Att"), weak)
						->_update_neighbours(UQ("English|Strong_Def"));
				}
				Type *set_strong_to(ReadTeam::PDA::IDREF strong) {
					handle_orphan();
					return _set_entry(UQ("English|Strong_Att"), strong)
						->_update_neighbours(UQ("English|Weak_Def"));
				}
				Type *set_resistant_from(RaddTeam::PDA::IDREF resist) { 
					handle_orphan();
					return _set_entry(UQ("English|Resist_Def"), resist)
						->_update_neighbours(UQ("English|Resist_Att"), resist);
				}
				Type *set_weakness_from(RaddTeam::PDA::IDREF weak) {
					handle_orphan();
					return _set_entry(UQ("English|Weak_Def"), weak)
						->_update_neighbours(UQ("English|Strong_Att"));
				}
				Type *set_strong_from(RaddTeam::PDA::IDREF strong) {
					handle_orphan();
					return _set_entry(UQ("English|Strong_Def"), strong)
						->_update_neighbours(UQ("English|Weak_Def"));
				}
			// Retrieve accessors
			public:
				RaddTeam::UString get_Name() {
					handle_orphan();
					return name;
				}

			protected:
				RaddTeam::PDA::Type _set_entry(RaddTeam::UString target_table, 
						               RaddTeam::PDA::IDREF from) {
					handle_orphan();
					if(not tactics[target_table].has(UQ("code|has_entry")) |
					   tactics[target_table].has_entry(from)) {
						return this;
					}
					tactics[target_table].push(from);
					return this;
				}
				RaddTeam::PDA::Type _update_neighbours(RaddTeam::UString target_table,
						                       RaddTeam::PDA::IDREF target) {
					handle_orphan();
					for(refers_form::iterator table =
					    refers_from.begin();
					    table < refers_from.end();
					    table++) {
						if(refers_from[table].has(UQ("code|type")) &&
						   refers_from[table].type(target).has(UQ("code|_set_entry"))) {
							refers_from[table].type(target)._set_entry(target_get);
						}

					}
				}
		};

	}
}

