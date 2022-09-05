# 
# 
# TOLERANT TEAMS
# =======================
#
"""
Write a function, tolerant_teams, that takes in a list of rivalries as an argument. 
A rivalry is a pair of people who should not be placed on the same team. 
The function should return a boolean indicating whether or not it is possible 
to separate people into two teams, without rivals being on the same team. 
The two teams formed do not have to be the same size.
"""

# 1. This is a graph problem.
# 2. The players can be represented as nodes and the rivalries can be represented as edges.
# 3. The problem is asking if the graph can be divided into two independent parts, 
# which is the definition of a BIPARTITE graph.
# 4. This problem is similar to the coloring problem.

# Time complexity: O(E) - iterate over all edges in the graph
# Space complexity: O(E) - build the adjacency list

from collections import defaultdict

def tolerant_teams(rivalries):
    # first convert the rivalries into an adjacency list
    graph = adjacency(rivalries)

    # Initialize a dictionary that will keep track of the players and their team.
    # The team will be simply True or False, since there are only two possible teams (bipartite)
    teams = {}

    # Iterate over all possible players. This iterative part is important,
    # in case there are disconnected components.
    for player in graph:
        # if the player is already on a team, skip to next player
        if player in teams:
            continue

        # if the player could not be assigned to a team, stop early and immediately return False
        if not assign(player, graph, teams):
            return False

    # all players assigned, return True
    return True


def assign(player, graph, teams, team = True):
    """
    Attempt to assign a player to a team
    """
    # If the player is already on a team, check if his team is the one we intend
    if player in teams:
        return teams[player] == team

    # Assign the player a team
    teams[player] = team

    # Now attempt to assign all rivals to opposite team
    for rival in graph[player]:
        if not assign(rival, graph, teams, not team):
            return False

    return True

def adjacency(edges):
    """
    Build an adjacency list from a list of edges
    """
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    return graph

# tests
assert tolerant_teams([
  ('alan', 'jj'),
  ('jj', 'richard'),
  ('betty', 'richard'),
  ('jj', 'simcha'),
  ('richard', 'christine')
]) == True

assert tolerant_teams([
  ('alan', 'jj'),
  ('betty', 'richard'),
  ('betty', 'christine'),
  ('jj', 'simcha'),
  ('richard', 'christine')
]) == False

assert tolerant_teams([
  ('cindy', 'anj'),
  ('alex', 'matt'),
  ('alex', 'cindy'),
  ('anj', 'matt'),
  ('brando', 'matt')
]) == True

print("All tests passed!")