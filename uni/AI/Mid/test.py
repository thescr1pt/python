from graphviz import Digraph

done = set()
graph = Digraph()


def solve(b):
    graph.node(str(b), label=str(b))

    if b[0] == 4:
        return
    done.add(b)

    if b[0] > 0:
        t = min(5 - b[1], b[0])
        new_state = (b[0] - t, b[1] + t, b[2])
        if new_state not in done:
            graph.edge(str(b), str(new_state))
            solve(new_state)

        t = min(3 - b[2], b[0])
        new_state = (b[0] - t, b[1], b[2] + t)
        if new_state not in done:
            graph.edge(str(b), str(new_state))
            solve(new_state)

    if b[1] > 0:
        t = min(8 - b[0], b[1])
        new_state = (b[0] + t, b[1] - t, b[2])
        if new_state not in done:
            graph.edge(str(b), str(new_state))
            solve(new_state)

        t = min(3 - b[2], b[1])
        new_state = (b[0], b[1] - t, b[2] + t)
        if new_state not in done:
            graph.edge(str(b), str(new_state))
            solve(new_state)

    if b[2] > 0:
        t = min(8 - b[0], b[2])
        new_state = (b[0] + t, b[1], b[2] - t)
        if new_state not in done:
            graph.edge(str(b), str(new_state))
            solve(new_state)

        t = min(5 - b[1], b[2])
        new_state = (b[0], b[1] + t, b[2] - t)
        if new_state not in done:
            graph.edge(str(b), str(new_state))
            solve(new_state)


solve((8, 0, 0))

# Render the graph to a file
graph.render("state_tree", format="png", view=True)
