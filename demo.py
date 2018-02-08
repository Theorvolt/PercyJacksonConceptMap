from pynode.main import *

# TODO 
# Determine colors for kingdoms
# Finish relations and add thickness for interactions within the book
# Fix scaling/size nodes differently


characters = ["Percy",
        "Annabeth",
        "Zeus",
        "Poseidon",
        "Chiron",
        "Grover",
        "Luke",
        "Hermes",
        "Hades",
        "Athena",
        "Clarisse",
        "Tyson",
        "Kronos",
        "Nico",
        "Ares",
        "Apollo",
        "Dionysus",
        "Thalia",
        "Rachel"]

sizes = [90.6, 196.0, 26.7, 28.8, 63.1, 128.9, 75.2, 22.7, 24.8, 12.1, 35.5, 64.4, 44.0, 50.9, 24.8, 16.9, 33.8, 57.1,33.1]
originalsize = [906, 1960, 267, 288, 631, 1289, 752, 227, 248, 121, 355, 644, 440, 509, 248, 169, 338, 571, 331]
alliance = [Color.BLUE, Color.GREY, Color.YELLOW, Color.BLUE, Color.GREEN, Color.GREEN, Color.BLACK, Color.GREY, Color.RED, Color.GREY, Color.RED, Color.BLUE, Color.BLACK, Color.RED, Color.RED, Color.GREY, Color.GREY, Color.GREEN, Color.YELLOW, Color.GREY]
positions = [(0,0),(500,400),(400,300),(0,100),(300,200),(222,333),(123,333),(250,250),(111,111),(399,399),
(499,399),(231,400),(111,333),(444,222),(333,66),(66,99),(144,169),(255,7),(475,132),(199,245)
]
relations = {

    "Percy":[["Luke","Former friend"], ["Annabeth","Best friend, love interest"],["Grover","Best friend"],["Chiron","Student"],["Poseidon","son"],["Nico","Ally and friend"],["Tyson","Half brother and close friend"], ["Rachel","Friend and love interest"], ["Ares","Enemy"], ["Clarisse", "Bully victim"]   ],
    "Annabeth":[["Luke","Former love interest"],["Percy","Best friend, love interest"], ["Athena","Daughter"], ["Clarisse","Rivals"], ["Grover","Friend"], ["Chiron","Friend"], ["Thalia", "Close friend"]],
    "Zeus":[["Hermes","Father"],["Apollo","Father"],["Poseidon","Brother and rivals"],["Hades","Brother on good terms"],["Kronos","Son, decapitated by Zeus"],["Dionysus","Father"], ["Ares", "Father"]],
    "Poseidon":[ ["Zeus","Brother"], ["Tyson","Father"], ["Kronos","Son and enemy"], ["Hades","Brother"]],
    "Chiron":[ ["Percy","Mentor"], ["Kronos","Son"], ["Annabeth","Friend"], ["Dionysus","Old friend"], ["Grover","Colleague and friend"] ],
    "Grover":[ ["Percy","Best friend"], ["Dionysus", "Co-worker"], ["Tyson","Akward terms but friendly"], ["Annabeth","friend"]   ],
    "Luke":[["Kronos", "enemy and host of body"], ["Annabeth", "Love interest"], ["Thalia", "close friend"], ["Hermes", "Son"], ["Percy","Enemy"]  ],
    "Hermes":[ ["Zeus","Son"], ["Apollo","Half brother"], ["Athena","Half sister"], ["Luke", "Father"], ["Percy", "Acquainted"] ],
    "Hades":[ ["Nico","Father"], ["Kronos", "Son, was consumed  by Kronos"], ["Zeus", "Brother and rival in dominion"], ["Poseidon", "Brother"] ],
    "Athena":[["Zeus","Daughter"], ["Athena","Mother"], ["Percy","Cautious of"]  ],
    "Clarisse":[ ["Ares", "Daughter"], ["Annabeth","Rivals"], ["Percy","Bully"], ["Luke", "Former friend"] ],
    "Tyson":[ ["Percy", "Half brother"], ["Poseidon", "Father"], ["Annabeth", "Friend"], ["Grover", "Uncomfortable around but friendly"]  ],
    "Kronos":[["Luke", "Parasite to Luke"], ["Zeus", "Father"], ["Chiron", "Father"], ["Hades", "Father"], ["Poseidon", "Father"], ["Percy", "Arch nemesis"], ["Ares", "Tricked to plan war"] ],
    "Nico":[ ["Hades", "Son"], ["Percy", "Close friend"], ["Athena", "acquaintences"], ["Luke", "Enemy"]  ],
    "Ares":[ ["Percy", "Enemy"], ["Zeus", "Son"], ["Clarisse", "Daughter"]   ],
    "Apollo":[ ["Zeus", "Son"], ["Percy", "Friend"], ["Grover", "Ally"] ],
    "Dionysus":[ ["Zeus", "Son"], ["Chiron","Old friends"], ["Percy", "Enjoys mocking"], ["Grover", "Serves in same counsel"] ],
    "Thalia":[ ["Zeus","Daughter"], ["Annabeth", "Close friend"], ["Luke", "Former friend"], ["Percy", "Friendly rival"] ],
    "Rachel":[ ["Percy", "Friend and love interest"], ["Annabeth", "Friend"]]  
}


def begin_graph():
	for i in range(len(characters)):
	    graph.add_node(characters[i])
	    curr_node = graph.nodes()[i]
	    curr_node.set_size(sizes[i]) # will change back to sizes[i] or rescale completely
	    curr_node.set_value_style(40,Color.WHITE,Color.BLACK)
	    curr_node.set_color(alliance[i]) # Not yet finished, will change colors
	    curr_node.set_position(positions[i][0], positions[i][1]) # May leave out locations entirely 
                     
	for s in range(len(characters)):
		for t in range(len(relations[characters[s]])):
			curr_edge = graph.add_edge(characters[s], relations[characters[s]][t][0], relations[characters[s]][t][1], True)
			curr_edge.set_weight_style(40)
			curr_edge.set_width(5) #Will be set to curr_edge.set_width(relations[characters[s]][t][2])




begin_pynode(begin_graph)

