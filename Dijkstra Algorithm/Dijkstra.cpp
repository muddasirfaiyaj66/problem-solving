#include <bits/stdc++.h>
using namespace std;

const int INF = INT_MAX;

vector<vector<pair<int,int>>> adj; 
vector<int> parent;

void addEdge(int u, int v, int w, bool undirected = true) {
    adj[u].push_back({v, w});
    if (undirected) adj[v].push_back({u, w});
}

int minDistance(vector<int>& dist, vector<bool>& visited, int n) {
    int minVal = INF;
    int minIndex = -1;
    for (int v = 0; v < n; v++) {
        if (!visited[v] && dist[v] < minVal) {
            minVal = dist[v];
            minIndex = v;
        }
    }
    return minIndex;
}

void dijkstra(int src, int n) {
    vector<int> dist(n, INF);
    vector<bool> visited(n, false);
    parent.assign(n, -1);

    dist[src] = 0;

    for (int count = 0; count < n - 1; count++) {
        int u = minDistance(dist, visited, n);
        if (u == -1) break;
        visited[u] = true;

        for (auto [v, w] : adj[u]) {
            if (!visited[v] && dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                parent[v] = u;
            }
        }
    }

    cout << "Shortest distances from source " << src << ":\n";
    for (int i = 0; i < n; i++) {
        cout << "To " << i << " = " 
             << (dist[i] == INF ? -1 : dist[i]) << "\n";
    }
}

void printPath(int dest) {
    if (parent[dest] == -1) {
        cout << dest << " ";
        return;
    }
    printPath(parent[dest]);
    cout << dest << " ";
}

int main() {
    int n = 5;
    adj.assign(n, {}); // initialize adjacency list

    addEdge(0, 1, 10);
    addEdge(0, 4, 5);
    addEdge(1, 2, 1);
    addEdge(1, 4, 2);
    addEdge(2, 3, 4);
    addEdge(3, 0, 7);
    addEdge(3, 2, 6);
    addEdge(4, 2, 9);
    addEdge(4, 3, 2);

    int src = 0;
    dijkstra(src, n);

    int dest = 3;
    cout << "\nPath from " << src << " to " << dest << ": ";
    printPath(dest);

    cout << "\nCost = (see above output)" << endl;
    return 0;
}
