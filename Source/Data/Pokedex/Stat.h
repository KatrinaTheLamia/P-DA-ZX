
/* Blah */

/* P*DA Specific Libraries */

#include <PDA/Flow/widget>
#include <PDA/types>

namespace RaddTeam {
	namespace PDA {
		class Stat : Widget {
			protected:
				/* What is this stat called? */
				RaddTeam::UString _name;
				/* The current stat level */
				RaddTeam::Number _current;
				/* Individual Values */
				const RaddTeam::IV _IV;
				/* Effort Values Post-Celebi */
				RaddTeam::EVs _EVs;
				/* Stat Experience Pre-Celebi */
				RaddTeam::Stat_Exp _Experience;
			public:
				/* Standard constructor */
				Stat(RaddTeam::UString name, RaddTeam::IV IV) : _name(name), _IV(IV) { }

			public:
				/* Behaviour: on setting return self. Else return its name name */
				name(RaddTeam::UString name = nil) {
					if(name != nil) {
						_name = name;
						return *this;
					}
					return _name;
				}

				current(RaddTeam::Number new_current = nil) {
                                        if(new_current != nil) {
						_current = current;
						return *this;
					}
					return _current;
				}

				evs(RaddTeam::EVs new_ev = nil) {
					if(new_ev != nil) {
						_EVs += new_ev;
						return *this;
					}
					return _EVs;
				}

				stat_exp(RaddTeam::Stat_Exp new_experience = nil) {
					if(new_experience != nil) {
						_Experience += new_experience;
						return *this;
					}
					return _Experience;
				}
			public:
				/* IV should be set at the begining. They are read only */
				iv() { return _IV; }
		};
	};
};

